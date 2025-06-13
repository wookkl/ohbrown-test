import { defineStore } from 'pinia'
import { UserService } from '@/services/user.ts'
import type { User } from '@/types/user.ts'
import { removeAccessToken } from '@/utils/token.ts'

const userService = new UserService()

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null as User | null
  }),

  actions: {
    async initAccount() {
      try {
        const res = await userService.getMine()
        if (res) {
          this.user = res
        }
      } catch {
        removeAccessToken()
      }
    },
  }
})
