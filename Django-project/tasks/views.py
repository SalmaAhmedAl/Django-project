from django.shortcuts import render

# Global variable that the entire application gonna have access to.
tasks = ["Foo", "Bar", "Baz"]
# Create your views here.
def index(request):
     return render(request, "tasks/index.html", {
        "tasks" : tasks
     })

def add(request):
    return render(request, "tasks/add.html")
