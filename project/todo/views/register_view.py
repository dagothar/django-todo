from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy


class RegisterView(FormView):
    """
    Handles User registration.
    """
    template_name = 'todo/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_success')

    def form_valid(self, form):
        """Adds the new user."""
        new_user = form.save()
        return super(FormView, self).form_valid(form)
