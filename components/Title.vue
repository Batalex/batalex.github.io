<template>
    <h1 class="text-4xl text-black font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
            <span class="inline relative">
                {{ titleName }}
                <span
                    class="absolute inset-0 mix-blend-multiply bg-green-400 transform scale-y-25 translate-y-5 z-0">
                </span>
            </span>

    </h1>
</template>
<script>
export default {
    props: {
        titleName: {
            type: String,
            required: true
        }
    }
}
</script>
