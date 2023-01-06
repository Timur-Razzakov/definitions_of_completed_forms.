from django import forms
from icecream import ic
import re
import time

from .models import MyModel


#

class My_Form(forms.ModelForm):
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

    # def clean_email(self):
    #     pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    #     get_email = self.cleaned_data.get('email')
    #     if bool(re.match(pattern, get_email)) is False:
    #         raise forms.ValidationError("Почта неверного формата")
    #     return super(My_Form, self)

    # def clean_phone_number(self):
    #     pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    #     get_phone_number = self.cleaned_data.get('phone_number')
    #     if re.match(pattern, get_phone_number) is None:
    #         raise forms.ValidationError("""Телефон передается в стандартном формате
    #                                        +7|7|8 xxx xxx xx xx (X - от 0 до 10)""")
    #     return super(My_Form, self)
