from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Records, RecordsEyebrows, RecordsEyelashes
from django.contrib.auth.models import User
import datetime
from django.db import models
from .models import Records
from django.forms import ModelForm

TIME_CHOISES = [datetime.time(8,0), datetime.time(8,30), datetime.time(9,0), datetime.time(9,30), datetime.time(10,0),
                datetime.time(10,30), datetime.time(11,0), datetime.time(11,30), datetime.time(12,0), datetime.time(12,30),
                datetime.time(13,0), datetime.time(13,30), datetime.time(14,0), datetime.time(14,30), datetime.time(15,0),
                datetime.time(15,30), datetime.time(16,0), datetime.time(16,30), datetime.time(17,0), datetime.time(17,30),
                datetime.time(18,0)]


def get_masters():
    users = User.objects.all()
    master_usernames = []
    for user in users:
        if (len(user.groups.all()) > 0) and (user.groups.all()[0].name == 'master'):
            master_usernames.append(user.username)
    return master_usernames


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.CharField(help_text="Enter 'master' or 'client'")
    username = forms.CharField()

    field_order = ['username', 'email', 'password1', 'password2']


class MakeRecordForm(ModelForm):
    time = forms.ChoiceField(required=False, choices=[(time, time) for time in TIME_CHOISES])
    master = forms.ChoiceField(required=False, choices=[(master, master) for master in get_masters()])
    client = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Records
        fields = ['time', 'master', 'client']


class MakeRecordEyebrowsForm(ModelForm):
    time = forms.ChoiceField(required=False, choices=[(time, time) for time in TIME_CHOISES])
    master = forms.ChoiceField(required=False, choices=[(master, master) for master in get_masters()])
    client = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = RecordsEyebrows
        fields = ['time', 'master', 'client']


class MakeRecordEyelashesForm(ModelForm):
    time = forms.ChoiceField(required=False, choices=[(time, time) for time in TIME_CHOISES])
    master = forms.ChoiceField(required=False, choices=[(master, master) for master in get_masters()])
    client = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = RecordsEyelashes
        fields = ['time', 'master', 'client']
