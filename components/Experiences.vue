<template>
    <div>
        <Title titleName="Experiences" />

        <p class="text-black text-xl py-4 md:py-8 lg:py-16">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ac finibus diam.
            Nulla in feugiat libero, vitae feugiat dolor. Phasellus eleifend, mauris at egestas
            pharetra, urna elit pellentesque nunc, eget scelerisque arcu neque quis risus. Donec
            quam diam, accumsan non finibus quis, dictum eu orci. Suspendisse auctor, velit nec
            sollicitudin gravida, massa felis congue augue, vel bibendum tortor urna at ex. Cras
            accumsan dui at ligula rhoncus pretium. Fusce semper leo sit amet purus euismod
            tincidunt. Nam ultricies ante sit amet tempor cursus. Quisque sit amet sapien in tortor
            ultricies tempor. Nunc rutrum mauris ac diam pharetra, id pharetra nisl mollis. Donec
            sed enim et magna accumsan egestas eu eu neque. Vestibulum porta est nisi, non egestas
            dolor auctor quis. Nunc iaculis neque sem.

        </p>
        <div class="flow-root hidden">
            <ul class="-mb-8">
                <li v-for="(event, eventIdx) in timeline" :key="event.id">
                    <div class="relative pb-8">
                        <span v-if="(eventIdx !== timeline.length - 1)"
                              class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                              aria-hidden="true"/>
                        <div class="relative flex space-x-3">
                            <div>
              <span
                  :class="[event.iconBackground, 'h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white']">
<!--                <component :is="event.icon" class="h-5 w-5 text-white" aria-hidden="true"/>-->
              </span>
                            </div>
                            <div class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-4">
                                <div>
                                    <p class="text-sm text-gray-500">
                                        {{ event.content }} <a :href="event.href"
                                                               class="font-medium text-gray-900">{{
                                            event.target
                                        }}</a>
                                    </p>
                                </div>
                                <div class="text-right text-sm whitespace-nowrap text-gray-500">
                                    <time :datetime="event.datetime">{{ event.date }}</time>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
const timeline = [
    {
        id: 1,
        content: 'Applied to',
        target: 'Front End Developer',
        href: '#',
        date: 'Sep 20',
        datetime: '2020-09-20',
        // icon: UserIcon,
        iconBackground: 'bg-gray-400',
    },
    {
        id: 2,
        content: 'Advanced to phone screening by',
        target: 'Bethany Blake',
        href: '#',
        date: 'Sep 22',
        datetime: '2020-09-22',
        // icon: ThumbUpIcon,
        iconBackground: 'bg-blue-500',
    },
    {
        id: 3,
        content: 'Completed phone screening with',
        target: 'Martha Gardner',
        href: '#',
        date: 'Sep 28',
        datetime: '2020-09-28',
        // icon: CheckIcon,
        iconBackground: 'bg-green-500',
    },
    {
        id: 4,
        content: 'Advanced to interview by',
        target: 'Bethany Blake',
        href: '#',
        date: 'Sep 30',
        datetime: '2020-09-30',
        // icon: ThumbUpIcon,
        iconBackground: 'bg-blue-500',
    },
    {
        id: 5,
        content: 'Completed interview with',
        target: 'Katherine Snyder',
        href: '#',
        date: 'Oct 4',
        datetime: '2020-10-04',
        // icon: CheckIcon,
        iconBackground: 'bg-green-500',
    },
]

export default {
    data() {
        return {
            timeline,
        }
    },
}
</script>
