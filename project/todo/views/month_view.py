from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar


class TaskCalendar(HTMLCalendar):
    def formatday(self, day, weekday):
        return super.formatday(day, weekday)
    pass


class MonthView(View):
    """Presents a month view of tasks."""

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Processes the GET request."""
        year = int(kwargs['year'])
        month = int(kwargs['month'])

        calendar = HTMLCalendar()
        ctx = {
            'calendar': mark_safe(calendar.formatmonth(year, month))
        }
        return render(request, 'todo/month_view.html', ctx)
