from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["owner", "tags"]
        widgets = {
            'tags': forms.CheckboxSelectMultiple
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, filed in self.fields.items():
            filed.widget.attrs.update({"class": "input"})
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["value", "body"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})