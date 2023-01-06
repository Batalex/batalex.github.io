<template>
    <h1 class="text-4xl text-olive-drab font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
        {{ titleName }}
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
