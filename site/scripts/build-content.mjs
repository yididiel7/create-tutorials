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
      content,
    };

    fs.writeFileSync(path.join(OUT_DIR, `${item.slug}.json`), JSON.stringify(item, null, 2));
    index.push({ slug: item.slug, title: item.title, category: item.category, tags: item.tags, date: item.date, readingTime: item.readingTime, description: item.description });
  }

  fs.writeFileSync(path.join(OUT_DIR, '_index.json'), JSON.stringify(index, null, 2));
  console.log(`Built ${index.length} tutorials`);
}

main();