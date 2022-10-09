from django.contrib.auth import login, get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView


# Create your views here.
User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "viewer/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    # def get_success_url(self) -> str:
    #     if 'next':
    #         return redirect('next')
    #     return reverse_lazy("own_notices")


class RegisterView(FormView):
    template_name = "viewer/register.html"
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("own_notices")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *arg, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("own_notices")
        return super(RegisterView, self).get(*arg, **kwargs)
