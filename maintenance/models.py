from django.db import models
from django.utils import timezone


class Maintenance (models.Model):
    company = models.CharField(max_length= 255, null= True)
    departament = models.CharField(max_length= 255, null= True)
    section = models.CharField(max_length= 255, null= True)
    employee = models.CharField(max_length= 255, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section