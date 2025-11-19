from django.urls import path
from .views import delete_post,edit_post,detail_post,create_post, home

urlpatterns = [
    path("", home, name="home"),
    path("delete_post/<int:todo_id>/", delete_post, name="delete_post"),
    path("edit_post/<int:todo_id>/", edit_post, name="edit_post"),
    path("detail_post/<int:todo_id>/", detail_post, name="detail_post"),
    path("create_post/", create_post, name="create_post"),
]