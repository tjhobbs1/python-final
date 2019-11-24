from django.urls import path
from .views import postFlightView


urlpatterns = [
    path('', postFlightView.as_view(), name="postflight"),
    
]