<template>
    <div class="bg-pastel-gray overflow-hidden">
        <main>
            <div class="sm:px-8 mt-16 sm:mt-32">
                <div class="mx-auto max-w-7xl lg:px-8">
                    <div class="relative px-4 sm:px-8 lg:px-12">
                        <div class="mx-auto max-w-2xl lg:max-w-5xl">
                            <div
                                class="grid grid-cols-1 gap-y-16 lg:grid-cols-2 lg:grid-rows-[auto_1fr] lg:gap-y-12">
                                <div class="lg:pl-20">
                                    <div class="max-w-xs px-2.5 lg:max-w-none">
                                        <img alt=""
                                             class="aspect-square rotate-3 rounded-2xl object-cover"
                                             loading="lazy"
                                             src="~assets/alex.jpg"
                                             style="color: transparent;"
                                             width="200">
                                    </div>
                                </div>
                                <div class="lg:order-first lg:row-span-2">
                                    <h1
                                        class="text-4xl font-bold tracking-tight text-olive-drab sm:text-5xl">
                                        Hi, I am <span class="font-black text-jet">Alex</span>.
                                    </h1>
                                    <h2 class="text-3xl font-bold tracking-tight text-olive-drab sm:text-4xl">
                                        I am a data
                                        scientist & software engineer living in Lyon (FR)</h2>
                                    <div
                                        class="mt-6 space-y-7 text-lg text-olive-drab dark:text-zinc-400">
                                        <p>My manifold technical interests include software
                                            engineering, statistics, and data
                                            visualization.
                                            I try to cultivate a diverse set of skills.
                                            Thus, I feel just as confident writing a data
                                            preprocessing script, serving a model
                                            in a web server, or setting up a CI pipeline for unit
                                            tests.</p>
                                        <p>Technology watch makes a significant part of my typical
                                            day, as I like to be in
                                            touch with the latest Python or analytics tools news.
                                            I feel strongly about the FOSS mindset and contribute to
                                            the projects I like when I
                                            can.</p>
                                        <p>I majored with honors (M.Sc.Eng) in telecommunications in
                                            2017.</p>
                                    </div>
                                </div>


                                <div class="lg:pl-20">
                                    <ul role="list">
                                        <li v-for="link in links" :key=link.href class="flex mt-2">
                                            <a
                                                :href="link.href"
                                                class="group flex font-medium text-olive-drab transition hover:text-jet"
                                                target="_blank">
                                                <svg :viewBox="link.vbox"
                                                     aria-hidden="true"
                                                     class="h-6 w-6 flex-none fill-wenge transition group-hover:fill-jet">
                                                    <path :d="link.path_d"
                                                          clip-rule="evenodd"
                                                          fill-rule="evenodd"></path>
                                                </svg>
                                                <span class="ml-4">{{ link.text }}</span></a></li>

                                        <li class="mt-8 border-t border-laurel-green pt-8  flex">
                                            <a class="group flex font-medium text-olive-drab transition hover:text-jet"
                                               href="mailto:alexandre.batisse@hey.com">
                                                <EnvelopeIcon
                                                    class="h-6 w-6 flex-none text-wenge transition group-hover:text-jet"></EnvelopeIcon>
                                                <span
                                                    class="ml-4">alexandre.batisse@hey.com</span></a>
                                        </li>
                                    </ul>
                                    <div class="mt-6 flex">
                                        <a class="inline-flex items-center gap-2 justify-center rounded-md py-2 px-3 text-sm outline-offset-2 transition active:transition-none bg-transparent border border-davys-grey font-medium text-olive-drab hover:bg-wenge hover:text-pastel-gray active:bg-wenge active:text-pastel-gray group mt-6 mx-auto lg:w-full"
                                           href="/Resume_BATISSE.pdf" target="_blank">Download CV
                                            <ArrowDownIcon
                                                class="h-4 w-4 -translate-y-0.5 stroke-wenge transition group-active:stroke-pastel-gray group-hover:stroke-pastel-gray group-hover:translate-y-0"></ArrowDownIcon>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <div class="relative bg-pastel-gray overflow-hidden">
            <div class="max-w-7xl mx-auto relative px-4 py-8 sm:px-6 sm:pt-20 lg:pt-16 lg:px-32">
                <Experiences/>
                <Projects/>
            </div>
        </div>
    </div>

