from django.urls import path
from . import views

# app_name = "user_auth"
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('accounts/register/', views.register_user, name='register'),
    # path('profile_settings/', views.user_detail, name='user_detail')
]