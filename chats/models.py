
from django.db import models
from django.contrib.auth.models import User

class BPMs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)  # Will be auto-generated
    xml_file = models.FileField(upload_to='bpmn_files/')
    description = models.TextField(blank=True, null=True)  # Will be auto-generated
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"BPMN {self.id}"

class Query(models.Model):
    id = models.AutoField(primary_key=True)
    bpm = models.ForeignKey(BPMs, on_delete=models.CASCADE)
    text = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query {self.id} on {self.bpm.title}"
