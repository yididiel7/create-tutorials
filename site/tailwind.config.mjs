/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        arch: {
          bg: '#0F141C',
          surface: '#171D27',
          border: '#2A3444',
          cyan: '#1793D1',
          sky: '#38BDF8',
          text: '#E2E8F0',
          muted: '#94A3B8',
          terminal: '#0D1117',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
        display: ['Instrument Sans', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};