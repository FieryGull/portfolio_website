from django.urls import path
from contact_form.views import ContactCreate, success
from .decorators import check_recaptcha

urlpatterns = [
    path('', check_recaptcha(ContactCreate.as_view()), name='contact_page'),
    path('success', success, name='success_page'),
]