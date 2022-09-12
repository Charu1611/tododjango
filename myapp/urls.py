from django.contrib import admin
from django.urls import path,include
from . import views
from myapp.views import signout

urlpatterns = [
     path('',views.home,name="home"),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    # path('todo/',views.todo,name="todo"),
    path('add-todo/' , views.add_todo ), 
    path('signout/',signout,name="signout"),
    path('delete_todo/<int:id>' , views.delete_todo ), 
   path('change-status/<int:id>/<str:status>' , views.change_todo ), 
]


   
