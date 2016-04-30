from django.conf.urls import url

import views


urlpatterns = [
    # single day view, e.g.: todo/16/04/30
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})', views.DayView.as_view(), name='day_view'),
]
