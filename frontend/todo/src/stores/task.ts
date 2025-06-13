import { defineStore } from 'pinia'
import type { ApiResponse } from '@/types/response.ts'
import { TaskService } from '@/services/task.ts'
import type { TaskListItem, Task, TaskStatus } from '@/types/task.ts'

const taskService = new TaskService()

export const useTaskStore = defineStore('task', {
  state: () => ({
    tasks: [] as TaskListItem[],
    cursor: undefined as string | null | undefined,
    selectedTask: null as Task | null,
  }),
  actions: {
    async create(title: string, description: string): Promise<ApiResponse<Task>> {
      const response = await taskService.create(title, description)
      this.tasks.unshift(response.data)
      return response
    },
    async loadList() {
      // TODO
      const response = await taskService.getList(this.cursor, 100)
      this.cursor = response.cursor
      response.data.tasks.forEach((task) => {
        this.tasks.push(task)
      })
    },
    async get(id: number): Promise<ApiResponse<Task>> {
      return await taskService.get(id)
    },
    async update(id: number, title: string, description: string, status: TaskStatus): Promise<ApiResponse<Task>> {
      const response = await taskService.update(id, title, description, status)

      const task = this.tasks.find(t => t.id === response.data.id)
      if (task) {
        Object.assign(task, response.data)
      }

      this.selectedTask = response.data
      return response
    },
    async delete(id: number) {
      await taskService.delete(id)
      const index = this.tasks.findIndex(t => t.id === id)
      this.tasks.splice(index, 1)
      this.selectedTask = null
    },
  }
})
