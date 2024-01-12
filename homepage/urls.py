from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('', homepage, name="homepage"),
    path('', include('authenticate.urls')),
    path('about', about, name="about"),
    path('service', service, name="service"),
    path('contact', contact, name="contact"),
    path('quotation', quotation, name='quotation'),
    path('edit', edit, name='edit'),
    path('new_id', new_id, name='new_id'),
    path('edit_details/<str:ro>', edit_details, name='edit_details'),
    path('delete/<str:ro>', delete, name='delete'),
    path('track', track, name='track')
]