import { getMine } from '@/api/user'
import type { User } from '@/types/user.ts'

export class UserService {
  async getMine(): Promise<User | null> {
    const res = await getMine()
    if (res.status !== 200) {
      return null
    }
    return res.data
  }
}
