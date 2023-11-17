from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):
    '''
    Moshe L. 14/11/2023 13:37
    '''
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    available = models.IntegerField(default=1)
    client = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'date: {self.date}, hour: from {self.start_time} to {self.end_time}, client: {self.client}'
