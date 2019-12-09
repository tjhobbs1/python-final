from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.registration_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('',views.account_view, name='account'),
    path('test/',views.must_authenticate_view, name="must_authenticate")
    
    # path('', views.postflight, name="postflight"),
    # path('submitted/',views.submitted,name="submitted"),
    
   
    
]