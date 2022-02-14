
from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('todo/', views.todoapp_view),
    path('todo/additem/', views.add_view),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView), 

]
