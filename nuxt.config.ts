import {defineNuxtConfig} from 'nuxt'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    ssr: false,
    modules: ['@nuxtjs/tailwindcss'],
    hooks: {
        'vite:extendConfig'(config, {isClient}) {
            if (process.env.NODE_ENV !== 'development' && isClient) {
                config.build.rollupOptions.output.chunkFileNames = '_nuxt/[hash].js'
                config.build.rollupOptions.output.entryFileNames = '_nuxt/entry.[hash].js'
            }
        }
    },

})
