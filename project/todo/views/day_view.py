from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import ProcessFormView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

from .. import models
from .. import forms


class DayView(LoginRequiredMixin, FormMixin, ListView, ProcessFormView):
    """
    Single day view.

    Presents a list of the tasks of the currently logged user for a given day.
    Additionaly, a form is presented to add a new task.
    """
    model = models.Task
    template_name = 'todo/day_view.html'
    context_object_name = 'tasks'
    form_class = forms.TaskForm

    def get_date(self):
        """
        Constructs date from the view url parameters.

        Returns:
            date: Date object constructed from the url path, e.g.:
                todo/2016/04/30 yields 2016-04-30 date.
        """
        return datetime.date(
            int(self.kwargs['year']),
            int(self.kwargs['month']),
            int(self.kwargs['day'])
        )

    def get_queryset(self):
        """Returns a list of tasks of the logged in user for a given day."""
        return models.Task.objects.filter(
            user__exact=self.request.user,
            date__exact=self.get_date()
        )

    def get_percent_completed(self):
        """Calculates the percentage of completed tasks."""
        completed = self.object_list.filter(status__exact=True).count()
        total = len(self.object_list)
        return int(100 * completed / total) if total > 0 else 0

    def get_context_data(self, **kwargs):
        """
        Adds day view context objects.

        Adds following context objects:
            tasks: A list of Tasks.
            date: The current date.
            prev_date: The previous day.
            next_date: The next day.
            form: A new task form.
            progress: The percentage of completed tasks.
        """
        context = super(LoginRequiredMixin, self).get_context_data(**kwargs)
        date = self.get_date()
        context['date'] = date
        context['prev_date'] = date - datetime.timedelta(days=1)
        context['next_date'] = date + datetime.timedelta(days=1)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        context['progress'] = self.get_percent_completed()
        return context

    def get_success_url(self):
        """
        Returns the current URL.

        Overrides the get_success_url() method from FormMixin.
        """
        return self.request.path

    def form_valid(self, form):
        """
        Handles processing if the form is valid.

        Overrides form_valid() from FormMixin. Sets the currently logged User
        on the newly created Task object.
        """
        new_task = form.save(commit=False)
        new_task.user = self.request.user
        new_task.date = self.get_date()
        new_task.save()
        return super(LoginRequiredMixin, self).form_valid(form)

    def form_invalid(self, form):
        """
        Handles processing if the form is invalid.

        Overrides form_invalid() from FormMixin.
        """
        return self.get(self.request, form=form)
