from django.urls import path
from . import views

urlpatterns = [
    path(route='helloWorld/', view=views.helloWorld)
]