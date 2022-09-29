from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import FormView


# Create your views here.

class CustomLoginView(LoginView):
    pass


class RegisterView(FormView):
    pass

