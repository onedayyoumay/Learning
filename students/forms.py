from django import forms
from models import Student, Group
from django.forms import ModelForm
class AuthForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

class Add_group(ModelForm):
    class Meta:
        model = Group
        fields = ('group_number', 'group_head')

class Add_student(ModelForm):
    class Meta:
        model = Student
        fields = ('full_name', 'photography', 'b_date', 'ticket_number', 'group_id')