import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Simple, minimal configuration to ensure build works
export default defineConfig({
  plugins: [vue()],
  server: {
    port: process.env.PORT || 5173,
    proxy: {
      '/api': {
        target: process.env.VITE_API_URL || 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})