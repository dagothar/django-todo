from django.views.generic import TemplateView


class RegisterView(TemplateView):
    template_name = 'todo/register.html'
