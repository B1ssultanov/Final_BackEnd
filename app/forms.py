from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from app.models import Products, Categories
from app.validators.password_validators import validate_password_strength


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        validate_password_strength(password)
        return password

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = 'Confirm Password'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class LoggingForm(AuthenticationForm):
#     log_username = forms.CharField(max_length=150, required=True)
#     log_password = forms.CharField(widget=forms.PasswordInput, required=True)

class UploadForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'manufacturer', 'name', 'price', 'characteristics', 'image', 'url']

    category = forms.ModelChoiceField(queryset=Categories.objects.all(), label='Category')
    manufacturer = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    characteristics = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    url = forms.URLField()


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
