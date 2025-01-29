from django.urls import path
from .views import *

urlpatterns = [
    path('info/', info_api, name='info_api'),
]
