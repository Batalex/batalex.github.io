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
            <a class="text-4xl hover:text-wenge transition"
               href="mailto:alexandre.batisse@hey.com"
               target="_blank">
                <MailIcon class="h-12"/>
            </a>
            <a class="text-4xl hover:text-wenge transition" href="https://github.com/batalex"
               target="_blank">
                <gh class="h-12"/>
            </a>
            <a class="text-4xl hover:text-wenge transition" href="https://gitlab.com/abatisse"
               target="_blank">
                <gl class="h-12"/>
            </a>

        </div>
    </div>
</template>

<script setup>
import {MailIcon} from '@heroicons/vue/outline'

const gh = defineComponent({
    render: () =>
        h('svg', {
            fill: 'currentColor',
            viewBox: '0 0 24 24'
        }, [
            h('path', {
                d: 'M12 2C6.477 2 2 6.463 2 11.97c0 4.404 2.865 8.14 6.839 9.458.5.092.682-.216.682-.48 0-.236-.008-.864-.013-1.695-2.782.602-3.369-1.337-3.369-1.337-.454-1.151-1.11-1.458-1.11-1.458-.908-.618.069-.606.069-.606 1.003.07 1.531 1.027 1.531 1.027.892 1.524 2.341 1.084 2.91.828.092-.643.35-1.083.636-1.332-2.22-.251-4.555-1.107-4.555-4.927 0-1.088.39-1.979 1.029-2.675-.103-.252-.446-1.266.098-2.638 0 0 .84-.268 2.75 1.022A9.606 9.606 0 0112 6.82c.85.004 1.705.114 2.504.336 1.909-1.29 2.747-1.022 2.747-1.022.546 1.372.202 2.386.1 2.638.64.696 1.028 1.587 1.028 2.675 0 3.83-2.339 4.673-4.566 4.92.359.307.678.915.678 1.846 0 1.332-.012 2.407-.012 2.734 0 .267.18.577.688.48C19.137 20.107 22 16.373 22 11.969 22 6.463 17.522 2 12 2z',
            }),
        ]),
})
const gl = defineComponent({
    render: () =>
        h('svg', {
            fill: 'currentColor',
            viewBox: '0 0 380 380'
        }, [
            h('path', {
                d: 'M282.83,170.73l-.27-.69-26.14-68.22a6.81,6.81,0,0,0-2.69-3.24,7,7,0,0,0-8,.43,7,7,0,0,0-2.32,3.52l-17.65,54H154.29l-17.65-54A6.86,6.86,0,0,0,134.32,99a7,7,0,0,0-8-.43,6.87,6.87,0,0,0-2.69,3.24L97.44,170l-.26.69a48.54,48.54,0,0,0,16.1,56.1l.09.07.24.17,39.82,29.82,19.7,14.91,12,9.06a8.07,8.07,0,0,0,9.76,0l12-9.06,19.7-14.91,40.06-30,.1-.08A48.56,48.56,0,0,0,282.83,170.73Z',
            }),
        ]),
})
</script>
