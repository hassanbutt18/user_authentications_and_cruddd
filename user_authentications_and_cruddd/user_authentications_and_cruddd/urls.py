"""User_authentications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mysite.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('profile/', profile, name='profile'),
    path('logout/', Logout, name='logout'),
    path('create/', create_list, name='create_list'),
    path('view_list/', view_list, name='view_list'),
    path('list/edit/<int:id>/', edit_list, name='edit_list'),
    path('list/delete/<int:id>/', delete_list, name='delete_list'),
    path('search/' ,search_item, name='search_item')
    # path('edit/(?P<pid>[0-9]+)', edit, name='edit'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
