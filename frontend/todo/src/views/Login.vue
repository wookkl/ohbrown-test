<script setup lang="ts">
import { ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.ts'

const router = useRouter()
const { login } = useAuthStore()
const username = ref('')
const password = ref('')
const errorMessage = ref('')

const handleLogin = async () => {
  try {
    await login(username.value, password.value)
    router.push('/')
  } catch (err) {
    if (err.response.status !== 500) {
      errorMessage.value = "서버오류가 발생했습니다"
    }
    errorMessage.value = "아이디 또는 패스워드가 잘못되었습니다"
  }
}
</script>

<template>
  <div>
    <h2>로그인</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">아이디</label>
        <input id="username" v-model="username" type="text" required/>
      </div>

      <div class="form-group">
        <label for="password">비밀번호</label>
        <input id="password" v-model="password" type="password" required/>
      </div>
      <button type="submit">로그인</button>
    </form>
    <div>
      <div>아직 계정이 없으신가요?</div>
      <RouterLink to="/sign-up">회원가입</RouterLink>
    </div>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>
<style scoped>
label {
  margin-right: 8px;
}
</style>
