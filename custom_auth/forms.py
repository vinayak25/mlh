from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=255, required=True)

    class Meta:
        widgets = {
            "password" : forms.PasswordInput()
        }
