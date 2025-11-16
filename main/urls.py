from django.urls import path
from .views import delete_todo,edit_todo, home

urlpatterns = [
    path("", home),
    path("delete/<int:todo_id>/", delete_todo),
    path("edit/<int:todo_id>/", edit_todo),
]