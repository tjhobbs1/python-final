from django.urls import path
from .views import dashboardView


urlpatterns = [
    path('', dashboardView.as_view(), name="dashboard")
]