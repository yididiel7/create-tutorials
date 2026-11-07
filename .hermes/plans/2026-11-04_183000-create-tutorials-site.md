# Plan: Build Tutorial Website for create-tutorials (GitHub Pages)

**Goal:** Convert the `~/labs/experiments/create-tutorials` markdown tutorial repository into a polished, searchable static website (Astro + Tailwind) styled like `zro.moonmath.ai`, deployed to GitHub Pages.

---

## Current Context / Assumptions

- **Repo:** `/home/srhills/labs/experiments/create-tutorials` — 200+ markdown files, flat + subdirs (`Niri-Guides/`, `Nm-Arch-Guide/`, `scripts/`), no existing site.
- **Reference:** `zro.moonmath.ai` — Next.js, dark-first, code-centric, token-stream hero, model-bento grid, testimonials, Clerk auth, PostHog. We'll borrow **visual language only** (fonts, dark theme, bento cards, token animation, stack diagram).
- **Host:** GitHub Pages (project site at `https://<user>.github.io/create-tutorials/`).
- **Stack:** Astro (static export), Tailwind CSS, TypeScript, `astro-icon` for Lucide icons, `fuse.js` for client-side search, `rehype-pretty-code` for syntax highlighting.
- **No backend:** No auth, no analytics, no Clerk. Pure static site.
- **Content source:** Existing `.md` files — frontmatter may be inconsistent; we'll parse what exists and infer structure from headings.

---

## Architecture / Approach

1. **Astro project** in `site/` subdirectory (keeps tutorial content separate from site code).
2. **Content pipeline:** Build-time script scans `../` for `.md`, extracts frontmatter + headings, writes `src/content/tutorials/*.json` (Astro content collections).
3. **Pages:** Home (hero + featured + search), Tutorial index (filterable grid), Tutorial detail (TOC, reading time, copy-code), Category pages (Niri, Nm-Arch, etc.), Tags page, 404.
4. **Styling:** Tailwind + CSS variables for theming (dark default, light toggle). Fonts: **Instrument Sans** (display), **JetBrains Mono** (code), **Inter** (body) — match zro.
5. **Deploy:** GitHub Actions workflow → `npm run build` → `actions/upload-pages-artifact` → `actions/deploy-pages`. Base path `/create-tutorials/`.

---

## Step-by-Step Tasks

### 0. Scaffold Astro Project

```bash
cd /home/srhills/labs/experiments/create-tutorials
npm create astro@latest site -- --template minimal --yes --install
cd site
npm install -D tailwindcss @astrojs/tailwind @astrojs/mdx @astrojs/sitemap
npm install fuse.js rehype-pretty-code shiki
npm install -D @iconify-json/lucide astro-icon
npx astro add tailwind mdx sitemap
```

**Verify:** `npm run dev` starts on `localhost:4321` with blank page.

---

### 1. Configure Astro + Tailwind

**File:** `site/astro.config.mjs`

```js
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://yididiel7.github.io',
  base: '/create-tutorials',
  output: 'static',
  integrations: [tailwind(), mdx(), sitemap()],
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
    rehypePlugins: [
      ['rehype-pretty-code', { theme: 'github-dark', keepBackground: true }],
    ],
  },
  vite: {
    css: { preprocessorOptions: { scss: { additionalData: `@use "src/styles/variables" as *;` } } },
  },
});
```

**File:** `site/tailwind.config.mjs`

```js
import defaultTheme from 'tailwindcss/defaultTheme';

export default {
  darkMode: 'class',
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Instrument Sans', ...defaultTheme.fontFamily.sans],
        mono: ['JetBrains Mono', ...defaultTheme.fontFamily.mono],
        body: ['Inter', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        canvas: 'var(--color-canvas)',
        ink: 'var(--color-ink)',
        muted: 'var(--color-muted)',
        rule: 'var(--color-rule)',
        accent: 'var(--color-accent)',
        'accent-hover': 'var(--color-accent-hover)',
      },
      animation: {
        'token-stream': 'token-stream 20s linear infinite',
      },
      keyframes: {
        'token-stream': {
          '0%': { transform: 'translateY(0)' },
          '100%': { transform: 'translateY(-50%)' },
        },
      },
    },
  },
  plugins: [],
};
```

