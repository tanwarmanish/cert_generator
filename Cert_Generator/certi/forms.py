from django import forms
from django.contrib.auth.models import User
from . import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password',)
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.ProjectData
        fields = ('project_id',"project_name","template","data")

class ProjectStatusForm(forms.ModelForm):
    class Meta:
        model = models.ProjectStatus
        fields='__all__'

