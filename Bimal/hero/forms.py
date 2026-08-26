from django import forms

from .models import Admission, Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = [
            "full_name",
            "email",
            "phone",
            "payment_method",
            "transaction_id",
            "payment_screenshot",
        ]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Full Name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                }
            ),
            "payment_method": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "transaction_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Transaction ID",
                }
            ),
            "payment_screenshot": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = [
            "name",
            "email",
            "phone",
            "address",
            "education",
            "gender",
            "course",
            "mode",
            "duration",
            "preferred_session",
            "preferred_time",
            "admission_date",
            "message",
        ]