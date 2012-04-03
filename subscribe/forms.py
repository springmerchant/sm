from django import forms
from bootstrap2.forms import BootstrapForm, Fieldset

class ApiForm(BootstrapForm):
    class Meta:
        layout = (Fieldset("Enter Your Email Address", "email", "first_name"),)

    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name",max_length=256)


