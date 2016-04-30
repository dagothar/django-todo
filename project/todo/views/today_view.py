from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
import datetime


class TodayView(RedirectView):
    """Redirects the user to the day view for today, e.g.: todo/2016/04/30."""

    def get_redirect_url(self, *args, **kwargs):
        """Returns URL to a day view with today's date."""
        date = datetime.date.today()
        return '/todo/{:0>4d}/{:0>2d}/{:0>2d}'.format(
            date.year,
            date.month,
            date.day
        )
