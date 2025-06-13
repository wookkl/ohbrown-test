<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth.ts'
import { useRouter } from 'vue-router'

const username = ref<string>('')
const password = ref('')
const password2 = ref('')
const firstName = ref('')
const lastName = ref('')
const errors = ref<string[]>([])

const { signUp } = useAuthStore()
const router = useRouter()

const handleSignUp = async () => {
  errors.value = []
  try {
    await signUp(
      username.value, password.value, password2.value, firstName.value, lastName.value
    )
    router.replace('/')
  } catch (err) {
    errors.value = Object.values(err.response.data).flatMap(value =>
      Array.isArray(value) ? value : [value]
    )
  }
}
</script>


<template>
  <div>
    <h2>회원가입</h2>
    <form @submit.prevent="handleSignUp">
      <div class="form-group">
        <label for="username">아이디</label>
        <input id="username" v-model="username" type="text" required/>
      </div>
      <div class="form-group">
        <label for="password">비밀번호</label>
        <input id="password" v-model="password" type="password" required/>
      </div>
      <div class="form-group">
        <label for="password">비밀번호 재확인</label>
        <input id="password2" v-model="password2" type="password" required/>
      </div>
      <div class="form-group">
        <label for="lastName">성</label>
        <input id="lastName" v-model="lastName" type="text" required/>
      </div>
      <div class="form-group">
        <label for="firstName">이름</label>
        <input id="firstName" v-model="firstName" type="text" required/>
      </div>
      <button type="submit">회원가입</button>
    </form>
    <div v-if="errors.length !== 0" class="errors">
      <p>아래 오류들을 해결해주새요.</p>
      <div v-for="(error, index) in errors" :key="index" class="error">
        {{ error }}
      </div>
    </div>

  </div>
</template>

<style scoped>
.form-group {
  display: flex;
  margin: 8px;
  justify-content: space-between;
}

label {
  margin-right: 8px;
}

.errors {
  margin-top: 8px;
  padding: 8px;
  border: 0.5px solid darkgrey;
}

.error {
  color: indianred;
}
</style>

