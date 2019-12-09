from django.urls import path
from . import views


urlpatterns = [
    
    path('flightdetail/<str:id>/',views.flight_detail_view,name="detail"),
    path('',views.dashboardView, name="dashboard")
    
]