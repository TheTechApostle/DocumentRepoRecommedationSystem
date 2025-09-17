from django import  forms  
from .models import *
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class forgetpassword(forms.Form):
    email = forms.CharField(max_length=100)



class UserDetail(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"


class DocRepo(forms.ModelForm):
    class Meta:
        fields = "__all__"


class Todos(forms.ModelForm):
    class Meta:
        fields = "__all__"

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting_Schedule
        fields = ['title', 'date', 'start_time', 'finish_time', 'agenda', 'attendees']
        widgets = {
            'attendees': forms.CheckboxSelectMultiple(),  # For multiple selections
        }



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'group']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('A user with this email already exists.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            user.groups.add(self.cleaned_data['group'])
        return user
    
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']


class formatDocumentForm(forms.ModelForm):
    class Meta:
        model = formatDocument
        fields  = ['fontSize','fontColor','fontFamily', 'letterSpacing']