<template>
    <div
        class="bg-white sm:max-w-sm border border-indigo-100 overflow-hidden flex flex-col justify-start shadow-md rounded-lg divide-y divide-gray-200 hover:shadow-xl md:transition">
        <div class="px-4 py-5 sm:px-6">
            <h3 class="text-black text-lg md:text-xl font-bold tracking-normal">{{
                    projectSpec.title
                }}</h3>
            <span class="inline text-sm text-green-900">{{ projectSpec.year }}</span>

        </div>
        <div class="px-4 pb-4 pt-3 sm:px-6 text-md flex-grow">
            <p v-for="para in projectSpec.content" class="pt-2">{{ para }}</p>
        </div>
        <div v-if="projectSpec.link" class="px-4 py-4 sm:px-6 text-center">
            <a :href="projectSpec.link"
               class="text-green-500 external hover:underline"
               target="_blank">{{ projectSpec.name }}</a>
        </div>

    </div>
</template>
<script>
export default {
    props: ["projectSpec"],
}
</script>
