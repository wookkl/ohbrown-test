<script setup lang="ts">
import { ref } from 'vue'
import { useTaskStore } from '@/stores/task.ts'
import router from '@/router'

const taskStore = useTaskStore()
const title = ref<string>('')
const description = ref<string>('')

const handleCreate = async () => {
  if (title.value !== '') {
    await taskStore.create(title.value, description.value)
    title.value = ''
    description.value = ''
  }
  router.back()
}
const handleGoBack = () => {
  router.back()
}
</script>

<template>
  <h1>생성하기</h1>
  <form @submit.prevent="handleCreate">
    <div class="form-group">
      <label for="title">할 일</label>
      <input id="title" v-model="title" type="text" required/>
    </div>
    <div class="form-group">
      <label for="description">상세 내용</label>
      <input id="description" v-model="description" type="text" required/>
    </div>
    <div class="btn-wrapper">
      <button type="submit">생성</button>
      <div @click="handleGoBack" class="back-btn">뒤로가기</div>
    </div>
  </form>
</template>

<style scoped>
input {
  margin: 8px;
}

.btn-wrapper {
  margin-top: 12px;
  display: flex;
  justify-content: space-between;
}

.back-btn {
  padding: 4px 10px;
  font-size: 12px;
  color: slategray;
  border: 0.5px solid #6b7280;
  border-radius: 4px;
  cursor: pointer;
}
</style>
