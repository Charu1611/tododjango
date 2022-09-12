from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser,logout
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import ToDoForm
from myapp.models import ToDo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



@login_required(login_url='signin')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=ToDoForm()
        todos=ToDo.objects.filter(user=user).order_by('priority')
        return render(request,'index.html',{'form': form,'todos' : todos,'name':request.user})

@login_required(login_url='signin')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else: 
            return render(request , 'index.html' , {'form' : form})

def signup(request):
    if request.method == 'POST':
        fm=UserCreationForm(request.POST or None)
        if fm.is_valid():
            messages.success(request,'Account created Successfully')
            user=fm.save()
            if user is not None:
                return redirect('/signin/')
    else:
        fm=UserCreationForm()
    return render(request,'signup.html',{'form':fm})

def signin(request):
        if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    loginUser(request, user)
                    messages.success(request,'Successfully logged in!')
                    return redirect('home')
        else:
            fm=AuthenticationForm()
        return render(request, 'signin.html',{'form':fm})
# def todo(request):
#     # profile page tbhi show kena h agar user authentictaed h
#     if request.user.is_authenticated:
#         return render(request, 'todo.html',{'name':request.user})
#     else:
#         return HttpResponseRedirect('/signin/')

def delete_todo(request,id):
    ToDo.objects.get(id=id).delete()
    return redirect('home')

def change_todo(request , id  , status):
    todo = ToDo.objects.get(id = id)
    todo.status = status
    todo.save()
    return redirect('home')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')