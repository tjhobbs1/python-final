from django.views.generic import TemplateView


class dashboardView(TemplateView):
    template_name = 'home.html'