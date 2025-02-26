from django.db import models
class Service(models.Model):
    service_name=models.CharField(max_length=50)
    service_title=models.CharField(max_length=50)
    service_des=models.TextField()
