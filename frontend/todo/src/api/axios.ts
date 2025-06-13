import axios from 'axios'
import { getAccessToken } from '@/utils/token.ts'
import { toSnakeCase, toCamelCase } from '@/utils/caseConverter.ts'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
    'Accept-Language': 'ko',
  },
})


api.interceptors.request.use(
  (config) => {
    const token = getAccessToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    if (config.data) {
      config.data = toSnakeCase(config.data)
    }
    if (config.params) {
      config.params = toSnakeCase(config.params)
    }
    return config
  },
  (error) => Promise.reject(error)
)


api.interceptors.response.use(
  (response) => {
    if (response.data) {
      response.data = toCamelCase(response.data)
    }
    return response
  },
  error => {
    const status = error.response?.status
    if (status === 500) {
      console.error('서버 오류 발생')
    } else {
      console.error(error.message)
    }
    return Promise.reject(error)
  }
)

export default api
