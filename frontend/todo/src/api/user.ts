import api from './axios'
import type { ApiResponse } from '@/types/response.ts'
import type { User } from '@/types/user.ts'

export async function getMine(): Promise<ApiResponse<User>> {
  return await api.get('users/mine')
}
