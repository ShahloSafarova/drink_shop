from django.urls import path
from .views import UserRegisterView, CustomUserLogin, LogoutView, homepage_view, profile_view, UpdateProfileView

urlpatterns = [
    path('', homepage_view, name='home'),
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/', CustomUserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', homepage_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('update/profile/', UpdateProfileView.as_view(), name='update'),
]
