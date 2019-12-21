from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home/index.html'


class Dashboard(TemplateView):
    template_name = 'home/dashboard.html'


class Faq(TemplateView):
    template_name = 'home/faq.html'
