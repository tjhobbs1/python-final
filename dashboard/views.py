from account.models import Account
from postflight.models import PostFlight
from django.shortcuts import render, get_object_or_404

# from django.views.generic import(
# TemplateView, 
# CreateView, 
# DetailView, 
# ListView, 
# UpdateView, 
# DeleteView)


def flight_detail_view(request,id):
    
    obj = get_object_or_404(PostFlight, flight_id=id)
    context ={
        "object" : obj
    }
    return render(request, "flightdetail.html", context)

def dashboardView(request):
    obj1 = PostFlight.objects.filter(severity_index="1")
    obj2 = PostFlight.objects.filter(severity_index="2")
    objNo = PostFlight.objects.filter(severity_index="NoIssues")
    context={
        "object1" :obj1,
        "object2" :obj2,
        "objectNo" :objNo,

    }
    return render(request, "home.html",context)


# class dashboardView(ListView):
#     queryset = PostFlight.objects.all()
#     template_name = 'home.html'

# class flightDetailView(DetailView):
#     queryset = PostFlight.objects.all()
#     template_name = 'flightdetail.html'