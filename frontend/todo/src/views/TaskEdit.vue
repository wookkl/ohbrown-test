<script setup lang="ts">

import { useTaskStore } from '@/stores/task.ts'
import { ref } from 'vue'
import type { TaskStatus } from '@/types/task.ts'
import router from '@/router'

const taskStore = useTaskStore()

const title = ref<string>(taskStore.selectedTask?.title ?? '')
const description = ref<string>(taskStore.selectedTask?.description ?? '')
const status = ref<TaskStatus>(taskStore.selectedTask?.status ?? 'TODO')

const handleEdit = async () => {
  if (taskStore.selectedTask) {
    taskStore.update(taskStore.selectedTask.id, title.value, description.value, status.value)
  }
  router.back()
}

const handleGoBack = () => {
  router.back()
}
</script>

<template>
  <h1>편집</h1>
  <form @submit.prevent="handleEdit">
    <div class="form-group">
      <label for="title">할 일</label>
      <input id="title" v-model="title" type="text" required/>
    </div>
    <div class="form-group">
      <label for="description">상세 내용</label>
      <input id="description" v-model="description" type="text" required/>
    </div>
    <div class="form-group">
      <label for="description">상태</label>
      <select v-model="status">
        <option value="TODO">할 일</option>
        <option value="IN_PROGRESS">진행 중</option>
        <option value="DONE">완료</option>
      </select>
    </div>
    <div class="submit-wrapper">
      <button type="submit" class="submit">변경</button>
      <div class="back-btn" @click="handleGoBack">뒤로가기</div>
    </div>
  </form>

</template>

<style scoped>
.form-group {
  margin: 8px;
  display: flex;
  justify-content: space-between;
}

label {
  margin-right: 16px;
}

input {
  width: 150px;
}

.submit-wrapper {
  display: flex;
  justify-content: center;
}

.submit {
  font-size: 16px;
}

.back-btn {
  margin-left: 8px;
  padding: 4px 10px;
  font-size: 12px;
  color: grey;
  border: 0.5px solid #6b7280;
  border-radius: 4px;
  cursor: pointer;
}
</style>
