import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const tutorials = defineCollection({
  loader: glob({ pattern: '**/[^_]*.json', base: './src/content/tutorials' }),
  schema: z.object({
    slug: z.string(),
    filePath: z.string(),
    title: z.string(),
    date: z.string().nullable(),
    author: z.string(),
    category: z.string(),
    tags: z.array(z.string()),
    description: z.string(),
    headings: z.array(z.object({ level: z.number(), text: z.string(), slug: z.string() })),
    readingTime: z.number(),
    content: z.string(),
  }),
});

export const collections = { tutorials };