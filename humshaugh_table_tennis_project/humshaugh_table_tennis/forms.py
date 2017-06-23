from django import forms
from humshaugh_table_tennis.models import News

class NewsForm(forms.ModelForm):
    title = forms.CharField(max_length=News.MAX_TITLE_LENGTH, help_text="Header")
    content = forms.CharField(max_length=News.MAX_CONTENT_LENGTH, help_text="Content")

    class Meta:
        model = News
        fields = ('title', 'content')
