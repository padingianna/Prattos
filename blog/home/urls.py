from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index,name='Home'),
    path('nosotros', views.nosotros,name='Nosotros'),
    path('contacto', views.contacto,name='Contacto'),







]