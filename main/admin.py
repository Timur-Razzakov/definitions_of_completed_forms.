from django.contrib import admin

from .models import MyModel


# from django.conf.locale.es import formats as es_formats
#
# es_formats.DATETIME_FORMAT = ['%d.%m.%Y', '%Y.%m.%d']

#
# class MyModelAdmin(admin.ModelAdmin):
#     # input_formats = ['%d.%m.%Y', '%Y.%m.%d'],
#
#     def create_time_display(self, obj):
#         return obj.created_at.strftime('%Y.%m.%d'),
#
#     create_time_display.admin_order_field = 'created_at'
#     list_display = ('name', 'email', 'create_time_display', 'phone_number', 'text')


# Register your models here.
admin.site.register(MyModel, )
