<template>
    <div class="mt-8">
        <Title titleName="Projects"/>
        <div
            class="mt-16 flex lg:-mx-32 lg:px-2 flex-row gap-2 sm:gap-4 flex-wrap justify-center align-middle">
            <ProjectCard
                v-for="project in projects"
                :key="project.title"
                v-bind:project-spec="project"
            />

        </div>
    </div>
</template>
<script setup>

const projects = [
    {
        title: 'Twitter campaign',
        content: [
            'I co-created a Twitter bot to go with a music album release.',
            'Over five days we generated and served over 4,000 short videos and were among the top trending topics worldwide.'
        ],
        year: '2022',
        link: 'https://twitter.com/hacklazzcc',
        name: 'Twitter bot'
    },
    {
        title: 'Effective Pandas Book',
        content: [
            'I am honored to be credited as a technical editor in this excellent book by Matt Harrison.',
            'This book presents the best practices for manipulating data with Pandas.'
        ],
        year: '2021',
        link: 'https://store.metasnake.com/effective-pandas-book',
        name: 'Website'
    },
    {
        title: 'Camelia',
        content: [
            'The fastest and easiest way to create videos for your music.',
            'Camelia combines audio analysis, video generation and background workers in web services.',
            'I am a co-creator of Camelia.'],
        year: '2021',
        link: 'https://www.camelia.studio/',
        name: 'Website'
    },
    {
        title: 'Personal website',
        content: ['I had never been fond of front-end development. That is until I discovered what a modern stack looks like!', 'This personal website was the perfect opportunity to take a shot at Nuxt & Tailwind.'],
        year: '2021'
    },
    {
        title: 'Scikit-learn Sprint of the Decade',
        content: ['At the end of January 2020, I participated in a 3-days scikit-learn sprint. I met some lovely people there and contributed to one of the most essential packages in the PyData ecosystem.', 'My contributions were quite diverse: bug fixes, unit tests improvements & refactoring.'],
        year: '2020',
        link: 'https://scikit-learn.fondation-inria.fr/paris-sprint-of-the-decade-happy-birthday-scikit-learn/',
        name: 'Event website'
    }
]
</script>
