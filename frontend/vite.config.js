import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Custom config that should work with Render
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
  },
  // Fix for build errors
  build: {
    commonjsOptions: {
      transformMixedEsModules: true,
    },
  }
})