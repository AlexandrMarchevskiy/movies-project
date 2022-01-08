"""movie_category_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.all_cats, name='all_cats'),
    path('post/<int:post_id>/', views.detail, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),


    #Auth
    # path('signup/', views.signupuser,name='signupuser'),
    # path('logout/', views.logoutuser, name='logoutuser'),
    # path('login/', views.loginuser, name='loginuser'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)