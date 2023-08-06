from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User

from django.conf import settings

ms_identity_web = settings.MS_IDENTITY_WEB


def home(request):
    return render(request, 'authenticate/home.html', {})


def login_user(request):
    # if request.method == 'POST':
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = authenticate(request, username=username, password=password)
    #     if user:
    #         login(request, user)
    #         messages.success(request, ('You have been logged In!'))
    #         return redirect('authenticate-home')
    #     else:
    #         messages.error(request, ('Error - Please Try Again...'))
    #         return redirect('authenticate-login')
    # else:
    #     return render(request, 'authenticate/login.html', {})
    # return redirect('sign_in')
    # if(request.user.is_authenticated):
    #     print(request.user.email)
    # else:
    #     print("No User Found")
    #     print("IS Authenticated By Azure", request.identity_context_data.authenticated)
    #     return redirect('sign_in')
    if(request.identity_context_data.authenticated or request.user.is_authenticated):
        print(f"The User is Authenticated By Azure : {request.identity_context_data.authenticated}" )
        print(f"The User is Authenticated By Django : {request.user.is_authenticated}" )
        if(request.user.is_authenticated):
            return redirect('authenticate-home')
        else:
            print(f'Username from Azure : {request.identity_context_data.username}')
            with transaction.atomic():
                user, created = User.objects.get_or_create(
                    username=request.identity_context_data.username,
                    defaults={
                        "first_name": request.identity_context_data.username.split()[0].capitalize(),
                        "last_name": '',
                        "email": request.identity_context_data._id_token_claims["preferred_username"],
                    }
                )
            login(request, user)
            return redirect('authenticate-home')
    else:
        return redirect('sign_in')

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged Out!'))
    return redirect('sign_out')
    return redirect('authenticate-home')
