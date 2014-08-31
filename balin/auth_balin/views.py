# -*- coding: utf-8 -*-

from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from eztables.views import DatatablesView

from balin.auth_balin.forms import CreateUserForm, ChangeUserForm
from balin.utils.views.mixins import SuccessDeleteMessageMixin


class UserListView(ListView):
    model = User
    template_name = "auth_balin/user_list.html"


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    template_name = "auth_balin/user_form.html"
    success_message = _("User %(first_name)s %(last_name)s was "
                        "created successfully")
    success_url = reverse_lazy('auth_balin:list')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = ChangeUserForm
    template_name = "auth_balin/user_update.html"
    success_message = _("User %(first_name)s %(last_name)s was "
                        "updated successfully")
    success_url = reverse_lazy('auth_balin:list')


class UserDeleteView(SuccessDeleteMessageMixin, DeleteView):
    model = User
    template_name = "auth_balin/user_confirm_delete.html"
    success_message = _("User was removed successfully")
    success_url = reverse_lazy('auth_balin:list')
