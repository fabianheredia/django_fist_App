from . import views as frontendview
from django.urls import path
from django.conf.urls import url, include, static
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [
    path('',frontendview.home,name='home'),
    url(r'^signup/$', frontendview.signup, name='signup'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    url(r'^nuevoevento/$', frontendview.newEvento.as_view(), name='nuevo'), 
    url(r'^ListaEventos$', frontendview.EventosL.as_view(), name='listaEventos'),
     url(r'^(?P<pk>\d+)$', frontendview.detalleEvento.as_view(), name='detalle'), 
     url(r'^editar/(?P<pk>\d+)$', frontendview.modificacionEvento.as_view(), name='editar'), 
     url(r'^borrar/(?P<pk>\d+)$', frontendview.borrarEvento.as_view(), name='borrar'),
]
