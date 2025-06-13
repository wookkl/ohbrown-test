<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth.ts'
import { useRouter } from 'vue-router'

const { initAccount } = useUserStore()
const { access } = useAuthStore()
const router = useRouter()

onMounted(async () => {
  if (access) {
    await initAccount()
  } else {
    router.push('/login')
  }
})

</script>

<template>
  <div>
    <router-view/>
  </div>
</template>
