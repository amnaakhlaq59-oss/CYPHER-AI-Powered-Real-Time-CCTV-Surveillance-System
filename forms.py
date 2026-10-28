from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # Add an email field, which is not in the default form
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email') # Add 'email' to the fields

    def save(self, commit=True):
        # Save the user instance
        user = super(CustomUserCreationForm, self).save(commit=False)
        # Save the email
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user