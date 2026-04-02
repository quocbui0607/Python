from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class':'tieude'}),
            'content': forms.Textarea(attrs={'id':'noidung','class':'quocbui'})
        }

class SendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'quocbui', 'id':'noidung'}))
    cc = forms.BooleanField(required=False)