from rest_framework import serializers

from utils.serializer import inline_serializer


class TaskCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()


class TaskListRequestSerializer(serializers.Serializer):
    cursor = serializers.CharField(required=False, default=None)
    page_size = serializers.IntegerField(required=False, default=5)


class TaskUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()


class TaskDetailResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class TaskListResponseSerializer(serializers.Serializer):
    tasks = inline_serializer(fields={
        'id': serializers.IntegerField(),
        'title': serializers.CharField(),
        'status': serializers.CharField(),
    }, many=True)
