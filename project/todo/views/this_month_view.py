from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
import datetime


class ThisMonthView(RedirectView):
    """Redirects the user to the day view for this month."""

    def get_redirect_url(self, *args, **kwargs):
        """Returns URL to a month view with today's date."""
        date = datetime.date.today()
        return '/todo/{:0>4d}/{:0>2d}'.format(
            date.year,
            date.month
        )
