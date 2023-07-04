from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import todo

app_name = "TodoApp"
urlpatterns = [
     path("", todo.index, name = "Index"),
     path("details/<str:todo_key>/", todo.list, name = "ViewTodo"),
     path("update/<str:todo_key>/", todo.update, name = "UpdateTodo"),
     path("delete/<str:todo_key>/", todo.delete, name = "DeleteTodo"),
     path("create/", todo.create, name = "CreateTodo"),
]