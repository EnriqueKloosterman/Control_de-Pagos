from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .forms import LoginForm



urlpatterns = [
    path('', views.home, name='home'),
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/add/', views.add_payment, name='add_payment'),
    path('payments/edit/<int:payment_id>/', views.edit_payment, name='edit_payment'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('payment/boleta', views.new_boleta, name='new_boleta')
]