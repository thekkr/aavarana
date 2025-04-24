from django import forms
from .models import Post, PostCategory

choices = PostCategory.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    # body = MarkdownxFormField(widget=MarkdownxWidget())
    class Meta:
        model = Post
        fields = ("title",'title_tag','author','category','body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Title of the Post Here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }

class PostUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title",'title_tag','body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Title of the Post Here'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class PostCategoryForm(forms.ModelForm):
    
    class Meta:
        model = PostCategory
        fields = ("name",)
        
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()

