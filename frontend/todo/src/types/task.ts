export interface Task {
  id: number
  title: string
  description: string
  status: TaskStatus
  createdAt: string
  updatedAt: string
}

export interface TaskListItem {
  id: number
  title: string
  status: TaskStatus
}

export interface TaskList {
  tasks: TaskListItem[]
}

export type TaskStatus = 'TODO' | 'IN_PROGRESS' | 'DONE'

export const statusMap = {
  IN_PROGRESS: '진행중',
  DONE: '완료',
  TODO: '해야할 일'
}
