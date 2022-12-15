from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views


from users.forms import SignupForm


class SignupView(FormView):

    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('registerok')

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):

    template_name = 'users/login.html'


class LogoutView(auth_views.LogoutView):

        template_name = 'home/index.html'

