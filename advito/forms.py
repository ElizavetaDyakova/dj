from django import forms
from django.core.exceptions import ValidationError

from advito.models import Add, Comment, Category


class CatForm(forms.ModelForm):
    class Meta:
        # Указываем модель
        model = Category
        # Указываем поля из модели
        fields = ['name']
        labels = {
            'name': 'Название категории',
        }
        # Можем переопределить виджеты
        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Название категории'}),
        }


class PostForm(forms.ModelForm):
    max_size_img = 5
    # Можно задать  поле и таким образом, если форма. например, не для модели.
    # image = forms.ImageField(label=_('Change photo'), required=False, error_messages={'invalid': _
    # ("Image files only")}, widget=FileInput)

    class Meta:
        # Указываем модель
        model = Add
        # Указываем поля из модели
        fields = ['header', 'description', 'category', 'image']
        labels = {
            'header': 'Название объявления',
            'description': 'Описание объявления',
            'category': 'Категория объявления',
            'image': 'Выберите файл',
        }
        # Можем переопределить виджеты
        widgets = {
            'header': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Название объявления'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание объявления'}),
            'image': forms.ClearableFileInput(attrs={'type': "file", 'class': "form-control-file"})
        }

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > self.max_size_img*1024*1024:
                raise ValidationError("Файл должен быть не больше {0} мб".format(self.max_size_img))
            return image
        else:
            raise ValidationError("Не удалось прочитать файл")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст комментария'})
        }
