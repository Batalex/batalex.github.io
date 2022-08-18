<template>
    <div class="bg-white overflow-hidden">
        <Hero/>
        <div class="relative bg-white overflow-hidden">
            <div class="hidden lg:block lg:absolute lg:inset-y-0 lg:h-full lg:w-full">
                <div aria-hidden="true" class="relative h-full text-lg max-w-prose mx-auto">
                    <svg class="absolute top-12 left-full transform translate-x-32" fill="none"
                         height="384" viewBox="0 0 404 384" width="404">
                        <defs>
                            <pattern id="74b3fd99-0a6f-4271-bef2-e80eeafdf357" height="20"
                                     patternUnits="userSpaceOnUse"
                                     width="20" x="0" y="0">
                                <rect class="text-gray-200" fill="currentColor" height="4" width="4"
                                      x="0"
                                      y="0"/>
                            </pattern>
                        </defs>
                        <rect fill="url(#74b3fd99-0a6f-4271-bef2-e80eeafdf357)" height="384"
                              width="404"/>
                    </svg>
                    <svg
                        class="absolute top-1/2 right-full transform -translate-y-1/2 -translate-x-32"
                        fill="none" height="384" viewBox="0 0 404 384" width="404">
                        <defs>
                            <pattern id="f210dbf6-a58d-4871-961e-36d5016a0f49" height="20"
                                     patternUnits="userSpaceOnUse"
                                     width="20" x="0" y="0">
                                <rect class="text-gray-200" fill="currentColor" height="4" width="4"
                                      x="0"
                                      y="0"/>
                            </pattern>
                        </defs>
                        <rect fill="url(#f210dbf6-a58d-4871-961e-36d5016a0f49)" height="384"
                              width="404"/>
                    </svg>
                    <svg class="absolute bottom-12 left-full transform translate-x-32" fill="none"
                         height="384" viewBox="0 0 404 384" width="404">
                        <defs>
                            <pattern id="d3eb07ae-5182-43e6-857d-35c643af9034" height="20"
                                     patternUnits="userSpaceOnUse"
                                     width="20" x="0" y="0">
                                <rect class="text-gray-200" fill="currentColor" height="4" width="4"
                                      x="0"
                                      y="0"/>
                            </pattern>
                        </defs>
                        <rect fill="url(#d3eb07ae-5182-43e6-857d-35c643af9034)" height="384"
                              width="404"/>
                    </svg>
                </div>
            </div>
            <div class="max-w-7xl mx-auto relative px-4 py-8 sm:px-6 sm:pt-24 lg:pt-20 lg:px-32">
                <About/>
                <Experiences/>
                <Projects/>
            </div>
        </div>
        <footer class="bg-white">
            <div
                class="text-left max-w-7xl mx-auto relative px-4 pt-8 pb-2 sm:px-6 sm:pt-12 lg:pt-16 lg:px-32">

                <p class=" text-base text-gray-400">
                    Photo by <a class="text-green-500 external hover:underline"
                                href="https://unsplash.com/@stayhome"
                                target="_blank">Alena Stepanova</a>.
                </p>
            </div>
        </footer>
    </div>

</template>

<script setup>
useHead({
    title: 'Alex Batisse',
    htmlAttrs: {
        lang: 'en'
    },
    meta: [
        {charset: 'utf-8'},
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

.external::after {
    content: "\00A0[↪]";
}

</style>
