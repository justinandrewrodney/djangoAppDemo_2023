from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def main(request):
    print(request)
    return HttpResponse('<h1>Main</h1>')

def helloWorld(request):
    return render(request, 'helloWorld.html', {'name': "Justin"})

def index(request, name):
    print(request)
    # toDoList = ToDoList.objects.get(id=id)
    toDoList = ToDoList.objects.get(name=name)
    item = toDoList.item_set.get(id=1)

    return HttpResponse("<h1>%s</h1><br></br><h1>%s</h1>" %(toDoList.name, item.text))