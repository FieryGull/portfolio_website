from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact
from django.utils.translation import ugettext_lazy as _


class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['first_name', 'last_name', 'email', 'message']
        labels = {'first_name': _('Имя'), 'last_name': _('Фамилия'),'email': _('Почта'), 'message': _('Сообщение')}
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': _('Напишите тут ваше сообщение')
                }
            )
        }