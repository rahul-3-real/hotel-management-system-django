from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Account


# Registration Form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Enter a valid email address."
    )
    name = forms.CharField(max_length=150, help_text="Required. Enter your full name.")

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "email",
            "name",
            "password1",
            "password2",
            Submit("submit", "Register", css_class="btn-success"),
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Account.objects.filter(username=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        user.name = self.cleaned_data["name"]
        if commit:
            user.save()
        return user

    class Meta:
        model = Account
        fields = ("email", "name", "password1", "password2")


# Login Form
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
