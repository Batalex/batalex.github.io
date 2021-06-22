<template>
    <a href="mailto:alexandre.batisse@hey.com" class="text-6xl hover:text-green-400">
        <font-awesome-icon  icon="envelope"/>
    </a>

</template>
<script>
export default {
    props: {
        iconName: {
            type: String,
            required: false
        },
        externalLink: {
            type: String,
            required: false
        }
    }
}
</script>
