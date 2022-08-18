<template>
    <div
        class="sm:max-w-sm border border-wenge overflow-hidden flex flex-col justify-start rounded-lg divide-y divide-laurel-green ">
        <div class="px-4 py-5 sm:px-6">
            <h3 class="text-jet text-lg md:text-xl font-bold tracking-normal">{{
                    projectSpec.title
                }}</h3>
            <span class="inline text-sm text-wenge">{{ projectSpec.year }}</span>

        </div>
        <div class="px-4 pb-4 pt-3 sm:px-6 text-md text-jet flex-grow">
            <p v-for="para in projectSpec.content" class="pt-2">{{ para }}</p>
        </div>
        <div v-if="projectSpec.link" class="px-4 py-4 sm:px-6 text-center">
            <a :href="projectSpec.link"
               class="text-jet external hover:underline"
               target="_blank">{{ projectSpec.name }}</a>
        </div>

    </div>
</template>
<script>
export default {
    props: ['projectSpec'],
}
</script>
