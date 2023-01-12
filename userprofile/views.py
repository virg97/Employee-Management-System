from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView
import random
from userprofile.forms import NewAccountForm
import string

class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'angajati/angajati_form.html'
    form_class = NewAccountForm

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%') for _ in range(8))

        if (user_instance := User.objects.filter(id=self.object.id)) and user_instance.exists():
            user_object = user_instance.first()
            user_object.set_password(psw)
            user_object.save()

            content = f"Buna ziua,\n Datele de autentificare sunt: \n username: {user_object.username}\n parola: {psw}"

            msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
            email = EmailMultiAlternatives(subject='Date contact platforma', body='content', from_email='contact@gmail.com', to=[user_object.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('angajati:lista_nume')

# Create your views here.
