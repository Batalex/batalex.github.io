<template>
    <div class="mt-8">
        <div class="md:max-w-3xl">
            <TitleSection titleName="Projects"/>
            <p class="mt-6 text-lg text-olive-drab">
                I have worked on many little projects over the years but these are the ones that I’m most proud of.
                I hope this list will continue to grow in the future!
            </p>

        </div>
        <div class="mt-16 sm:mt-20 p-8">
            <ul class="grid grid-cols-1 gap-x-12 gap-y-16 sm:grid-cols-2 lg:grid-cols-3"
                role="list">

                <li v-for="project in projects"
                    :key="project.title" class="group relative flex flex-col items-start">
                    <div
                        class="relative z-10 flex h-12 w-12 items-center justify-center rounded-full bg-laurel-green shadow-md">
                        <span class="text-xl">{{ project.illustration }}</span></div>
                    <h2 class="mt-6 text-base font-semibold text-davys-grey">
                        <div
                            class="absolute -inset-y-6 -inset-x-4 z-0 scale-95 bg-dark-vanilla opacity-0 transition group-hover:scale-100 group-hover:opacity-100 sm:-inset-x-6 sm:rounded-2xl"></div>
                        <a :href="project.link"><span
                            class="absolute -inset-y-6 -inset-x-4 z-20 sm:-inset-x-6 sm:rounded-2xl"></span><span
                            class="relative z-10">{{ project.title }}</span></a></h2>
                    <p class="relative z-10 mt-2 text-sm text-wenge">
                        {{ project.content }}</p>
                    <p v-if="project.short"
                       class="relative z-10 mt-6 flex text-sm font-medium text-wenge transition group-hover:text-jet">
                        <LinkIcon class="h-4 w-4 flex-none"></LinkIcon>
                        <span class="ml-2">{{ project.short }}</span></p>
                </li>

            </ul>
        </div>
    </div>
</template>
<script setup>
import {LinkIcon} from "@heroicons/vue/24/solid";
import TitleSection from "./TitleSection.vue";

const projects = [
    {
        title: "To be announced",
        content: "This is something I have been working on for quite some time. I hope I can release it soon!",
        short: "fosstodon.org",
        link: "https://fosstodon.org/@batalex/109671714126269564",
        illustration: "❓"
    },
    {
        title: "pyOpenSci reviewer",
        content: "I am proud to have joined the community that supports free and open Python tools for processing scientific data.",
        short: "pyopensci.org",
        link: "#",
        illustration: "✔"
    },
    {
        title: 'Twitter campaign',
        content: 'I co-created a bot for a music promotional campaign. Over five days, the bot generated and served over 4,000 short videos and were among the top trending topics worldwide.'
        ,
        link: 'https://twitter.com/hacklazzcc',
        short: "twitter.com",
        illustration: "🤖"
    },
    {
        title: 'Effective Pandas Book',
        content: 'I am honored to be credited as a technical editor in this excellent book by Matt Harrison. This book presents the best practices for manipulating data with Pandas.',
        link: 'https://store.metasnake.com/effective-pandas-book',
        short: "metasnake.com",
        illustration: "📕"
    },
    {
        title: 'Camelia',
        content: 'I co-created Camelia, a platform combining audio analysis, video generation, and background workers to allow music artists to create videos quickly.',
        link: 'https://www.camelia.studio/',
        short: 'camelia.studio',
        illustration: "🎵"
    },
    {
        title: 'Personal website',
        content: 'This personal website was the perfect opportunity to take a shot at Nuxt & Tailwind.',
        short: "",
        link: "#",
        illustration: "🖼️"
    },
    {
        title: 'Scikit-learn Sprint of the Decade',
        content: 'I participated in a 3-days scikit-learn sprint in Jan. 2020. I met some lovely people there and contributed to one of the most essential packages in the PyData ecosystem.',
        link: 'https://scikit-learn.fondation-inria.fr/paris-sprint-of-the-decade-happy-birthday-scikit-learn/',
        short: 'scikit-learn.fondation-inria.fr',
        illustration: "👨‍💻"
    }
]
</script>
