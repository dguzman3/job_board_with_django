from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models import fields
from .models import CustomUser


# Set up the form to edit Custom User by inheriting default UserChangeForm
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


# Set up the form to create Custom User by inheriting default UserCreationForm
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
