
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('dairy/', views.dairy_view, name='dairy'),

]
