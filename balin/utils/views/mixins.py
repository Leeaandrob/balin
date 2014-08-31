# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class SuccessDeleteMessageMixin(SuccessMessageMixin):

    """
    Mixin criado para propagar mensagem de sucesso em
    ações de exclusão.
    """

    def get_success_message(self):
        return self.success_message

    def delete(self, request, *args, **kwargs):
        success_message = self.get_success_message()
        if success_message:
            messages.success(request, success_message)
        return super(SuccessDeleteMessageMixin, self).delete(request,
                                                             *args, **kwargs)
