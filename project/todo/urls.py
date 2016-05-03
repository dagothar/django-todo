from django.conf.urls import url
import django.contrib.auth.views as auth_views
from django.views.generic import RedirectView
from django.views.generic import TemplateView

import views


urlpatterns = [
    # login view
    url(
        r'^login$',
        auth_views.login,
        {'template_name': 'todo/login.html'},
        name='login'
    ),
    # logout view
    url(
        r'^logout$',
        auth_views.logout,
        {'template_name': 'todo/logout.html'},
        name='logout'
    ),
    # register view
    url(
        r'^register$',
        views.RegisterView.as_view(),
        name='register'
    ),
    # register success view
    url(
        r'^register_success$',
        TemplateView.as_view(template_name='todo/registration_successful.html'),
        name='register_success'
    ),
    # main view, redirects to /today
    url(
        r'^$',
        RedirectView.as_view(url='today'),
        name='home'
    ),
    # today view, e.g.: /todo/today
    url(
        r'^today$',
        views.TodayView.as_view(),
        name='today_view'
    ),
    # single day view, e.g.: /todo/2016/04/30
    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})$',
        views.DayView.as_view(),
        name='day_view'
    ),
    # month view, e.g.: /todo/2016/04
    url(
        r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$',
        views.MonthView.as_view(),
        name='month_view'
    ),
    # this month view, e.g.: /todo/this_month
    url(
        r'^this_month$',
        views.ThisMonthView.as_view(),
        name='this_month_view'
    ),
    # delete task, e.g. /todo/delete/1
    url(
        r'^delete/(?P<id>[0-9]+)',
        views.delete_task,
        name='delete_task'
    ),
    # toggle task status, e.g. /todo/toggle/1
    url(
        r'^toggle/(?P<id>[0-9]+)',
        views.toggle_task_status,
        name='toggle_task'
    ),
]
