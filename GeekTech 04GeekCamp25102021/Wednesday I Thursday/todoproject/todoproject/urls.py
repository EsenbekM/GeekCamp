from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', views.todoappView),
    path('addTodoItem/', views.addTodoView),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView), 
    path('random/', views.random_num),
    path('api/v1/products/', views.ProductListAPIView.as_view()),
    path('api/v1/productss/<int:id>/', views.ProductDetailAPIView.as_view()),
]