**File:** `site/src/styles/global.css`

```css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

@layer base {
  :root {
    --color-canvas: #08090b;
    --color-ink: #f4f1ec;
    --color-muted: #71717a;
    --color-rule: #27272a;
    --color-accent: #f4f1ec;
    --color-accent-hover: #e4e0d9;
  }
  .light {
    --color-canvas: #fafafa;
    --color-ink: #08090b;
    --color-muted: #52525b;
    --color-rule: #e4e4e7;
    --color-accent: #08090b;
    --color-accent-hover: #18181b;
  }
  html { @apply font-body antialiased; }
  body { @apply bg-canvas text-ink min-h-screen; }
  ::selection { @apply bg-accent/30; }
}

@layer components {
  .btn-primary {
    @apply inline-flex items-center gap-2 rounded-sm px-4 py-2.5 text-sm font-medium
           bg-accent text-canvas transition-colors hover:bg-accent-hover;
  }
  .btn-secondary {
    @apply inline-flex items-center gap-2 rounded-sm px-4 py-2.5 text-sm font-medium
           border border-rule bg-transparent hover:bg-rule transition-colors;
  }
  .card {
    @apply rounded-lg border border-rule bg-canvas/50 p-6 transition-colors hover:border-accent/50;
  }
  .prose { @apply max-w-none; }
  .prose h1 { @apply display text-3xl font-bold tracking-tight; }
  .prose h2 { @apply display text-2xl font-semibold tracking-tight mt-10 mb-4; }
  .prose h3 { @apply display text-xl font-medium mt-8 mb-3; }
  .prose p { @apply text-base leading-7 text-muted mt-4; }
  .prose code { @apply font-mono text-sm bg-rule px-1.5 py-0.5 rounded; }
  .prose pre { @apply bg-rule/50 rounded-lg p-4 overflow-x-auto my-6; }
  .prose pre code { @apply bg-transparent p-0 text-base; }
  .prose a { @apply underline underline-offset-2 hover:text-accent transition-colors; }
  .prose ul { @apply list-disc list-inside space-y-2 mt-4; }
  .prose ol { @apply list-decimal list-inside space-y-2 mt-4; }
  .prose blockquote { @apply border-l-2 border-rule pl-4 italic text-muted my-6; }
}
```

**Verify:** `npm run dev` → page loads with dark background, correct fonts.

---

### 2. Font Setup (Local, Self-Hosted)

```bash
mkdir -p site/public/fonts
# Download woff2: Instrument Sans, Inter, JetBrains Mono
# Place in public/fonts/
```

**File:** `site/src/styles/fonts.css`

```css
@font-face {
  font-family: 'Instrument Sans';
  src: url('/fonts/InstrumentSans-Variable.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-Variable.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
@font-face {
  font-family: 'JetBrains Mono';
  src: url('/fonts/JetBrainsMono-Variable.woff2') format('woff2');
  font-weight: 100 800;
  font-display: swap;
}
```

Import in `global.css`: `@import './fonts.css';`

---

### 3. Content Pipeline — Scan Tutorials → JSON

**File:** `site/scripts/build-content.mjs`

