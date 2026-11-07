import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://yididiel7.github.io',
  base: '/create-tutorials',
  output: 'static',
  integrations: [tailwind()],
});