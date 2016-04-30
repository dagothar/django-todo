from django.views.generic import ListView
from django.shortcuts import render
import datetime

from .. import models


class DayView(ListView):
    """
    Single day view.
    """
    model = models.Task
    template_name = 'todo/day_view.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        date = datetime.date(
            int(self.kwargs['year']),
            int(self.kwargs['month']),
            int(self.kwargs['day'])
        )
        return models.Task.objects.filter(date__exact=date)
