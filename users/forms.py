from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message
from django.forms import ModelForm

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]
        labels = {
            "first_name": "Name",
        }

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "placeholder": field.label})
    


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "placeholder": field.label})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "placeholder": field.label})
        
        
class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ["name", "email", "subject", "body"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        print(dir(self.fields["subject"]))
        print(self.fields["subject"].to_python)
        self.login_fields = [self.fields["subject"], self.fields["body"]]
        self.anon_fileds = [self.fields["name"], self.fields["email"], *self.login_fields]
        
        print(self.login_fields)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input", "placeholder": field.label})