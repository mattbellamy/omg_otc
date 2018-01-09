from django.db import models

# Create your models here.
class Notifications(models.Model):
    notificationType = models.CharField(max_length=45, blank=True, null=True)