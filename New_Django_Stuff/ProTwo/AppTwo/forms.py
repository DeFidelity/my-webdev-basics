from django import forms
from AppTwo.models import Users


class Formdel(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
