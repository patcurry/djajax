from django.forms import ModelForm

from contacts.models import Contact
from contacts.models import City
from contacts.models import State


class ContactCreateForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['user', 'first_name',
                  'last_name', 'phone',
                  'email', 'city']


class CityCreateForm(ModelForm):

    class Meta:
        model = City
        fields =['city', 'state']


class StateCreateForm(ModelForm):

    class Meta:
        model = State
        fields = ['state']
