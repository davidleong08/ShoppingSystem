from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from apps.users.forms import UserRegForm
from apps.users.models import MyUser
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def user_register(request):
    if request.method == "GET":
        form_obj = UserRegForm()
        return render(request, 'user_register.html', {'form_obj': form_obj})
    if request.method == "POST":
        form_obj = UserRegForm(request.POST, request.FILES)
        if form_obj.is_valid():
            uname = request.POST.get("username", '')
            users = MyUser.objects.filter(username=uname)
            email = request.POST.get("email", '')
            if users:
                info = 'the user has been existed'
                return render(request, 'user_register.html', {"form_obj": form_obj, "info": info})
            else:
                form_obj.cleaned_data["username"] = uname
                form_obj.cleaned_data["email"] = email
                form_obj.cleaned_data.pop("re_password")
                form_obj.cleaned_data["is_staff"] = 1
                form_obj.cleaned_data["is_superuser"] = 0
                # new user
                user = MyUser.objects.create_user(**form_obj.cleaned_data)
                info = 'register successful, please login'
                return render(request, 'user_register.html', {"form_obj": form_obj, "info": info})
        else:
            errors = form_obj.errors
            print(errors)
            return render(request, "user_register.html", {'form_obj': form_obj, 'errors': errors})


def user_login(request):
    return render(request, "user_login.html")


def ajax_login_data(request):
    uname = request.POST.get("username", '')
    pwd = request.POST.get("password", '')
    json_dict = {}
    if uname and pwd:
        if MyUser.objects.filter(username=uname):
            user = authenticate(username=uname, password=pwd)
            if user:
                if user.is_active:
                    login(request, user)
                    json_dict["code"] = 1000
                    json_dict["msg"] = "login successful"
                else:
                    json_dict["code"] = 1001
                    json_dict["msg"] = "the user doesn't active"
            else:
                json_dict["code"] = 1002
                json_dict["msg"] = "the password is wrong, please try again"
        else:
            json_dict["code"] = 1003
            json_dict["msg"] = "the username is wrong, please try again"
    else:
        json_dict["code"] = 1004
        json_dict["msg"] = "the username or password is empty"
    return JsonResponse(json_dict)


def user_logout(request):
    if request.user.is_authenticated:
        return render(request, "user_logout.html")
    else:
        return redirect('login')


def ajax_logout_data(request):
    json_dict = {}
    logout(request)
    json_dict["code"] = 1000
    json_dict["msg"] = "logout successful"
    return JsonResponse(json_dict)
