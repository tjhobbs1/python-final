from django import forms
from .models import PostFlight
import datetime 
from django.contrib.admin.widgets import AdminTimeWidget
from account.models import Account
from django.forms import ModelChoiceField


BASE_CHOICES = (
    ('', 'Select a Base'),
    ('AirMed1', 'AirMed 1'),
    ('AirMed2', 'AirMed 2'),
    ('AirMed3', 'AirMed 3'),
    ('AirMed4', 'AirMed 4'),
)

AIRFRAME_CHOICES = (
    ('', 'Select a Transport Type'),
    ('Ground', 'Ground'),
    ('Air', 'Air'),
)

TAILNUM_CHOICES = (
    ('', 'Select a Tail Number'),
    ('911ED', '911ED'),
    ('911KX', '911KX'),
    ('530LN', '530LN'),
    ('534LN', '534LN')
)



class NameChoiceField(ModelChoiceField):
    """Overrides the ModelChoiceField in order to get the value to display the full name"""
    def label_from_instance(self,obj):
        return '{last_name} , {first_name}'.format(last_name=obj.last_name, first_name = obj.first_name)

class PostFlightForm(forms.Form):
    
   
    transport_date = forms.DateField(input_formats=['%Y-%m-%d'],label='Transport Date' ,widget=forms.TextInput(attrs={'id':'datepicker'}))
    flight_num = forms.CharField(label="Flight Number")
    base = forms.CharField(label="",widget=forms.Select(choices=BASE_CHOICES))
    transport_type = forms.CharField(label='',widget=forms.Select(choices=AIRFRAME_CHOICES))
    tail_num = forms.CharField(label='',widget=forms.Select(choices=TAILNUM_CHOICES))
    med_crew_1 = forms.ModelChoiceField(queryset = Account.objects.all().exclude(job_title="dispatcher").exclude(job_title="pilot").exclude(job_title="programmer").exclude(job_title="mechanic").exclude(job_title="flightMedic"))
    med_crew_2 = forms.ModelChoiceField(queryset = Account.objects.all().exclude(job_title="dispatcher").exclude(job_title="pilot").exclude(job_title="programmer").exclude(job_title="mechanic"))
    pilot = forms.ModelChoiceField(queryset = Account.objects.all().exclude(job_title="dispatcher").exclude(job_title="flightNurse").exclude(job_title="programmer").exclude(job_title="mechanic").exclude(job_title="flightMedic"))
    dispatcher = forms.ModelChoiceField(queryset = Account.objects.all().exclude(job_title="pilot").exclude(job_title="flightNurse").exclude(job_title="programmer").exclude(job_title="mechanic").exclude(job_title="flightMedic"))
    
    activity_flight = forms.CharField(label='',widget=forms.Select(
        choices=[
        ('', 'Select the Activity of the transport'), 
        ('Completed', 'Completed By Air'),
        ('Completed','Completed By Ground'),
        ('Completed','Aborted Flight, Completed by Ground'),
        ('Completed','Patient Care Only, No Transport'),
        ('Aborted','Aborted Flight, No Patient Contact')
        ]))
    scene_hosp = forms.CharField(label='Transport Type',widget=forms.RadioSelect(choices=[('Scene','Scene'),('Interfacility','Interfacility')]))
    start_time = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
    lift_time = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
    at_recieving_time = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
    at_patient_time = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
    depart_recieving_time = forms.TimeField(widget=AdminTimeWidget(format='%H:%M'))
    ifr_vfr = forms.CharField(label='',widget=forms.RadioSelect(choices=[('IFR','IFR'),('VFR','VFR')]))
    weather_issues = forms.CharField(label='Weather Issues',widget=forms.RadioSelect(choices=[('Yes','Yes'),('No','No')]),initial='No')
    aviation_issues = forms.CharField(label='Aviation Issues',widget=forms.RadioSelect(choices=[('Yes','Yes'),('No','No')]),initial='No')
    maintenance_issues = forms.CharField(label='Maintenance Issues',widget=forms.RadioSelect(choices=[('Yes','Yes'),('No','No')]),initial='No')
    aviation_issues_comments = forms.CharField(widget=forms.Textarea(attrs={'cols' :80,'rows': 10}))
    priority_level = forms.CharField(widget=forms.RadioSelect(choices=[('1','Priority 1'),('2','Priority 2'),('NoIssues','No Issues')]))

  


    def __init__(self, *args, **kwargs):
        
        super(forms.Form, self).__init__(*args, **kwargs)
        
       
        

        
       




    