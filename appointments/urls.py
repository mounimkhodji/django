from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'appointments'  # Add this line

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='appointments/login.html'), name='login'),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('booking/', views.booking, name='booking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    from django.urls import path
from . import views

app_name = 'appointments'  # Add this line

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('booking/', views.booking, name='booking'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)