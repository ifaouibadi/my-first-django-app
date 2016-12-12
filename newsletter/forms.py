from django import forms

from newsletter.models import SignUp


class SignUpFrom(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # if not 'gmail' in email:
        #     raise forms.ValidationError('Please use a valid gmail email address')
        return email
