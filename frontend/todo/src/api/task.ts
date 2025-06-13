import api from './axios'
import type { ApiResponse } from '@/types/response.ts'
import type { Task, TaskList, TaskStatus } from '@/types/task.ts'

export async function createTask(
  title: string, description: string
): Promise<ApiResponse<Task>> {
  const data = { title, description }
  return await api.post('tasks', data)
}

export async function updateTask(
  id: number, title?: string, description?: string, status?: TaskStatus
): Promise<ApiResponse<Task>> {
  const data = { title, description, status }
  // TODO
  return await api.patch(`tasks/${id}`, data)
}

export async function getTask(id: number): Promise<ApiResponse<Task>> {
  return await api.get(`tasks/${id}`)
}

export async function getTaskList(
  cursor?: string | null, pageSize: number = 5
): Promise<ApiResponse<TaskList>> {
  const params = { cursor, pageSize }
  return await api.get('tasks', { params })
}

export async function deleteTask(id: number): Promise<ApiResponse<{}>> {
  return await api.delete(`tasks/${id}`)
}
