from django.urls import path
from . import views

# This just helps uniquely identiy all of the URLs 
app_name = "tasks"

urlpatterns = [
    path("", views.index, name = "index"),
    path("add", views.add, name = "add")
]