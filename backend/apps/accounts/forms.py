from django import forms


from .models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.EmailField(
        label = "Электронная почта",
        widget=forms.EmailInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(
        label = "Пароль",
        widget=forms.PasswordInput(attrs={"class":"form-control"}),

    )

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone',
        ]
        widgets = {
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "middle_name":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
        }


