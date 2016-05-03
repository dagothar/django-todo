from __future__ import absolute_import
from django.utils.html import html_safe
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
import calendar as py_calendar


@html_safe
@python_2_unicode_compatible
class Calendar(object):
    table_class = ""
    day_class = ""

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        """Returns the calendar rendered to html."""
        return unicode(self.render())

    def render(self):
        weeks = self.get_weeks()

        output = []
        output.append('<table class="{}">'.format(self.get_table_class()))
        for week in weeks:
            output.append('<tr>')
            for day in week:
                output.append(self.render_day(day))
            output.append('</tr>')
        output.append('</table>')

        return '\n'.join(output)

    def get_weeks(self):
        """
        Returns a list of weeks of the month.

        Each week is the list of 7 days. Included are the days necessary to
        complete a week, even if they are not the days of the current month.
        """
        cal = py_calendar.Calendar()
        return cal.monthdatescalendar(self.year, self.month)

    def get_table_class(self):
        """Returns the css classes to be added to the table tag."""
        return self.table_class

    def render_day(self, date):
        return '<td class="{}">{}</td>'.format(
            self.get_day_class(date),
            self.get_day_content(date)
        )

    def get_day_class(self, date):
        """Returns css classes to be added to the td tag."""
        return self.day_class

    def get_day_content(self, date):
        """Returns the content of the day td cell."""
        return date.strftime('%d')
