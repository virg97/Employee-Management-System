from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from angajati import models
Angajati = models.Angajati


class AngajatiView(LoginRequiredMixin, ListView):
    model = Angajati
    template_name = 'angajati/angajati_index.html'


class CreateAngajatiView(LoginRequiredMixin, CreateView):
    model = Angajati
    fields = ['name', 'country', 'firma', 'link']
    template_name = 'angajati/angajati_form.html'

    def get_success_url(self):
        return reverse('angajati:lista_nume')

class UpdateAngajatiView(LoginRequiredMixin, UpdateView):
    model = Angajati
    fields =['name', 'country', 'firma', 'link']
    template_name = 'angajati/angajati_form.html'

    def get_success_url(self):
        return reverse('angajati:lista_nume')


@login_required
def delete_angajati(request, pk):

    Angajati.objects.filter(id=pk).update(active=0)
    return redirect('angajati:lista_nume')


@login_required
def activate_angajati(request, pk):
    Angajati.objects.filter(id=pk).update(active=1)
    return redirect('angajati:lista_nume')

