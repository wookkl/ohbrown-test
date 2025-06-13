from dataclasses import dataclass
from typing import Dict


@dataclass
class TaskCreateCommand:
    title: str
    description: str

    @staticmethod
    def to_command(validated_data: Dict):
        return TaskCreateCommand(title=validated_data['title'], description=validated_data['description'])
