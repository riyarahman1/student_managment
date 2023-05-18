from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm


class HomePageView(View):
    template_name = "index.html"


class LoginView(View):
    form_class = LoginForm
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("index")
        return render(request, self.template_name, {"form": form})


class RegisterView(View):
    form_class = RegisterForm
    template_name = "registration/register.html"

    def get(self, request, *args, **kwargs):
        if request.method != "POST":
            form = self.form_class()
        else:
            form = self.form_class(request.POST)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")
