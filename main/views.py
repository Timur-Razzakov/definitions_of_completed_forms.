from django.http import JsonResponse
from django.shortcuts import render

from .forms import AddForm, Search_Form
from .models import MyModel


def check_form_view(request):
    """Сравниваем приходящие данные с существующей формой """
    form = Search_Form(request.POST or None)
    result = {}
    if form.is_valid():
        get_data = form.cleaned_data
        my_form = MyModel.objects.filter(
            created_at=get_data['created_at'],
            phone_number=get_data['phone_number'],
            email=get_data['user_email'],
            text=get_data['text'],
        ).values('name')
        for item in my_form:
            result['Form name'] = item['name']
        if not my_form.exists():
            result['date'] = 'datetime'
            result['phone_number'] = 'str'
            result['email'] = 'str'
            result['text'] = 'str'
        return JsonResponse(result)
    return render(request, 'home.html', {'form': form, 'result': result})


def add_form_view(request):
    """Добавляем новые формы """
    form = AddForm(request.POST or None)
    if form.is_valid():
        new_form = form.save()
        data = form.cleaned_data
        new_form.created_at = data['created_at']
        new_form.phone_number = data['phone_number']
        new_form.email = data['user_email']
        new_form.name = data['name']
        new_form.text = data['text']
        new_form.save()
        return render(request, 'add_forms.html', {'new_form': new_form})
    return render(request, 'home.html', {'form': form})
