from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    if request.method == "POST": # checking if it's a post request
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = request.POST['username'], password = request.POST['password'])
            if user is not None:
                if user.is_active: # checking if the user is still active
                    login(request, user) # logging the user in
                    request.session.set_expiry(1800) # setting the session expiry time, after which login is required
                    return HttpResponseRedirect(reverse('ACMS:homepage'))
            else:
                messages.error(request, 'Incorrect username and password!!!') # saving message error to be displayed on template
                return HttpResponseRedirect(reverse('ACMS:index'))


    else:
        form = LoginForm() # creating new form
        if request.path == "/acms/login/":
            messages.info(request, "Please log in");
        logout(request) # logging out the user and clearing the user's session

    return render(request, 'acms/index.html', {"form": form})

@login_required(redirect_field_name="", login_url='/acms/login') # login required to view this page
def homepage(request):
    context = {"name" : "%s %s" % (request.user.last_name, request.user.first_name), "username" : request.user.username}
    return render(request, 'acms/homepage.html', context)







