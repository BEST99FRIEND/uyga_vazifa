from django.shortcuts import render,redirect
from main.models import Post

def home(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        status = request.POST.get("status")
        print(title,desc,status)
        Post.objects.create(
            title=title,
            desc=desc,
            tatus=status
        )
        return redirect("/")
    data = {
        'posts':Post.objects.all()
    }
    return render(request, 'index.html', context=data)

def delete_post(request, todo_id):
    try:
        posts = Post.objects.get(id=todo_id)
    except:
        return render(request,'delete_post.html',{'message': 'Bunday topshiriq mavjud emas'})

    if request.method == "POST":
        posts.delete()
        return redirect("/")


    return render(request, "delete_post.html", {'post': posts})

def edit_post(request, todo_id):
    try:
        posts = Post.objects.get(id=todo_id)
    except:
        return render(request,'edit_post.html',{'message': 'Bunday topshiriq mavjud emas'})
    
    if request.method == "POST":
        posts.title = request.POST.get('title')
        posts.desc = request.POST.get('desc')
        posts.status = request.POST.get('status')
        posts.save()
        return redirect("/")
    
    return render(request,"edit_post.html", {"post": posts})

def detail_post(request, todo_id):
    try:
        posts = Post.objects.get(id=todo_id)
    except:
        return render(request,'detail_post.html',{'message': 'Bunday topshiriq mavjud emas'})
    

    return render(request,'detail_post.html', {"todo":posts})

def create_post(request):

    return render(request,'create_post.html')


