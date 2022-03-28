from django import forms
from users.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = [
            "employee_reg_no",
            "employee_name",
            "employee_email",
            "employee_mobile",
            "created_at"
        ]
