from django import forms

class Contact_Form(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={ "class" : "form-control" , "placeholder" : "Your Name"}))
    emailid = forms.EmailField(widget=forms.EmailInput(attrs={ "class" : "form-control" , "placeholder" : "Your Email Id"}))
    content = forms.CharField(widget=forms.Textarea(attrs={ "class" : "form-control" , "placeholder" : "Your Content"}))
