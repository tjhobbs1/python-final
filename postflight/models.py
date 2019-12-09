from django.contrib.auth import get_user_model
from django.db import models
from datetime import date
from account.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

User = get_user_model()


# Create your models here.

class PostFlight(models.Model):
    transport_date = models.DateField(default=date(2019,11,1))
    flight_id = models.CharField(primary_key=True,unique=True, max_length=100,default='')
    base = models.CharField(max_length=100,default='')
    transport_type = models.CharField(max_length=100,default='')
    tail_num = models.CharField(max_length = 50,default='')
    med_crew_1 = models.CharField(max_length=100,default='')
    med_crew_2 = models.CharField(max_length=100,default='')
    pilot = models.CharField(max_length=100,default='')
    dispatch = models.CharField(max_length=100,default='')
    activity_flight = models.CharField(max_length=100,default='')
    scene_hosp = models.CharField(max_length=100,default='')
    assigned_time = models.TimeField(blank= True,default='00:00')
    lift_time = models.TimeField(blank= True,default='00:00')
    at_sending_time = models.TimeField(blank= True,default='00:00')
    at_patient_time = models.TimeField(blank= True,default='00:00')
    depart_sending_time = models.TimeField(blank= True,default='00:00')
    ifr_vfr = models.CharField(max_length=100,default='')
    weather_issues = models.CharField(max_length=100,default='')
    aviation_issues = models.CharField(max_length=100,default='')
    maintenance_issues = models.CharField(max_length=100,default='')
    aviation_issues_comments = models.TextField(max_length=1000,default='')
    severity_index = models.CharField(max_length=100,default='')

   

    def __str__(self):
        return self.flight_id

    def summary(self):
        return self.flight_id
    
    def get_absolute_url(self):
        return reverse("dashboard:detail", kwargs={"id": self.flight_id}) 
    
    def get_absolute_url2(self):
        return reverse("dashboard:detail", kwargs={"id": self.flight_id}) 




    