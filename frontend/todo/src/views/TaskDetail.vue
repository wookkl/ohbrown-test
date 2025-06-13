<script setup lang="ts">
import { statusMap, type TaskStatus } from '@/types/task.ts'
import { onMounted } from 'vue'
import router from '@/router'
import { useTaskStore } from '@/stores/task.ts'

const props = defineProps<{ id: number }>()

const taskStore = useTaskStore()
const statusClass = (status: TaskStatus) => {
  if (status === 'IN_PROGRESS') return 'status-in-progress'
  if (status === 'DONE') return 'status-done'
  if (status === 'TODO') return 'status-todo'
  return ''
}

const handleEdit = async () => {
  if (taskStore.selectedTask) {
    router.push('/task/edit')
  }
}
const handleGoBack = () => {
  router.back()
}
const handleDelete = () => {
  if (taskStore.selectedTask) {
    taskStore.delete(taskStore.selectedTask.id)
    router.back()
  }
}
onMounted(async () => {
  try {
    await taskStore.get(props.id).then((resp) => {
        taskStore.selectedTask = resp.data
      }
    )
  } catch (e) {
    router.back()
  }
})

</script>

<template>
  <div v-if="taskStore.selectedTask" class="container">
    <div class="header">
      <h2 class="title">{{ taskStore.selectedTask.title }}</h2>
      <div class="badge-wrapper">
        <div :class="statusClass(taskStore.selectedTask.status)" class="badge">
          {{ statusMap[taskStore.selectedTask.status] }}
        </div>
      </div>
    </div>
    <div class="options">
      <div @click="handleEdit" class="edit-btn">편집</div>
      <div @click="handleDelete" class="delete-btn">삭제</div>
    </div>
    <p class="description">{{ taskStore.selectedTask.description }}</p>
    <div class="back-btn-wrapper">
      <div @click="handleGoBack" class="back-btn">뒤로가기</div>
    </div>
  </div>
</template>

<style scoped>
.header {
  display: flex;
  gap: 8px;
  justify-content: space-between;
  align-items: center;
}

.options {
  display: flex;
  gap: 12px;
  margin-bottom: 12px;
}

.container {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 24px;
  min-width: 300px;
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}

.title {
  font-size: 24px;
  font-weight: bold;
}

.badge-wrapper {
  display: flex;
  justify-content: end;
}

.badge {
  padding: 4px 10px;
  font-size: 12px;
  border-radius: 999px;
  color: white;
}

.description {
  color: #444;
  line-height: 1.6;
  white-space: pre-line;
}

.status-in-progress {
  background-color: #3b82f6;
}

.status-done {
  background-color: #10b981;
}

.status-todo {
  background-color: #6b7280;
}

.edit-btn {
  padding: 4px 10px;
  font-size: 12px;
  color: black;
  margin-bottom: 16px;
  border: 0.5px solid #6b7280;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn {
  padding: 4px 10px;
  font-size: 12px;
  color: black;
  margin-bottom: 16px;
  border: 0.5px solid indianred;
  border-radius: 4px;
  cursor: pointer;
}

.back-btn-wrapper {
  margin-top: 12px;
  display: flex;
  justify-content: end;
}

.back-btn {
  padding: 4px 10px;
  font-size: 10px;
  color: slategray;
  border: 0.5px solid #6b7280;
  border-radius: 4px;
  cursor: pointer;
}
</style>
