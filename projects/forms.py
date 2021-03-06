from django.forms import ModelForm
from django import forms
from .models import Project
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["owner"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, filed in self.fields.items():
            filed.widget.attrs.update({"class": "input"})
    
