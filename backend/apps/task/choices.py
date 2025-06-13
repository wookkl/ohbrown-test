from django.db.models import TextChoices


class TaskStatus(TextChoices):
    TODO = ('TODO', 'todo')
    IN_PROGRESS = ('IN_PROGRESS', 'in_progress')
    DONE = ('DONE', 'done')
