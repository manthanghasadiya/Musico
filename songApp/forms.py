from django import forms
from .models import userInfo, Song
from django.contrib.auth.models import User


class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['email', 'username', 'password']


class userInfoForm(forms.ModelForm):
    class Meta():
        model = userInfo
        fields = ['mobile_number']


class songForm(forms.ModelForm):
    class Meta():
        model = Song
        fields = ['user', 'audio_name',
                  'audio_file', 'audio_type', 'thumbnail']