```js
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { glob } from 'glob';

const ROOT = path.resolve('../');
const OUT_DIR = path.resolve('./src/content/tutorials');
const CATEGORIES = ['Niri-Guides', 'Nm-Arch-Guide', 'scripts'];

function slugify(str) {
  return str.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

function extractHeadings(content) {
  const regex = /^(#{2,4})\s+(.+)$/gm;
  const headings = [];
  let match;
  while ((match = regex.exec(content)) !== null) {
    headings.push({ level: match[1].length, text: match[2].trim(), slug: slugify(match[2]) });
  }
  return headings;
}

function readingTime(text) {
  const words = text.split(/\s+/).length;
  return Math.ceil(words / 200);
}

async function main() {
  if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

  const files = await glob('**/*.md', { cwd: ROOT, ignore: ['node_modules/**', 'site/**', '.hermes/**'] });
  const index = [];

  for (const file of files) {
    const full = path.join(ROOT, file);
    const raw = fs.readFileSync(full, 'utf-8');
    const { data, content } = matter(raw);

    const category = CATEGORIES.find(c => file.startsWith(c)) || 'General';
    const headings = extractHeadings(content);
    const time = readingTime(content);

    const item = {
      slug: slugify(path.basename(file, '.md')),
      filePath: file,
      title: data.Title || data.title || headings[0]?.text || path.basename(file, '.md'),
      date: data.Date || data.date || null,
      author: data.Author || data.author || 'Sr. Yididiel Hills',
      category,
      tags: data.Tags || data.tags || [],
      description: data.Description || data.description || content.slice(0, 200).replace(/[#*`]/g, '').trim() + '…',
      headings,
      readingTime: time,
      content, // store for detail page
    };

    fs.writeFileSync(path.join(OUT_DIR, `${item.slug}.json`), JSON.stringify(item, null, 2));
    index.push({ slug: item.slug, title: item.title, category: item.category, tags: item.tags, date: item.date, readingTime: item.readingTime, description: item.description });
  }

  fs.writeFileSync(path.join(OUT_DIR, '_index.json'), JSON.stringify(index, null, 2));
  console.log(`Built ${index.length} tutorials`);
}

