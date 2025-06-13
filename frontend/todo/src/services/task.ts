// src/services/authService.ts
import { createTask, getTaskList, getTask, updateTask, deleteTask } from '@/api/task'
import type { ApiResponse } from '@/types/response.ts'
import type { TaskList, Task, TaskStatus } from '@/types/task.ts'

export class TaskService {
  async create(title: string, description: string): Promise<ApiResponse<Task>> {
    return await createTask(title, description)
  }

  async get(id: number): Promise<ApiResponse<Task>> {
    return await getTask(id)
  }

  async getList(cursor?: string | null, pageSize: number = 5,): Promise<ApiResponse<TaskList>> {
    return await getTaskList(cursor, pageSize)
  }

  async update(id: number, title?: string, description?: string, status?: TaskStatus): Promise<ApiResponse<Task>> {
    return await updateTask(id, title, description, status)
  }

  async delete(id: number): Promise<ApiResponse<{}>> {
    return await deleteTask(id)
  }
}
