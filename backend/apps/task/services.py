from typing import Dict, Tuple

from django.shortcuts import get_object_or_404

from apps.account.models import User
from apps.task.choices import TaskStatus
from apps.task.dto import TaskCreateCommand, TaskInfo, TaskListInfo
from apps.task.models import Task
from utils.decorators import service
from utils.paginator import CustomCursorPagination


@service
def task_create(*, user: User, command: TaskCreateCommand) -> TaskInfo:
    task = Task.objects.create(
        user=user, title=command.title, description=command.description, status=TaskStatus.TODO
    )
    return TaskInfo.from_model(task)


@service
def task_update(*, user: User, pk: int, update_fields: Dict) -> TaskInfo:
    task = get_object_or_404(Task.objects, user=user, pk=pk)
    task.update(**update_fields)
    return TaskInfo.from_model(task)


@service
def task_delete(*, user: User, pk: int):
    task = get_object_or_404(Task.objects, user=user, pk=pk)
    task.delete()


@service
def task_get_list(*, user: User, page_size: int = 5, cursor: str = None) -> Tuple[TaskListInfo, str]:
    paginator = CustomCursorPagination()
    paginator.ordering = '-created_at'
    queryset = Task.objects.filter(user=user)
    paginated_queryset = paginator.paginate_queryset(queryset=queryset, page_size=page_size, cursor_str=cursor)
    tasks = [TaskInfo.from_model(task) for task in paginated_queryset]
    cursor = paginator.get_next_link()
    return TaskListInfo(tasks=tasks), cursor


@service
def task_get(*, user: User, pk: int) -> TaskInfo:
    task = get_object_or_404(Task.objects, user=user, pk=pk)
    return TaskInfo.from_model(task)
