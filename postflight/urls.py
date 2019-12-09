from django.urls import path, include
from . import views


urlpatterns = [
    #path('', views.dashboardView, name="dashboard"),
    path('postflight/', views.postflight, name="postflight"),
    path('submitted/',views.submitted,name="submitted"),
    path('error/',views.errorPage,name="error"),
    
    
    
   
    
]