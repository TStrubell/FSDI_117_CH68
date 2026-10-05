from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    first_name = forms.CharField(
        max_length=50,
        label=_("First Name"),
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=50,
        label=_("Last Name"),
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    confirm_email = forms.EmailField(
        label=_("Confirm Email"),
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    subject = forms.CharField(
        max_length=150,
        label=_("Subject"),
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    message = forms.CharField(
        label=_("Comments"),
        max_length=600,  # character limit
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 6,
            "placeholder": _("Enter your message (max 600 characters)"),
            "id": "sgng-message-box"
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            self.add_error("confirm_email", _("Email addresses must match."))