</template>

<script setup>
import {ArrowDownIcon, EnvelopeIcon} from "@heroicons/vue/20/solid";

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
        },
        {
            rel: 'stylesheet',
            href: 'https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;700;900&display=swap'
        }
    ]
})

const links = [
    {
        href: 'https://github.com/batalex',
        text: 'GitHub',
        path_d: 'M12 2C6.475 2 2 6.588 2 12.253c0 4.537 2.862 8.369 6.838 9.727.5.09.687-.218.687-.487 0-.243-.013-1.05-.013-1.91C7 20.059 6.35 18.957 6.15 18.38c-.113-.295-.6-1.205-1.025-1.448-.35-.192-.85-.667-.013-.68.788-.012 1.35.744 1.538 1.051.9 1.551 2.338 1.116 2.912.846.088-.666.35-1.115.638-1.371-2.225-.256-4.55-1.14-4.55-5.062 0-1.115.387-2.038 1.025-2.756-.1-.256-.45-1.307.1-2.717 0 0 .837-.269 2.75 1.051.8-.23 1.65-.346 2.5-.346.85 0 1.7.115 2.5.346 1.912-1.333 2.75-1.05 2.75-1.05.55 1.409.2 2.46.1 2.716.637.718 1.025 1.628 1.025 2.756 0 3.934-2.337 4.806-4.562 5.062.362.32.675.936.675 1.897 0 1.371-.013 2.473-.013 2.82 0 .268.188.589.688.486a10.039 10.039 0 0 0 4.932-3.74A10.447 10.447 0 0 0 22 12.253C22 6.588 17.525 2 12 2Z',
        vbox: "0 0 24 24"

    }, {
        href: 'https://gitlab.com/abatisse',
        text: 'GitLab',
        path_d: "M282.83,170.73l-.27-.69-26.14-68.22a6.81,6.81,0,0,0-2.69-3.24,7,7,0,0,0-8,.43,7,7,0,0,0-2.32,3.52l-17.65,54H154.29l-17.65-54A6.86,6.86,0,0,0,134.32,99a7,7,0,0,0-8-.43,6.87,6.87,0,0,0-2.69,3.24L97.44,170l-.26.69a48.54,48.54,0,0,0,16.1,56.1l.09.07.24.17,39.82,29.82,19.7,14.91,12,9.06a8.07,8.07,0,0,0,9.76,0l12-9.06,19.7-14.91,40.06-30,.1-.08A48.56,48.56,0,0,0,282.83,170.73Z",
        vbox: "0 0 380 380"
    }, {
        href: 'https://www.linkedin.com/in/alexandre-batisse-401578b4/',
        text: 'LinkedIn',
        path_d: "M18.335 18.339H15.67v-4.177c0-.996-.02-2.278-1.39-2.278-1.389 0-1.601 1.084-1.601 2.205v4.25h-2.666V9.75h2.56v1.17h.035c.358-.674 1.228-1.387 2.528-1.387 2.7 0 3.2 1.778 3.2 4.091v4.715zM7.003 8.575a1.546 1.546 0 01-1.548-1.549 1.548 1.548 0 111.547 1.549zm1.336 9.764H5.666V9.75H8.34v8.589zM19.67 3H4.329C3.593 3 3 3.58 3 4.297v15.406C3 20.42 3.594 21 4.328 21h15.338C20.4 21 21 20.42 21 19.703V4.297C21 3.58 20.4 3 19.666 3h.003z",
        vbox: "0 0 24 24"
    }

]

</script>

<style>
.external::after {
    content: "\00A0[↪]";
}
</style>
