from django.conf.urls import url
import django.contrib.auth.views as auth_views

import views


urlpatterns = [
    # login view
    url(
        r'^login',
        auth_views.login,
        {'template_name': 'todo/login.html'},
        name='login'
    ),
    # logout view
    url(
        r'^logout',
        auth_views.logout,
        {'template_name': 'todo/logout.html'},
        name='logout'
    ),
    # today view, e.g.: todo/today
    url(
        r'^today',
        views.TodayView.as_view(),
        name='today_view'
    ),
    # single day view, e.g.: todo/2016/04/30
    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})',
        views.DayView.as_view(),
        name='day_view'
    ),
    # month view, e.g.: todo/2016/04
    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})',
        views.MonthView.as_view(),
        name='month_view'
    ),
]
