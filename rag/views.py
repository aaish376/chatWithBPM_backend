import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import convert_bpmn_to_nl, store_nl_description, generate_query_response

@csrf_exempt
def bpmn_to_nl_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            xml_content = data.get("xml_content", "")

            if not xml_content:
                return JsonResponse({"error": "No BPMN XML provided"}, status=400)

            nl_description = convert_bpmn_to_nl(xml_content)
            store_nl_description(nl_description)  # Store for RAG use

            return JsonResponse({"nl_description": nl_description})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def query_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query_text = data.get("query", "")

            if not query_text:
                return JsonResponse({"error": "No query provided"}, status=400)

            response = generate_query_response(query_text)

            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
