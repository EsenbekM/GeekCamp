from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoListItem, Product
import random


from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProductsSerializer

def random_num(request):
    return HttpResponse(f"Рандомное число: {random.randint(1, 100)}")

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 
 
def addTodoView(request): 
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'id'