from django.shortcuts import render, redirect, get_object_or_404
from .models import PostFlight
from django.contrib.auth import login, authenticate, logout
from account.models import Account

from .forms import PostFlightForm


def postflight(request):
  
    if not request.user.is_authenticated:
        return redirect("login")
 
    form = PostFlightForm(request.POST or None)
    account = Account.objects.all()

    if request.method == 'POST':
      flight_crew_1_first_name = Account.objects.get(id=request.POST['med_crew_1']).first_name
      flight_crew_1_last_name = Account.objects.get(id=request.POST['med_crew_1']).last_name
      flight_crew_1_commit = f'{flight_crew_1_first_name} {flight_crew_1_last_name}'

      flight_crew_2_first_name = Account.objects.get(id=request.POST['med_crew_2']).first_name
      flight_crew_2_last_name = Account.objects.get(id=request.POST['med_crew_2']).last_name
      flight_crew_2_commit = f'{flight_crew_2_first_name} {flight_crew_2_last_name}'

      pilot_first_name = Account.objects.get(id=request.POST['pilot']).first_name
      pilot_last_name = Account.objects.get(id=request.POST['pilot']).last_name
      pilot_commit = f'{pilot_first_name} {pilot_last_name}'

      dispatcher_first_name = Account.objects.get(id=request.POST['dispatcher']).first_name
      dispatcher_last_name = Account.objects.get(id=request.POST['dispatcher']).last_name
      dispatcher_commit = f'{dispatcher_first_name} {dispatcher_last_name}'

        
      if form.is_valid():
        postflight = PostFlight()
        
        postflight.transport_date = form.cleaned_data['transport_date']
        postflight.flight_id = form.cleaned_data['flight_num']
        postflight.base = form.cleaned_data['base']
        postflight.transport_type = form.cleaned_data['transport_type']
        postflight.tail_num = form.cleaned_data['tail_num']
        postflight.med_crew_1 = flight_crew_1_commit
        postflight.med_crew_2 = flight_crew_2_commit
        postflight.pilot = pilot_commit
        postflight.dispatch = dispatcher_commit
        postflight.activity_flight = form.cleaned_data['activity_flight']
        postflight.scene_hosp = form.cleaned_data['scene_hosp']
        postflight.assigned_time = form.cleaned_data['start_time']
        postflight.lift_time = form.cleaned_data['lift_time']
        postflight.at_sending_time = form.cleaned_data['at_recieving_time']
        postflight.at_patient_time = form.cleaned_data['at_patient_time']
        postflight.depart_sending_time = form.cleaned_data['depart_recieving_time']
        postflight.ifr_vfr = form.cleaned_data['ifr_vfr']
        postflight.weather_issues = form.cleaned_data['weather_issues']
        postflight.aviation_issues = form.cleaned_data['aviation_issues']
        postflight.maintenance_issues = form.cleaned_data['maintenance_issues']
        postflight.aviation_issues_comments = form.cleaned_data['aviation_issues_comments']
        postflight.severity_index = form.cleaned_data['priority_level']
        postflight.save()
        
        
        return redirect('submitted')
      else:
        return render(request,'postflight.html',{"form" : form,'error' : 'Everything is required'}) 
        
    else:
      context = {
        'form': form,
        'account' : account,
       
    }
       
      return render(request,'postflight.html',context)
  


def submitted(request):
  
    return render(request,'submitted.html')

def errorPage(request):
  """This will render if there is an error. """
  user = request.user
  if user.is_authenticated:
    if user.user_role =='admin':
      return  render(request,'error.html')
    else:
      return  render(request,'submitted.html')
  else:
    return  render(request,'submitted.html')



  

       


