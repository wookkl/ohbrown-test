// src/services/authService.ts
import { login, signUp } from '@/api/auth'
import type { Token } from '@/types/auth'
import type { ApiResponse } from '@/types/response.ts'

export class AuthService {
  async signUp(
    username: string, password: string, password2: string, firstName: string, lastName: string
  ): Promise<ApiResponse<Token>> {
    const res = await signUp(username, password, password2, firstName, lastName)

    if (res.data.access && res.data.refresh) {
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
    }
    return res
  }

  async login(username: string, password: string): Promise<ApiResponse<Token>> {
    const res = await login(username, password)
    // 예: accessToken 저장, 상태 업데이트 등 부가 로직 처리
    if (res.data.access && res.data.refresh) {
      localStorage.setItem('access', res.data.access)
      localStorage.setItem('refresh', res.data.refresh)
    }
    return res
  }
}
