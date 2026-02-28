import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  base: '/gensoftworks/',
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        capture: resolve(__dirname, 'capture.html'),
      },
    },
  },
});
