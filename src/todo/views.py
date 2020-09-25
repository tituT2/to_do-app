from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

###############################################


def index(request):
    if request.user.is_authenticated:
        user = request.user
        item_list = user.todo_user.all().order_by("-date")
        if request.method == "POST":
            form = TodoForm(request.POST)
            if form.is_valid():
                DataForm = form.save(commit=False)
                DataForm.user = request.user
                DataForm.save()
                return redirect("todo")
        form = TodoForm()
    else:
        form = ""
        item_list = ""

    page = {
        "form": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, "todo/index.html", page)


### function to remove item , it recive todo item id from url ##
@login_required
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect("todo")
