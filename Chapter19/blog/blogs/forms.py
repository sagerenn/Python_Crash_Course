from django.forms import ModelForm
from blogs.models import BlogPost

class PostForm(ModelForm):
    """define the post form """

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'text',
        ]