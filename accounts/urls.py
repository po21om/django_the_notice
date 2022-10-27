from django.urls import path
from .views import CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView

# url do widoków - login i i register imortowane z naszych views
urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    # czysty import django
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
