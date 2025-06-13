import datetime
from dataclasses import dataclass
from typing import List

from apps.task.choices import TaskStatus
from apps.task.models import Task


@dataclass
class TaskInfo:
    id: int
    title: int
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def from_model(model: Task):
        return TaskInfo(
            id=model.id, title=model.title, description=model.description, status=model.status,
            created_at=model.created_at, updated_at=model.updated_at
        )


@dataclass
class TaskListInfo:
    tasks: List[TaskInfo]
