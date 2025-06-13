from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.task.views import TaskViewSet

task_router = SimpleRouter(trailing_slash=False)
task_router.register(r'tasks', TaskViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('apps.account.urls', namespace='auth')),
    path(r'', include(task_router.urls)),
]
