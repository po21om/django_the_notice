from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# modele formularzy
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # wybrane pola do wypełnienia w fomularzu
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number',
                  'postal_code', 'town_name', 'password1', 'password2')


# formularz zmian - jeszcze nie zaimplementowane
# nie było w MVP - zaplanowane n aprzyszłość
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number',
                  'postal_code', 'town_name')
