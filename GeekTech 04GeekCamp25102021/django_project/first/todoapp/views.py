from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoList
import random
# Create your views here.

def hello(request):
    return HttpResponse(f"<h1> Random number: {random.randint(1,100)} </h1>")

def todoapp_view(request):
    all_todo_items = TodoList.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})




def add_view(request):
    x = request.POST['content']
    new_item = TodoList(content = x) 
    new_item.save()
    return HttpResponseRedirect('/todo/')





def deleteTodoView(request, i):
    y = TodoList.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todo/')