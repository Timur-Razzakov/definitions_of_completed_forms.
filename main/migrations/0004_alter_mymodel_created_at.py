# Generated by Django 4.1.5 on 2023-01-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_mymodel_created_at_alter_mymodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='created_at',
            field=models.DateField(blank=True, help_text='Укажите дату в формате "DD.MM.YYYY или YYYY-MM-DD" ', null=True, verbose_name='Дата создания'),
        ),
    ]
