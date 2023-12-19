from django.db import models

# Create your models here.
class FormData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
