from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomCreationForm(UserCreationForm):
    
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "placeholder": field.label})
    
    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
        labels = {
            "first_name": "Name",
        }