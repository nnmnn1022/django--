from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        exclude = []
        fields = ['email',
                  'name',
                  'profile_image',
                  'gmail',
                  'l10n'
                  ]
