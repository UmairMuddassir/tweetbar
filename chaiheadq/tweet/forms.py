from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control-custom',
                'rows': 4,
                'placeholder': "What's on your mind? (max 280 characters)",
                'maxlength': 280,
                'id': 'tweet-text-input',
            }),
            'photo': forms.FileInput(attrs={
                'class': 'file-input-custom',
                'accept': 'image/*',
                'id': 'tweet-photo-input',
            }),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control-custom',
            'placeholder': 'Enter your email address',
            'id': 'id_email',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control-custom',
                'placeholder': 'Choose a unique username',
                'id': 'id_username',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control-custom',
            'placeholder': 'Create a strong password',
            'id': 'id_password1',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control-custom',
            'placeholder': 'Confirm your password',
            'id': 'id_password2',
        })
        self.fields['email'].required = True