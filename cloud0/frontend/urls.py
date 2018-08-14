from . import views as frontendview
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [
    path('',frontendview.home,name='home'),
    url(r'^signup/$', frontendview.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html')),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='login.html')),
   
]
