from django.db import models
from datetime import datetime

def get_current_date():
    return datetime.today().date()
# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    priority = models.IntegerField()
    start_date = models.DateField(default=get_current_date)
    end_date = models.DateField(default=get_current_date)
    description = models.CharField(max_length = 400, default="")
    status = models.CharField(max_length = 100, default="pending")