<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
import { storeToRefs } from 'pinia'
import { onMounted } from 'vue'
import { useTaskStore } from '@/stores/task.ts'
import { statusMap } from '@/types/task.ts'
import router from '@/router'

const userStore = useUserStore()
const { user } = storeToRefs(userStore)
const taskStore = useTaskStore()

const onTaskSelected = async (taskId: number) => {
  router.push(`/task/${taskId}`)
}
const handleCreate = async () => {
  router.push('/task/create')
}
onMounted(async () => {
  if (taskStore.tasks.length === 0) {
    await taskStore.loadList()
  }
})
</script>

<template>
  <h1 class="welcome-title">안녕하세요, {{ user?.lastName }}{{ user?.firstName }}님!</h1>
  <div class="content">
    <h2>TODO LIST</h2>
    <div @click="handleCreate" class="create-btn">생성하기</div>
  </div>
  <div>
    <div v-for="(task, index) in taskStore.tasks" :key="index"
         class="task" @click="onTaskSelected(task.id)">
      <div class="task-title">{{ task.title }}</div>
      <div class="task-status">{{ statusMap[task.status] }}</div>
    </div>
  </div>
</template>

<style scoped>
.welcome-title {
  margin: 8px;
}

.task {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #ddd;
  padding: 12px 16px;
  margin-bottom: 10px;
  border-radius: 8px;
  background-color: #f9f9f9;
  cursor: pointer;
  transition: background-color 0.2s;
}

.content {
  display: flex;
  justify-content: space-between;
  margin-bottom: 18px;
}

.task:hover {
  background-color: #ececec;
}

.task-title {
  font-weight: bold;
}

.task-status {
  color: #666;
  font-size: 0.9rem;
}

.create-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4px 10px;
  font-size: 12px;
  color: white;
  border-radius: 4px;
  background-color: dodgerblue;
  cursor: pointer;
}
</style>