main();
```

**File:** `site/package.json` — add script:

```json
"scripts": {
  "build:content": "node scripts/build-content.mjs",
  "dev": "npm run build:content && astro dev",
  "build": "npm run build:content && astro build",
  "preview": "astro preview"
}
```

**Run:** `npm run build:content` → verify `src/content/tutorials/*.json` created.

---

### 4. Astro Content Collection

**File:** `site/src/content/config.ts`

```ts
import { defineCollection, z } from 'astro:content';

const tutorials = defineCollection({
  type: 'data',
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
```

---

### 5. Layout Components

**File:** `site/src/components/ThemeToggle.astro`

```astro
---
const isDark = Astro.cookies.get('theme')?.value === 'dark' ?? true;
---
<script is:inline>
  const toggle = document.getElementById('theme-toggle');
  const html = document.documentElement;
  const saved = localStorage.getItem('theme');
  if (saved === 'light' || (!saved && window.matchMedia('(prefers-color-scheme: light)').matches)) {
    html.classList.add('light');
  }
  toggle?.addEventListener('click', () => {
    html.classList.toggle('light');
    localStorage.setItem('theme', html.classList.contains('light') ? 'light' : 'dark');
  });
</script>
<button id="theme-toggle" class="size-10 grid place-items-center rounded-sm hover:bg-rule transition-colors" aria-label="Toggle theme">
  <svg class="size-5 stroke-ink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <circle cx="12" cy="12" r="5" />
    <path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" />
  </svg>
</button>
```

**File:** `site/src/components/Header.astro`

```astro
---
import ThemeToggle from './ThemeToggle.astro';
const nav = [
  { href: '/', label: 'Home' },
  { href: '/tutorials', label: 'Tutorials' },
  { href: '/categories', label: 'Categories' },
  { href: '/tags', label: 'Tags' },
];
---
<header class="sticky top-0 z-30 border-b border-rule bg-canvas/80 backdrop-blur-sm">
  <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-3">
    <a href="/" class="flex shrink-0 items-center gap-2 text-xl font-semibold tracking-tight">
      <svg class="size-7" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="32" height="32" rx="6" class="stroke-ink stroke-2"/>
        <path d="M8 12h16M8 16h12M8 20h8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
      </svg>
      create-tutorials
    </a>
    <nav class="hidden md:flex items-center gap-1" aria-label="Main navigation">
      {nav.map(item => (
        <a href={item.href} class="rounded-sm px-3 py-1.5 text-sm font-medium transition-colors hover:text-accent">{item.label}</a>
      ))}
    </nav>
    <div class="flex items-center gap-2">
      <ThemeToggle />
    </div>
  </div>
</header>
```

**File:** `site/src/components/Footer.astro`

```astro
---
const year = new Date().getFullYear();
---
<footer class="border-t border-rule py-12">
  <div class="mx-auto max-w-7xl px-4 text-center text-sm text-muted">
    <p>© {year} Sr. Yididiel Hills · MIT License</p>
    <p class="mt-2">Built with Astro · Deployed on GitHub Pages</p>
  </div>
</footer>
```

**File:** `site/src/layouts/Layout.astro`

```astro
---
interface Props { title: string; description?: string; }
const { title, description } = Astro.props;
---
<!doctype html>
<html lang="en" class="dark">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="generator" content={Astro.generator} />
    <title>{title}</title>
    <meta name="description" content={description || 'Linux/Arch tutorials, guides, and references.'} />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description || 'Linux/Arch tutorials, guides, and references.'} />
    <meta property="og:type" content="website" />
  </head>
  <body class="flex min-h-screen flex-col font-body">
    <slot name="header" />
    <main class="flex-1">
      <slot />
    </main>
    <slot name="footer" />
  </body>
</html>
```

**File:** `site/src/layouts/PageLayout.astro`

```astro
---
import Layout from './Layout.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
interface Props { title: string; description?: string; }
const { title, description } = Astro.props;
---
<Layout title={title} description={description}>
  <slot name="header"><Header /></slot>
  <div class="mx-auto w-full max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
    <slot />
  </div>
  <slot name="footer"><Footer /></slot>
</Layout>
```

---

### 6. Home Page — Hero + Token Stream + Featured

**File:** `site/src/pages/index.astro`

```astro
---
import PageLayout from '../layouts/PageLayout.astro';
import { getCollection } from 'astro:content';

const tutorials = await getCollection('tutorials');
const featured = tutorials
  .filter(t => t.data.category !== 'General')
  .sort((a, b) => (b.data.date?.localeCompare(a.data.date || '') || 0))
  .slice(0, 6);
---

<PageLayout title="create-tutorials — Linux & Arch Guides" description="Curated Linux/Arch Linux tutorials, CLI references, and system administration guides.">
  <section class="hero-screen relative min-h-[70vh] flex items-center justify-center overflow-hidden px-6 pt-20 pb-16">
    <div class="token-stream absolute inset-0 -z-10" aria-hidden="true">
      <!-- Animated code snippets floating up -->
      {[
        '$ niri msg action move-window-left',
        '$ nmcli device wifi connect "SSID" password "pass"',
        '$ pacman -S --needed base linux linux-firmware',
        '$ systemctl enable --now sshd',
        '$ git clone git@github.com:user/repo.git',
        '$ nvim ~/.config/nvim/init.lua',
        '$ uv pip install -r requirements.txt',
        '$ docker compose up -d',
      ].map((line, i) => (
        <div class="session-lane absolute font-mono text-xs text-muted/30" style={{ top: `${10 + i * 10}%`, left: `${5 + (i % 3) * 10}%`, animationDelay: `-${i * 2}s` }}>
          <span class="session-prompt text-accent">$</span>{' '}{line}
        </div>
      ))}
    </div>

    <div class="relative z-10 mx-auto max-w-3xl text-center">
      <span class="eyebrow inline-block rounded-full bg-rule px-3 py-1 text-xs font-medium text-muted mb-6">Tutorial Collection</span>
      <h1 class="display text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight">
        Linux & Arch Guides for Developers
      </h1>
      <p class="mt-6 max-w-2xl mx-auto text-lg leading-relaxed text-muted">
        200+ battle-tested tutorials covering Arch installation, Niri window manager,
        NetworkManager, Neovim, Docker, and CLI workflows. Zero fluff, copy-paste ready.
      </p>
      <div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="/tutorials" class="btn-primary w-full sm:w-auto">
          Browse Tutorials
          <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="/categories" class="btn-secondary w-full sm:w-auto">Explore Categories</a>
      </div>
    </div>
  </section>

  <section class="border-t border-rule py-16" aria-labelledby="featured-heading">
    <div class="mx-auto max-w-3xl text-center mb-12">
      <h2 id="featured-heading" class="display text-3xl font-bold">Featured Tutorials</h2>
      <p class="mt-3 text-muted">Recently updated and most referenced guides</p>
    </div>
    <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
      {featured.map(t => (
        <article class="card group">
          <div class="flex items-start gap-2 mb-3">
            <span class="text-xs font-medium text-accent uppercase tracking-wider">{t.data.category}</span>
            <span class="text-xs text-muted ml-auto">{t.data.readingTime} min read</span>
          </div>
          <h3 class="display text-lg font-semibold group-hover:text-accent transition-colors">
            <a href={`/tutorials/${t.slug}`}>{t.data.title}</a>
          </h3>
          <p class="mt-2 text-sm text-muted line-clamp-2">{t.data.description}</p>
          <div class="mt-4 flex flex-wrap gap-1">
            {t.data.tags.slice(0, 3).map(tag => (
              <span class="rounded px-2 py-0.5 text-xs border border-rule text-muted">{tag}</span>
            ))}
          </div>
        </article>
      ))}
    </div>
    <div class="mt-10 text-center">
      <a href="/tutorials" class="btn-secondary">View All Tutorials →</a>
    </div>
  </section>

  <section class="border-t border-rule py-16" aria-labelledby="stats-heading">
    <h2 id="stats-heading" class="sr-only">Statistics</h2>
    <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
      <div>
        <p class="display text-4xl font-bold text-accent">{tutorials.length}</p>
        <p class="text-muted mt-1">Total Tutorials</p>
      </div>
      <div>
        <p class="display text-4xl font-bold text-accent">{[...new Set(tutorials.map(t => t.data.category))].length}</p>
        <p class="text-muted mt-1">Categories</p>
      </div>
      <div>
        <p class="display text-4xl font-bold text-accent">{[...new Set(tutorials.flatMap(t => t.data.tags))].length}</p>
        <p class="text-muted mt-1">Unique Tags</p>
      </div>
      <div>
        <p class="display text-4xl font-bold text-accent">{tutorials.reduce((a, b) => a + b.data.readingTime, 0)}</p>
        <p class="text-muted mt-1">Minutes of Reading</p>
      </div>
    </div>
  </section>
</PageLayout>

<style>
  .hero-screen { background: radial-gradient(ellipse at 50% 0%, var(--color-rule) 0%, transparent 70%); }
  .token-stream .session-lane { animation: token-stream 30s linear infinite; white-space: nowrap; }
  @keyframes token-stream { from { transform: translateY(100%); opacity: 0; } 10% { opacity: 0.3; } 90% { opacity: 0.3; } to { transform: translateY(-120%); opacity: 0; } }
</style>
```

---

### 7. Tutorial Index Page — Search + Filter

**File:** `site/src/pages/tutorials/index.astro`

```astro
---
import PageLayout from '../../layouts/PageLayout.astro';
import { getCollection } from 'astro:content';

const tutorials = await getCollection('tutorials');
const categories = [...new Set(tutorials.map(t => t.data.category))].sort();
const allTags = [...new Set(tutorials.flatMap(t => t.data.tags))].sort();
---

<PageLayout title="All Tutorials" description="Browse and search all Linux/Arch tutorials.">
  <header class="mb-12">
    <h1 class="display text-3xl sm:text-4xl font-bold">Tutorials</h1>
    <p class="mt-2 text-muted">{tutorials.length} guides — search, filter, learn.</p>
  </header>

  <div class="flex flex-col lg:flex-row gap-8">
    <aside class="lg:w-64 shrink-0">
      <div class="sticky top-24 space-y-6">
        <section>
          <h3 class="font-medium mb-3">Categories</h3>
          <ul class="space-y-1" id="category-filters">
            <li><label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" value="all" checked class="accent-accent" /> <span>All</span></label></li>
            {categories.map(c => (
              <li><label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" value={c} class="accent-accent" /> <span>{c}</span></label></li>
            ))}
          </ul>
        </section>
        <section>
          <h3 class="font-medium mb-3">Tags</h3>
          <div class="flex flex-wrap gap-1" id="tag-cloud">
            {allTags.map(tag => (
              <button type="button" class="tag-btn rounded px-2 py-0.5 text-xs border border-rule text-muted hover:border-accent hover:text-ink transition-colors" data-tag={tag}>{tag}</button>
            ))}
          </div>
        </section>
      </div>
    </aside>

    <section class="flex-1">
      <div class="mb-6">
        <label for="search" class="sr-only">Search tutorials</label>
        <div class="relative">
          <svg class="absolute left-3 top-1/2 -translate-y-1/2 size-5 text-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.3-4.3"/></svg>
          <input type="search" id="search" placeholder="Search by title, description, tags…" class="w-full rounded-lg border border-rule bg-canvas px-10 py-2.5 text-sm placeholder:text-muted focus:outline-none focus:border-accent focus:ring-1 focus:ring-accent" />
        </div>
      </div>
      <div id="results" class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {tutorials.map(t => (
          <article class="card group" data-category={t.data.category} data-tags={t.data.tags.join(',')}>
            <div class="flex items-start gap-2 mb-2">
              <span class="text-xs font-medium text-accent uppercase tracking-wider">{t.data.category}</span>
              <span class="text-xs text-muted ml-auto">{t.data.readingTime} min</span>
            </div>
            <h3 class="display text-lg font-semibold group-hover:text-accent transition-colors">
              <a href={`/tutorials/${t.slug}`}>{t.data.title}</a>
            </h3>
            <p class="mt-2 text-sm text-muted line-clamp-2">{t.data.description}</p>
            <div class="mt-3 flex flex-wrap gap-1">
              {t.data.tags.slice(0, 4).map(tag => (
                <span class="rounded px-2 py-0.5 text-xs border border-rule text-muted">{tag}</span>
              ))}
            </div>
          </article>
        ))}
      </div>
      <p id="no-results" class="hidden text-center text-muted py-12">No tutorials match your filters.</p>
    </section>
  </div>
</PageLayout>

<script is:inline>
  const search = document.getElementById('search');
  const categoryFilters = document.querySelectorAll('#category-filters input[type="checkbox"]');
  const tagButtons = document.querySelectorAll('.tag-btn');
  const cards = document.querySelectorAll('#results article');
  const noResults = document.getElementById('no-results');

  let activeCategories = ['all'];
  let activeTags = new Set();
  let searchTerm = '';

  function filter() {
    let visible = 0;
    cards.forEach(card => {
      const cats = card.dataset.category;
      const tags = card.dataset.tags.split(',');
      const text = card.textContent.toLowerCase();

      const catMatch = activeCategories.includes('all') || activeCategories.includes(cats);
      const tagMatch = activeTags.size === 0 || tags.some(t => activeTags.has(t));
      const searchMatch = !searchTerm || text.includes(searchTerm);

      const show = catMatch && tagMatch && searchMatch;
      card.classList.toggle('hidden', !show);
      if (show) visible++;
    });
    noResults.classList.toggle('hidden', visible > 0);
  }

  search.addEventListener('input', e => { searchTerm = e.target.value.toLowerCase(); filter(); });
  categoryFilters.forEach(cb => cb.addEventListener('change', () => {
    if (cb.value === 'all') {
      if (cb.checked) { categoryFilters.forEach(c => { c.checked = c === cb; }); activeCategories = ['all']; }
      else { cb.checked = true; }
    } else {
      document.querySelector('#category-filters input[value="all"]').checked = false;
      activeCategories = Array.from(categoryFilters).filter(c => c.checked).map(c => c.value);
      if (activeCategories.length === 0) { document.querySelector('#category-filters input[value="all"]').checked = true; activeCategories = ['all']; }
    }
    filter();
  }));
  tagButtons.forEach(btn => btn.addEventListener('click', () => {
    const tag = btn.dataset.tag;
    if (activeTags.has(tag)) { activeTags.delete(tag); btn.classList.remove('border-accent', 'text-ink', 'bg-accent/10'); }
    else { activeTags.add(tag); btn.classList.add('border-accent', 'text-ink', 'bg-accent/10'); }
    filter();
  }));
</script>
```

---

### 8. Tutorial Detail Page — `[slug].astro`

**File:** `site/src/pages/tutorials/[slug].astro`

```astro
---
import { getCollection, getEntryBySlug } from 'astro:content';
import PageLayout from '../../layouts/PageLayout.astro';
import { Markdown } from 'astro/components';

export async function getStaticPaths() {
  const tutorials = await getCollection('tutorials');
  return tutorials.map(t => ({ params: { slug: t.slug }, props: t }));
}

const { tutorial } = Astro.props;
const { title, date, author, category, tags, readingTime, headings, content } = tutorial.data;
---

<PageLayout title={title} description={content.slice(0, 160).replace(/[#*`]/g, '')}>
  <article class="max-w-4xl mx-auto">
    <header class="mb-8 pb-6 border-b border-rule">
      <div class="flex flex-wrap items-center gap-3 text-sm text-muted mb-3">
        <span class="rounded px-2 py-0.5 text-xs font-medium bg-accent/10 text-accent">{category}</span>
        {date && <time datetime={date}>{new Date(date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</time>}
        <span>·</span>
        <span>{readingTime} min read</span>
      </div>
      <h1 class="display text-3xl sm:text-4xl font-bold tracking-tight">{title}</h1>
      <p class="mt-3 text-muted">By {author}</p>
      <div class="mt-4 flex flex-wrap gap-1">
        {tags.map(tag => <span class="rounded px-2 py-0.5 text-xs border border-rule text-muted">{tag}</span>)}
      </div>
    </header>

    {headings.length > 1 && (
      <aside class="hidden lg:block lg:absolute lg:left-[-280px] lg:w-64 lg:pt-8">
        <nav class="sticky top-24 space-y-1" aria-label="Table of contents">
          <h4 class="text-xs font-medium uppercase tracking-wider text-muted mb-2">On this page</h4>
          <ul>
            {headings.map(h => (
              <li class="pl-{h.level * 2}"><a href={`#${h.slug}`} class="text-sm text-muted hover:text-ink transition-colors block py-0.5">{h.text}</a></li>
            ))}
          </ul>
        </nav>
      </aside>
    )}

    <div class="prose lg:max-w-none">
      <Markdown>{content}</Markdown>
    </div>

    <footer class="mt-12 pt-8 border-t border-rule">
      <a href="/tutorials" class="btn-secondary inline-flex items-center gap-2">
        <svg class="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        Back to Tutorials
      </a>
    </footer>
  </article>
</PageLayout>
```

---

### 9. Category & Tag Pages

**File:** `site/src/pages/categories/index.astro` — list all categories with counts.

**File:** `site/src/pages/categories/[category].astro` — filter tutorials by category.

**File:** `site/src/pages/tags/[tag].astro` — filter tutorials by tag.

(Pattern same as tutorial index; omit for brevity.)

---

### 10. 404 Page

**File:** `site/src/pages/404.astro`

```astro
---
import PageLayout from '../layouts/PageLayout.astro';
---
<PageLayout title="404 — Not Found">
  <div class="flex min-h-[60vh] items-center justify-center text-center">
    <div>
      <h1 class="display text-6xl font-bold text-accent">404</h1>
      <p class="mt-4 text-xl text-muted">Tutorial not found</p>
      <a href="/tutorials" class="btn-primary mt-6 inline-block">Browse Tutorials</a>
    </div>
  </div>
</PageLayout>
```

---

### 11. GitHub Actions Deploy Workflow

**File:** `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm, cache-dependency-path: site/package-lock.json }
      - name: Install dependencies
        run: npm ci
        working-directory: site
      - name: Build
        run: npm run build
        working-directory: site
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with: { path: site/dist }

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy
        id: deployment
        uses: actions/deploy-pages@v4
```

---

### 12. Repository Config for Pages

**File:** `site/public/CNAME` (optional — if custom domain)

```text
tutorials.yourdomain.com
```

**File:** `site/public/.nojekyll` — empty file (prevents Jekyll processing).

---

### 13. Verify Build & Deploy

```bash
cd /home/srhills/labs/experiments/create-tutorials/site
npm run build
# → dist/ created with index.html, tutorials/, categories/, tags/, 404.html
npx serve dist  # preview locally
```

**Push to GitHub:**

```bash
cd /home/srhills/labs/experiments/create-tutorials
git add site .github
git commit -m "feat: add Astro tutorial site with GitHub Pages deploy"
git push origin main
```

Then in GitHub repo settings → **Pages** → Source: **GitHub Actions**.

---

## Tests / Validation

| Task | Test Command | Expected |
|------|--------------|----------|
| Content pipeline | `npm run build:content` | `src/content/tutorials/_index.json` with 200+ entries |
| Dev server | `npm run dev` | Loads `localhost:4321` no errors |
| Build | `npm run build` | `dist/` generated, `index.html` present |
| Lint | `npx astro check` | No TypeScript errors |
| Links | `npx @astrojs/check-links dist` | No broken internal links |
| Mobile | Resize browser | Header collapses, grid stacks, TOC hidden |
| Theme toggle | Click sun/moon icon | `html.light` class toggles, persists in localStorage |
| Search | Type in search box | Cards filter in real-time |
| Category filter | Check checkboxes | Cards filter by category |
| Tag filter | Click tag pills | Cards filter by tag |

---

## Risks, Tradeoffs, Open Questions

1. **Frontmatter inconsistency** — Many `.md` files lack `Title:`/`Date:` fields. Pipeline falls back to first H2 or filename. *Mitigation:* Add `Title:`/`Date:` to top 20 files manually; script logs missing fields.
2. **Large content** — 200+ tutorials → `content` field in JSON duplicates markdown. *Tradeoff:* Acceptable for static build (~2 MB JSON). Alternative: store only `filePath` and read at render time (slower dev).
3. **GitHub Pages base path** — `base: '/create-tutorials/'` means local `npm run dev` serves at `/` but links resolve to `/create-tutorials/`. *Fix:* Use `import.meta.env.BASE_URL` in all `href` (Astro handles this in `<a>` but not in JS strings). Audit all programmatic links.
4. **No CMS** — Content updates require rebuild + push. *Acceptable* for tutorial repo.
5. **Search is client-side only** — Fuse.js loads all tutorials (~200 KB JSON). Fine for <500 tutorials.
6. **Fonts** — Self-hosted woff2 needed. Download from Google Fonts / GitHub releases.
7. **Images** — Tutorials may reference local images. Pipeline should copy `assets/` alongside markdown or rewrite paths.
8. **Syntax highlighting theme** — `github-dark` matches zro aesthetic. Verify with actual code blocks.

---

## Execution Order (for implementer)

1. Scaffold Astro + deps (Task 0)
2. Config + fonts + global styles (Tasks 1–2)
3. Content pipeline script + run (Task 3)
4. Content collection config (Task 4)
5. Layout components (Task 5)
6. Home page (Task 6)
7. Tutorial index + search/filter (Task 7)
8. Tutorial detail (Task 8)
9. Category/Tag pages (Task 9)
10. 404 (Task 10)
11. GitHub Actions workflow (Task 11)
12. Build, verify, push (Task 13)
13. Enable Pages in GitHub UI (manual)

---

## Deliverable

A working static site at `https://yididiel7.github.io/create-tutorials/` with:

- Dark-first design matching zro.moonmath.ai visual language
- Full-text search + category/tag filtering
- Responsive, accessible, fast (Astro island = zero JS by default)
- Auto-deploy on push to main