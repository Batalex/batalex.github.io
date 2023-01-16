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
                                    <div class="px-2.5 lg:max-w-none"
                                    >
                                        <div class="relative flex justify-center lg:justify-start">
                                            <div class="absolute z-0 hidden md:block">
                                                <svg id="blobSvg"
                                                     class="h-[300px] lg:-translate-x-20 -translate-y-20"
                                                     version="1.1"
                                                     viewBox="0 0 500 500"
                                                     xmlns="http://www.w3.org/2000/svg"
                                                >
                                                    <defs>
                                                        <linearGradient id="gradient" x1="0%"
                                                                        x2="0%" y1="0%" y2="100%">
                                                            <stop offset="0%"
                                                                  style="stop-color: #4E4B42;"></stop>
                                                            <stop offset="100%"
                                                                  style="stop-color: #363636;"></stop>
                                                        </linearGradient>
                                                    </defs>
                                                    <path id="blob" fill="url(#gradient)">
                                                        <animate attributeName="d" dur="25000ms"
                                                                 repeatCount="indefinite"
                                                                 values="M440.5,320.5Q418,391,355.5,442.5Q293,494,226,450.5Q159,407,99,367Q39,327,31.5,247.5Q24,168,89,125.5Q154,83,219.5,68Q285,53,335.5,94.5Q386,136,424.5,193Q463,250,440.5,320.5Z;M453.78747,319.98894Q416.97789,389.97789,353.96683,436.87838Q290.95577,483.77887,223.95577,447.43366Q156.95577,411.08845,105.64373,365.97789Q54.33169,320.86732,62.67444,252.61056Q71.01719,184.3538,113.01965,135.21007Q155.02211,86.06634,220.52211,66.46683Q286.02211,46.86732,335.5,91.94472Q384.97789,137.02211,437.78747,193.51106Q490.59704,250,453.78747,319.98894Z;M411.39826,313.90633Q402.59677,377.81265,342.92059,407.63957Q283.24442,437.46649,215.13648,432.5428Q147.02853,427.61911,82.23325,380.9572Q17.43796,334.29529,20.45223,250.83809Q23.46649,167.38089,82.5856,115.05707Q141.70471,62.73325,212.19045,63.73015Q282.67618,64.72705,352.67308,84.79839Q422.66998,104.86972,421.43486,177.43486Q420.19974,250,411.39826,313.90633Z;M440.5,320.5Q418,391,355.5,442.5Q293,494,226,450.5Q159,407,99,367Q39,327,31.5,247.5Q24,168,89,125.5Q154,83,219.5,68Q285,53,335.5,94.5Q386,136,424.5,193Q463,250,440.5,320.5Z;"></animate>
                                                    </path>
                                                </svg>
                                            </div>
                                            <img alt=""
                                                 class=" rotate-3 rounded-2xl"
                                                 loading="lazy"
                                                 src="~assets/alex.jpeg"
                                                 style="color: transparent;"
                                                 width="150">
                                        </div>
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
                                        class="mt-6 space-y-7 text-lg text-olive-drab">
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

                                <div class="z-20 mt-4 lg:pl-20">
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

</style>
