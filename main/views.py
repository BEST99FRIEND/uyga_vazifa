from django.shortcuts import render,redirect
from main.models import Todo

def home(request):
    data = {
        'todos':Todo.objects.all()
    }
    return render(request, 'todo.html', context=data)

def delete_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except:
        return render(request,'delete.html',{'message': 'Bunday topshiriq mavjud emas'})

    if request.method == "POST":
        todo.delete()
        return redirect("/")


    return render(request, "delete.html", {'todo': todo})

def edit_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id)
    except:
        return render(request,'edit.html',{'message': 'Bunday topshiriq mavjud emas'})
    
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect("/")
    
    return render(request,"edit.html", {"todo": todo})