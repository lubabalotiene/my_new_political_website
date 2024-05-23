# views.py
from .models import Person, Biography, PoliticalBeliefs, CommunityInvolvement
from django.shortcuts import render
from .models import RegistrationLink
from .models import LoginButton
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def home_view(request):
    return render(request, 'home.html')

def password_reset_view(request):
    return render(request, 'password_reset.html')

def home_view(request):
    RegistrationLink.url = RegistrationLink.objects.first()
    context = {
        'RegistrationLink.url': RegistrationLink.url
    }
    return render(request, 'home.html', context)

def about_view(request):
    person = Person.objects.first()
    biography = Biography.objects.first()
    political_beliefs = PoliticalBeliefs.objects.first()
    community_involvement = CommunityInvolvement.objects.first()
    
    context = {
        'person': person,
        'biography': biography,
        'political_beliefs': political_beliefs,
        'community_involvement': community_involvement
    }
    return render(request, 'about.html', context)

def login_view(request):
    login_button = LoginButton.objects.first()  # Assuming having only one login button
    context = {
        'login_button': login_button
    }
    return render(request, 'authentication/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page or another page after registration
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/signup.html'
    


