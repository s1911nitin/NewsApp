from django import forms
from .models import Post

class MultiplePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","desc","post_image"]
        labels = {
            "title":"Title",
            "desc":"Description",
            "post_image":"Image"
        }
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "desc":forms.Textarea(attrs={"class":"form-control"}),
            "post_image":forms.ClearableFileInput(attrs={"class":"form-control"})
        }
