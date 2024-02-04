from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import CustomerCreateForm, UpdateProfileForm  # Corrected import
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def homepage_view(request):
    return render(request, 'home.html')

def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context=context)

class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UpdateProfileForm(instance=request.user)
        context = {"form": form}
        return render(request, "users/editprofile.html", context)

    def post(self, request):
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
            context = {"form": form}
            return render(request, "users/editprofile.html", context)


class UserRegisterView(View):
    def get(self, request):
        create_form = CustomerCreateForm()
        context = {
            'form': create_form
        }
        return render(request, template_name='registration/signup.html', context=context)

    def post(self, request):
        create_form = CustomerCreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('login')
        else:
            context = {
                'form': create_form
            }
            return render(request, template_name='registration/signup.html', context=context)

class CustomUserLogin(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(request, template_name='registration/login.html', context=context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, template_name='registration/login.html', context=context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
