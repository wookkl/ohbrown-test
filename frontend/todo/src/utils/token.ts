const ACCESS_KEY = 'access'
const REFRESH_KEY = 'refresh'

export const getAccessToken = () => localStorage.getItem(ACCESS_KEY)
export const setAccessToken = (token: string) => localStorage.setItem(ACCESS_KEY, token)
export const removeAccessToken = () => localStorage.removeItem(ACCESS_KEY)
