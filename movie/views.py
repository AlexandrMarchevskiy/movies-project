from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView

from .models import Movie, Category
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

menu = [
        # {'title': "Войти", 'url_name': 'loginuser'}
]

# def signupuser(request):
#     if request.method == 'GET':
#         return render(request, 'movie/signupuser.html', {'form': UserCreationForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('all_cats')
#             except IntegrityError:
#                 return render(request, 'movie/signupuser.html', {'form': UserCreationForm(), 'error': 'Имя уже используется. Пожалуйста , выберите новое имя.'})
#         else:
#             return render(request, 'movie/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают!'})
#

# def loginuser(request):
#     if request.method == 'GET':
#         return render(request, 'movie/loginuser.html', {'form': AuthenticationForm()})
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'movie/loginuser.html', {'form': AuthenticationForm(), 'error': 'Имя пользователя и пароль не совпадают!'})
#         else:
#             login(request, user)
#             return redirect('all_cats')

# @login_required
# def logoutuser(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('all_cats')



def all_cats(request):
    posts = Movie.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'movie/all_cats.html', context=context)



def detail(request, post_id):
    movie= get_object_or_404(Movie, pk=post_id)
    cats = Category.objects.all()
    context = {
        'movie': movie,
        'cats': cats,
        'menu': menu,
        'title': movie.title,
        'cat_selected': movie.cat_id,
    }
    return render(request, 'movie/detail.html',context=context)


def show_category(request, cat_id):
    posts = Movie.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'movie/all_cats.html', context=context)
