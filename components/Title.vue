<template>
    <h1 class="text-4xl text-jet font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
        <span class="underline decoration-8 decoration-jet">{{ titleName }}</span>
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
