from django.contrib.auth.forms import forms, UserCreationForm, UserChangeForm
from django import forms
from storemain.models import User

class CreateProfileForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        email = forms.EmailField()
        fields = ('email','first_name','last_name' )
        widgets = {
                'first_name':forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
                'last_name':forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
                'email':forms.EmailInput(attrs={'class':'form-control', 'required':'required'}),
                'password1':forms.PasswordInput(attrs={'class':'form-control'}),
                'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            }
            
class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('email','first_name','last_name')
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            }