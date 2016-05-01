from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from ..models import Task


@login_required
def delete_task(request, id):
    """
    Deletes Task with a given id.

    Redirects to the day view with the date of the deleted Task.
    """
    task = get_object_or_404(Task, id__exact=id, user__exact=request.user)
    date = task.date
    task.delete()
    redirect_url = '/todo/' + date.strftime('%Y/%m/%d')
    return HttpResponseRedirect(redirect_url)


@login_required
def toggle_task_status(request, id):
    """
    Toggles Task status.

    Redirects to the day view with the date of the edited Task.
    """
    task = get_object_or_404(Task, id__exact=id, user__exact=request.user)
    date = task.date
    task.status = not task.status
    task.save()
    redirect_url = '/todo/' + date.strftime('%Y/%m/%d')
    return HttpResponseRedirect(redirect_url)
