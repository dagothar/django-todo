from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
import datetime

from ..util import Calendar


class TaskCalendar(Calendar):
    table_class = 'table text-center'
    day_class = ''

    def get_day_class(self, date):
        if date.month != self.month:
            return "bg-info"

    def get_day_content(self, date):
        return '<a href="{}">{}</a>'.format(
            reverse_lazy('day_view', kwargs={
                'year': '{:0>4d}'.format(date.year),
                'month': '{:0>2d}'.format(date.month),
                'day': '{:0>2d}'.format(date.day),
            }),
            date.strftime('%d')
        )


class MonthView(View):
    """Presents a month view of tasks."""

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Processes the GET request."""
        year = int(kwargs['year'])
        month = int(kwargs['month'])

        cal = TaskCalendar(year, month)

        ctx = {
            'date': datetime.date(year, month, 1),
            'calendar': cal,
        }
        return render(request, 'todo/month_view.html', ctx)
