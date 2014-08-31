# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

from braces.views import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"
