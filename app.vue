<template>
    <div>
        <NuxtLayout>
            <NuxtPage/>
        </NuxtLayout>
    </div>
</template>

<script setup>
useHead({
    title: 'Alex Batisse',
    htmlAttrs: {
        lang: 'en'
    },
    meta: [
        { charset: 'utf-8' },
        {
            name: 'viewport',
            content: 'width=device-width, initial-scale=1'
        },
        {
            name: 'Alex Batisse\'s personnal page',
            content: 'Get to know me and my projects.'
        }
    ],
    link: [
        {
            rel: 'icon',
            type: 'image/svg+xml',
            href: '/hexagon.svg'
        }
    ]
})

</script>

<style>

html {
    font-family: 'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
    font-size: 16px;
    word-spacing: 1px;
    -ms-text-size-adjust: 100%;
    -webkit-text-size-adjust: 100%;
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    box-sizing: border-box;
}

</style>
