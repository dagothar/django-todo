from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render

from ..util import Calendar


class TaskCalendar(Calendar):
    table_class = "table text-center"

    def get_day_content(self, date):
        return '<a href="#">{}</a>'.format(date.strftime('%d'))


class MonthView(View):
    """Presents a month view of tasks."""

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Processes the GET request."""
        year = int(kwargs['year'])
        month = int(kwargs['month'])

        cal = TaskCalendar(year, month)

        ctx = {
            'calendar': cal,
        }
        return render(request, 'todo/month_view.html', ctx)
