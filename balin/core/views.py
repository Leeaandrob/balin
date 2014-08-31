# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    template_name = "core/dashboard.html"
