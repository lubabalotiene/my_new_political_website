# views.py
from .models import Person, Biography, PoliticalBeliefs, CommunityInvolvement
from django.shortcuts import render, redirect
from .models import RegistrationLink, LoginButton
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic

def about_view(request):
    """
    View function to render the 'about' page.

    Retrieves information about a person, their biography, political beliefs,
    and community involvement from the database and passes it to the template.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template 'about.html' with context.
    """
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
    """
    View function to render the login page.

    Retrieves the login button information from the database and passes it to the template.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template 'authentication/login.html' with context.
    """
    login_button = LoginButton.objects.first()
    context = {
        'login_button': login_button
    }
    return render(request, 'authentication/login.html', context)

def register(request):
    """
    View function to handle user registration.

    Renders the registration form and processes form submission. Upon successful registration,
    logs the user in and redirects them to the home page.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template 'authentication/register.html' with context.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

@login_required
def about(request):
    """
    View function to render the 'about' page for authenticated users.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template 'about.html'.
    """
    return render(request, 'about.html')

@login_required
def contact(request):
    """
    View function to render the 'contact' page for authenticated users.

    Args:
        request: HTTP request object.

    Returns:
        Rendered template 'contact.html'.
    """
    return render(request, 'contact.html')

class SignUpView(generic.CreateView):
    """
    Class-based view for user registration.

    Renders the registration form and handles form submission.
    Upon successful registration, redirects the user to the login page.

    Attributes:
        form_class (Form): The form class to use for user registration.
        success_url (str): URL to redirect to after successful registration.
        template_name (str): Name of the template for rendering the registration form.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/signup.html'
