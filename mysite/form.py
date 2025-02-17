
from django import forms
 
class Userform(forms.Form):
    name=forms.CharField( label='Enter your name',max_length=100,required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    fname=forms.CharField(label='Enter your fname',max_length=100,required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    