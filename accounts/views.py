from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from . forms import UserForm, ProfileForm
from . models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           
           user = authenticate(username=username, password=password)
           login(request, user)
           
        return redirect("/products")
           
           
    else :
        form = UserCreationForm()
        
    context= { 'form':form }
    
    return render(request, "registration/signup.html", context)
        
   
        
@login_required(redirect_field_name='my_redirect_field')    
def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    
    context = {'profile': profile}
    return render (request, 'registration/profile.html', context)