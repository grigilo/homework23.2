from django.forms import ModelForm, forms

from blogs.models import Blog, Release


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'image', 'is_published',)

    def clean_title(self):
        title = self.cleaned_data['title']
        list_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                      'бесплатно', 'обман', 'полиция', 'радар']
        for word in list_words:
            if word in title:
                raise forms.ValidationError(
                    'Заголовок не должен содержать слова: казино, '
                    'криптовалюта, крипта, биржа, дешево, бесплатно, '
                    'обман, полиция, радар')
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        list_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                      'бесплатно', 'обман', 'полиция', 'радар']
        for word in list_words:
            if word in content:
                raise forms.ValidationError(
                    'Содержимое не должно содержать слова: казино, '
                    'криптовалюта, крипта, биржа, дешево, бесплатно, '
                    'обман, полиция, радар')
        return content


class ReleaseForm(ModelForm):
    class Meta:
        model = Release
        fields = "__all__"
