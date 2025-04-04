import { initTRPC } from '@trpc/server'
import { z } from 'zod'

const t = initTRPC.create()

const publicProcedure = t.procedure
const router = t.router

export const appRouter = router({
  hello: publicProcedure.input(z.string().nullish()).query(({ input }) => {
    return `Hello ${input ?? 'World'}!`
  }),
  getUser: publicProcedure
    .input(z.object({ id: z.string().nullish() }))
    .query(({ input }) => {
      return `User ${input.id ?? 'unknown'}`
    }),
  nustFetch: publicProcedure
  .output(z.array(z.object({
    userId: z.number(),
    id: z.number(),
    title: z.string(),
    body: z.string(),
  })))
  .query(async() => {
    return fetch('https://jsonplaceholder.typicode.com/posts')
      .then((res) => res.json())
      .then((data) => data as Array<{ userId: number; id: number; title: string; body: string; }>)
  })
})

export type AppRouter = typeof appRouter
