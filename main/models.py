from django.core.validators import RegexValidator
from django.db import models


class MyModel(models.Model):
    phone_number_validator = RegexValidator(
        regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        message="""Телефон передается в стандартном формате 
                                           +7|7|8 xxx xxx xx xx (X - от 0 до 10)""")
    email_validator = RegexValidator(
        regex=r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$",
        message="Почта неверного формата")
    created_at = models.DateField(verbose_name='Дата создания',
                                  help_text='Укажите дату в формате "DD.MM.YYYY или YYYY-MM-DD" ', blank=True,
                                  null=True)
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=13, validators=[phone_number_validator], blank=True, null=True)

    email = models.CharField(max_length=255,
                             verbose_name='Почта', validators=[email_validator], blank=True, null=True)
    name = models.CharField(verbose_name='Наименование',
                            max_length=255, blank=True, null=True)

    text = models.TextField(verbose_name='Текст', blank=True, null=True)

    def __str__(self):
        return self.name
