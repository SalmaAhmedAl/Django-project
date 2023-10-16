from django import forms
from django.shortcuts import render

# Global variable that the entire application gonna have access to.
tasks = ["Foo", "Bar", "Baz"]

# This class will inherit from forms.Form
# Inside this class I will define all fields I'd like for this field to have.
# all of the inputs that I'd like the user to prodive.
class NewTaskForm(forms.Form):
   task = forms.CharField(label="New Task ")
   # Min & Max make client-server validation! The server isn't getting any of this data.
   priority = forms.IntegerField(label="Priority", min_value=1, max_value=10 )


# Create your views here.
def index(request):
     return render(request, "tasks/index.html", {
        "tasks" : tasks
     })

def add(request):
    return render(request, "tasks/add.html", {
      # I'm gonna create a new task form, pass it into this add.html template.
      "form" : NewTaskForm()
    })
