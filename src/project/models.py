from django.db import models

# Create your models here.
# Models are linked to our database
class ProjectPost(models.Model):
    title = models.TextField()
    description = models.TextField(null=True, blank=True)

