from django import forms
from .models import Post , Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField






class PostForm(forms.ModelForm):
  # content = SummernoteTextField()
  content = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

  class Meta:
    model = Post
    # fields = '__all__'
    exclude = ('author',)
    # widgets = {
    #         'content': SummernoteWidget(),
    #         'content': SummernoteInplaceWidget(),
    #     }


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment',]