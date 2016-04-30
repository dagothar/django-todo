from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from .. import models


class DayView(LoginRequiredMixin, FormMixin, ListView):
    """
    Single day view.

    Context:
        tasks: A list of Tasks.
        date: The current date.
        prev_date: The previous day.
        next_date: The next day.
    """
    model = models.Task
    template_name = 'todo/day_view.html'
    context_object_name = 'tasks'

    def get_date(self):
        """
        Constructs date from the view url parameters.

        Returns:
            date: Date object constructed from the url path, e.g.:
                todo/2016/04/30 yields 2016-04-30 date.
        """
        return datetime.date(
            int(self.kwargs['year']),
            int(self.kwargs['month']),
            int(self.kwargs['day'])
        )

    def get_queryset(self):
        """Returns a list of tasks of the logged in user for a given day."""
        return models.Task.objects.filter(
            user__exact=self.request.user,
            date__exact=self.get_date()
        )

    def get_context_data(self, **kwargs):
        """Adds day view context objects."""
        context = super(ListView, self).get_context_data(**kwargs)
        date = self.get_date()
        context['date'] = date
        context['prev_date'] = date - datetime.timedelta(days=1)
        context['next_date'] = date + datetime.timedelta(days=1)
        return context
