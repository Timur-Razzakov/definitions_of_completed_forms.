from django.urls import path

from .views import *

# app_name = 'scraping'
urlpatterns = [
    path('get_form', check_form_view, name='home'),
    path('add_forms/', add_form_view, name='add_forms'),
]
