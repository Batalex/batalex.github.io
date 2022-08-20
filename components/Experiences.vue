<template>
    <div class="mt-8 mx-auto md:max-w-3xl">
        <Title titleName="Experiences"/>
        <div class="py-8 mx-auto">
            <div v-for="(phase,index) in timeline" :key="index" class="mt-8 md:flex">
                <div class="w-48 font-bold text-wenge leading-8 tracking-normal ">
                    <span>{{ phase.startDate }} - </span>
                    <span v-if="index === 0">Current</span>
                    <span v-else>{{ phase.endDate }}</span>

                </div>
                <div class="md:max-w-lg lg:max-w-xl md:pl-8">
                    <h3 class="text-xl text-olive-drab font-bold pb-2 leading-8">{{ phase.firm }}</h3>
                    <div v-for="(sub,index) in phase.subPhases" :key="index"
                         class="text-normal md:text-lg"
                         v-bind:class="[index != 0  ? 'mt-4' : '']">
                        <h4 class="font-extrabold text-jet">{{ sub.title }}</h4>
                        <p class="text-jet">{{ sub.content }}</p>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>

const timeline = [
    {
        firm: 'HEVA',
        location: "Lyon (FR)",
        startDate: 'Jan. 2019',
        endDate: undefined,
        title: 'Data Scientist',
        subPhases: [
            {
                title: 'Data Scientist & Tech lead',
                content: 'I have taken on some additional responsibilities. Nowadays, I provide technical support for the entire firm and manage the evolution of our technical stack.',
                startDate: 'Nov. 2020'

            },
            {
                title: 'Data Scientist',
                content: 'My responsibilities are twofold. First, I conduct our clients\' (pharmaceutical industry) studies on national health claim data. This work involves data management, statistical modeling, and reporting with the PyData stack. Secondly, I tend to my team\'s internal tools as a maintainer and Python developer.',
                startDate: 'Jan. 2019'
            }
        ]

    },
    {
        firm: 'Worldline',
        location: "Lyon (FR)",
        startDate: 'Jan. 2017',
        endDate: 'Dec. 2018',
        title: 'Software Engineer',
        subPhases: [
            {
                title: 'Software Engineer',
                content: 'I was part of the Business Intelligence & Big Data team in charge of designing and building a production-ready data science platform for training and deploying models. I worked on several projects involving banking information (fraud detection, cheque recovery prediction) with full-fledged data scientists.',
                startDate: 'Jan. 2017'

            },
            {
                title: 'Engineering internship',
                content: 'I worked in the Business Development unit on a banking chatbot.\n',
                startDate: 'Jan. 2017'

            }
        ]

    }
]

export default {
    data () {
        return {
            timeline
        }
    }
}
</script>
