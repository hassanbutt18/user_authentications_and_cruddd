from django.contrib.auth import forms
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, MyAuthenticationForm, DashboardForm, EditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.paginator import Paginator


# Create your views here.

def register(request):
    """
    This function register the user
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def user_login(request):
    """
    This function is for user login
    """
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = MyAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = MyAuthenticationForm()
        context = {'form': form}
        return render(request, 'user_login.html', context)
    else:
        return redirect('profile')


def Logout(request):
    logout(request)
    return redirect('user_login')


def profile(request):
    """
    This function is to render to the home page
    """
    if request.user.is_authenticated:
        user = request.user.user_Img.url
        name = request.user.email
        return render(request, 'profile.html', {'user': user, 'name': name})
    else:
        return redirect('user_login')


def create_list(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST, request.FILES)
        if form.is_valid():
            nick_name = form.cleaned_data['nick_name']
            work_description = form.cleaned_data['work_description']
            Family_detail = form.cleaned_data['Family_detail']
            user_Img = form.cleaned_data['user_Img']
            profile = Profile.objects.create(nick_name=nick_name, work_description=work_description,
                                             Family_detail=Family_detail, user_Img=user_Img, user=request.user)
            return redirect('view_list')


    else:
        form = DashboardForm()
    return render(request, "create_list.html", {'form': form})


def view_list(request):
    data = Profile.objects.filter(user=request.user.id)
    context = {'data': data}
    return render(request, 'reterive_data.html', context)


def delete_list(request, id):
    data = Profile.objects.get(id=id)
    data.delete()
    # context = {'data': data2}
    return redirect('view_list')
    # return render(request, 'reterive_data.html', context)


def edit_list(request, id):
    obj = Profile.objects.get(id=id)
    form = EditForm(request.POST, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('view_list')
    else:
        form = EditForm(instance=obj)
    context = {'form': form}

    return render(request, "editlist.html", context)


def search_item(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('Family_detail', None)
        if query_name:
            results = Profile.objects.filter(
                Q(Family_detail__contains=query_name) | Q(work_description__contains=query_name) | Q(
                    user_Img__contains=query_name) | Q(nick_name__contains=query_name), user=request.user.id, )
            return render(request, 'reterive_data.html', {"results": results})

    return render(request, 'reterive_data.html')
