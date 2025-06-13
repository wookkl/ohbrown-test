import { defineStore } from 'pinia'
import { AuthService } from '@/services/auth'
import { useUserStore } from '@/stores/user.ts'
import { setAccessToken } from '@/utils/token.ts'
import type { ApiResponse } from '@/types/response.ts'
import type { Token } from '@/types/auth.ts'

const authService = new AuthService()

export const useAuthStore = defineStore('auth', {
  state: () => ({
    access: localStorage.getItem('access') || '',
    isLoggedIn: !!localStorage.getItem('access'),
  }),

  actions: {
    async handleLoginSuccess(token: Token) {
      this.access = token.access
      this.isLoggedIn = true
      setAccessToken(this.access)
      const { initAccount } = useUserStore()
      await initAccount()
    },

    async login(username: string, password: string): Promise<ApiResponse<Token>> {
      const res = await authService.login(username, password)
      if (res.data.access && res.data.refresh) {
        await this.handleLoginSuccess(res.data)
      }
      return res
    },

    async signUp(username: string, password: string, password2: string, firstName: string, lastName: string): Promise<ApiResponse<Token>> {
      const res = await authService.signUp(username, password, password2, firstName, lastName)
      if (res.data.access && res.data.refresh) {
        await this.handleLoginSuccess(res.data)
      }
      return res
    },
  }
})
