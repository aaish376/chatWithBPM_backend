from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import BPMs, Query
from .utils import convert_bpmn_to_nl, generate_query_response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BPMs
from .utils import convert_bpmn_to_nl  # assuming you have this utility

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_bpmn(request):
    if "file" not in request.FILES:
        return Response({"error": "No file provided"}, status=400)

    file = request.FILES["file"]
    user = request.user  # Provided by JWT authentication

    xml_text = file.read().decode("utf-8")

    bpm = BPMs.objects.create(
        user=user,
        xml_content=xml_text,
    )
    bpm.title = f"BPMN Process {bpm.id}"
    bpm.description = convert_bpmn_to_nl(xml_text)
    bpm.save()

    return Response({
        "bpmid": bpm.id,
        "title": bpm.title,
        "description": bpm.description
    }, status=201)

# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def upload_bpmn(request):
#     if "file" not in request.FILES:
#         return Response({"error": "No file provided"}, status=400)

#     file = request.FILES["file"]
#     user = request.user  # JWT will provide the authenticated user

#     saved_path = default_storage.save(f"bpmn_files/{file.name}", ContentFile(file.read()))

#     bpm = BPMs.objects.create(user=user, xml_file=saved_path)
#     bpm.title = f"BPMN Process {bpm.id}"
#     bpm.description = convert_bpmn_to_nl(saved_path)
#     bpm.save()

#     return Response({
#         "bpmid": bpm.id,
#         "title": bpm.title,
#         "description": bpm.description
#     }, status=201)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def send_query(request):
    bpm_id = request.data.get("bpmid")
    query_text = request.data.get("query")

    bpm = get_object_or_404(BPMs, id=bpm_id, user=request.user)

    print(bpm.description)

    response_text = generate_query_response(bpm.description, query_text)
    query = Query.objects.create(bpm=bpm, text=query_text, response=response_text)

    return Response({
        "id": query.id,
        "text": query.text,
        "response": query.response,
        "created_at": query.created_at.isoformat()
    }, status=201)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_chats(request):
    bpmns = BPMs.objects.filter(user=request.user).order_by("-id").values("id", "title", "description")  # Order by descending ID
    
    # Print all BPMNs in the console
    print("Fetched BPMNs for user:", request.user.username)
    for bpm in bpmns:
        print(f"ID: {bpm['id']}, Title: {bpm['title']}, Description: {bpm['description']}")

    return Response(list(bpmns))



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_chat_messages(request, bpmid):
    bpm = get_object_or_404(BPMs, id=bpmid, user=request.user)
    queries = Query.objects.filter(bpm=bpm).values("id", "text", "response", "created_at")
    return Response(list(queries))


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_chat(request, bpmid):
    bpm = get_object_or_404(BPMs, id=bpmid, user=request.user)

    # Delete related queries first
    Query.objects.filter(bpm=bpm).delete()

    # # Delete BPMN file from storage
    # if bpm.xml_file:
    #     default_storage.delete(bpm.xml_file.path)

    # Delete BPMN record
    bpm.delete()

    return Response({"message": "Chat and related data deleted successfully"}, status=200)
