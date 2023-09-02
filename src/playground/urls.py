from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.main, name="Main"),
    path(route='helloWorld/', view=views.helloWorld, name="Hello World"),
    path(route='<int:id>/', view=views.index, name="Index")
]