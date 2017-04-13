from django.shortcuts import render, redirect

from contacts.models import Contact
from contacts.models import City
from contacts.models import State

from contacts.forms import ContactCreateForm
from contacts.forms import CityCreateForm
from contacts.forms import StateCreateForm


def index(request):
    template_name = 'contacts/index.html'
    return render(request, template_name)


def contact_list(request):
    contact_list = Contact.objects.all()
    template_name = 'contacts/contact_list.html'
    context = {'contact_list': contact_list}
    return render(request, template_name, context)


def city_list(request):
    city_list = City.objects.all()
    template_name = 'contacts/city_list.html'
    context = {'city_list': city_list}
    return render(request, template_name, context)


def state_list(request):
    state_list = State.objects.all()
    template_name = 'contacts/state_list.html'
    context = {'state_list': state_list}
    return render(request, template_name, context)


def contact_create(request):
    action = '/contact_create/'
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = ContactCreateForm()
    template_name = 'contacts/form.html'
    context = {'form': form, 'action': action}
    return render(request, template_name, context)

 
def city_create(request):
    action = '/city_create/'
    if request.method == 'POST':
        form = CityCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CityCreateForm()
    template_name = 'contacts/form.html'
    context = {'form': form, 'action': action}
    return render(request, template_name, context)


def state_create(request):
    action = '/state_create/'
    if request.method == 'POST':
        form = StateCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = StateCreateForm()
    template_name = 'contacts/form.html'
    context = {'form': form, 'action': action}
    return render(request, template_name, context)
 
