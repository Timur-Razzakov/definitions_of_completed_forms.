from django import forms

from .models import MyModel


class Search_Form(forms.ModelForm):
    created_at = forms.DateField(label='Дата',
                                 input_formats=['%d.%m.%Y', '%Y.%m.%d'],
                                 widget=forms.DateInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Введите номер телефона ',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(label='Введите email',
                                  widget=forms.EmailInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Введите какой-то текст',
                           widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = MyModel
        fields = ('created_at', 'phone_number', 'user_email', 'text')


class AddForm(forms.ModelForm):
    created_at = forms.DateField(label='Дата',
                                 input_formats=['%d.%m.%Y', '%Y.%m.%d'],
                                 widget=forms.DateInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Введите номер телефона ',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(label='Введите email',
                                  widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Введите наименование формы ',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Введите какой-то текст',
                           widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = MyModel
        fields = ('created_at', 'phone_number', 'user_email', 'name', 'text')
