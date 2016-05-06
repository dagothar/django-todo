from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Defines a single task.

    Attributes:
        user (User): The owner of the task.
        date (date): The date of the task.
        status (boolean): The status of the task: True - done or False - not done.
        description (str): The name of the task.
    """
    class Meta:
        app_label = 'todo'

    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        """
        Returns string representation of the model.

        Returns:
            str: String representation of the task, e.g.:
                user1: [X] finish the app @ 2016-04-30
        """
        return '{user}: [{status}] {description} @ {date}'.format(
            user=self.user.username,
            status='X' if self.status else ' ',
            description=self.description,
            date=self.date.strftime('%Y-%m-%d'),
        )
