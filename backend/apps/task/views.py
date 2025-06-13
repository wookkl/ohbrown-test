from rest_framework import status, permissions

from apps.task import dto
from apps.task import services, serializers
from utils.viewset import CustomViewSet


class TaskViewSet(CustomViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request):
        serializer = serializers.TaskCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cmd = dto.TaskCreateCommand.to_command(serializer.validated_data)
        task = services.task_create(user=request.user, command=cmd)
        data = serializers.TaskDetailResponseSerializer(task).data
        return self.response(status=status.HTTP_201_CREATED, data=data)

    def list(self, request):
        serializer = serializers.TaskListRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        cursor = serializer.validated_data['cursor']
        page_size = serializer.validated_data['page_size']
        task_list, cursor = services.task_get_list(user=request.user, cursor=cursor, page_size=page_size)
        data = serializers.TaskListResponseSerializer(task_list).data
        return self.cursor_response(status=status.HTTP_200_OK, data=data, cursor=cursor)

    def retrieve(self, request, pk):
        task = services.task_get(user=request.user, pk=pk)
        data = serializers.TaskDetailResponseSerializer(task).data
        return self.response(status=status.HTTP_200_OK, data=data)

    def partial_update(self, request, pk):
        serializer = serializers.TaskUpdateRequestSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        task = services.task_update(user=request.user, pk=pk, update_fields=serializer.validated_data)
        data = serializers.TaskDetailResponseSerializer(task).data
        return self.response(status=status.HTTP_200_OK, data=data)

    def destroy(self, request, pk):
        services.task_delete(user=request.user, pk=pk)
        return self.response(status=status.HTTP_204_NO_CONTENT)
