from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render
from django.conf import settings
from main.models import NavContent


class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["datanav"] = NavContent.objects.all()
        context["GOOGLE_RECAPTCHA_KEY"] = settings.GOOGLE_RECAPTCHA_KEY
        return context

    def form_valid(self, form):
        # Формируем сообщение для отправки
        if self.request.recaptcha_is_valid:
            data = form.data
            subject = f'Сообщение с формы от {data["first_name"]} {data["last_name"]} Почта отправителя: {data["email"]}'
            sender_email = f'{data["email"]}'
            email(subject, data['message'], sender_email)
            return super().form_valid(form)
        return render(self.request, "contact_form/contact_form.html", self.get_context_data())


# Функция отправки сообщения
def email(subject, content, sender_email):
    send_mail(subject,
              content,
              sender_email,
              [settings.EMAIL_HOST_USER]
              )


# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
    datanav = NavContent.objects.all()
    return render(request, "contact_form/success_page.html", {'datanav': datanav})
