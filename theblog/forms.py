from django import forms
from .models import Post, Category, Comment


# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name')

choices_list = []
for item in choices:
    choices_list.append(item)


class PostForm (forms.ModelForm):
      class Meta:
          model = Post
          fields = ('title', 'title_tag', 'author', 'category', 'body')

          widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Type title'}),
                'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control','id':'elder','type':'hidden'}),
                # 'author': forms.Select(attrs={'class': 'form-control'}),
                'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'}),
          }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is title placeholder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }