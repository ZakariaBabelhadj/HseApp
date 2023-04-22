from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='main'),
    path('SignUp/', views.SignUp, name="SignUp"),
    path('AddLois/', views.AddLois, name="AddLois"),
    path('Login/', views.Login, name='Login'),
    path('loisAdmin', views.loisAdmin, name='loisAdmin')
]