<template>
    <div>
        <figure class="flex px-4 items-center sm:flex-col">
            <img alt="Young Alex" class="w-32 h-32 md:w-48 h-auto rounded-full mx-auto"
                 height="512" src="~assets/alex.jpg"
                 width="384">
            <div class="pl-4 text-left md:text-center md:pt-6 space-y-4">
                <figcaption class="font-medium">
                    <div class="text-jet text-lg md:text-2xl font-extrabold tracking-normal">
                        Alexandre Batisse
                    </div>
                    <div class="text-normal text-olive-drab md:text-xl">
                        <span class="font-bold text-jet">Data scientist & Tech lead</span> at HEVA
                    </div>
                </figcaption>
            </div>
        </figure>
        <div class="text-olive-drab text-normal max-w-3xl mx-auto md:text-lg py-4 md:py-8 lg:py-8">
            <p>
                My manifold technical interests include software engineering, statistics, and data
                visualization.
                I try to cultivate a diverse set of skills.
                Thus, I feel just as confident writing a data preprocessing script, serving a model
                in a web server, or setting up a CI pipeline for unit tests.
            </p>

            <p class="mt-2">
                Technology watch makes a significant part of my typical day, as I like to be in
                touch with the latest Python or analytics tools news.
                I feel strongly about the FOSS mindset and contribute to the projects I like when I
                can.
            </p>

            <p class="mt-2">
                I majored with honors (M.Sc.Eng) in telecommunications in 2017.
            </p>
        </div>

        <h2 class="text-2xl text-center text-jet font-extrabold tracking-normal sm:text-2xl lg:text-3xl">
            Get in touch</h2>
        <div
            class="flex grid-flow-col justify-between mx-auto max-w-sm md:max-w-md py-4 md:py-8 lg:py-8 text-jet">
            <a v-for="link in links" :key="link.href"
               :href="link.href"
               class="inline-flex items-center px-4 py-2 border-2 border-wenge shadow-sm text-base font-medium rounded-md text-wenge bg-transparent hover:bg-wenge hover:text-pastel-gray focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-wenge transition">
                {{ link.text }}
            </a>
        </div>
    </div>
</template>

<script setup>
const links = [
    {
        href: 'mailto:alexandre.batisse+site@hey.com',
        text: 'Mail'
    }, {
        href: 'https://github.com/batalex',
        text: 'GitHub'
    }, {
        href: 'https://gitlab.com/abatisse',
        text: 'GitLab'
    }, {
        href: '/Resume_BATISSE.pdf',
        text: 'CV'
    },
]
</script>
