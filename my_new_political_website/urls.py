# political_website/urls.py
from django.contrib import admin
from django.urls import path, include
from my_new_combrate import views
#from .views import SignUpView

app_name = 'my_new_combrate'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),  # Ensure this URL pattern is present
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset_view, name='password_reset'),
    #path('signup/', SignUpView.as_view(), name='signup'),
    path('my_new_combrate/', include('my_new_combrate.urls', namespace='my_new_combrate')),  # Include app URLs
]
