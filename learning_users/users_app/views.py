from django.shortcuts import render
from users_app.forms import UserForm, UserProfileInfoForm

#imports for the login/logout part
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse #No longer useed in Django 2.0
from django.urls import reverse #use this instead of .core.urlresolvers import reverse


from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'users_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    """
        method for logging a users out
    """
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """
        method for registering a new user to the database
    """
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'users_app/registration.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered})



#Luser login definition

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACIVE')
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'users_app/user_login.html',{})
