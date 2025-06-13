import api from './axios'
import type { ApiResponse } from '@/types/response.ts'
import type { Token } from '@/types/auth.ts'

export async function signUp(
  username: string,
  password: string,
  password2: string,
  firstName: string,
  lastName: string,
): Promise<ApiResponse<Token>> {
  const data = { username, password, password2, firstName, lastName }
  return await api.post('auth/sign-up', data)
}

export async function login(
  username: string,
  password: string,
): Promise<ApiResponse<Token>> {
  const data = { username, password }
  return await api.post('auth/login', data)
}
