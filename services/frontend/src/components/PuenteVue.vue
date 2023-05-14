<template>
    <div display="none"></div>
</template>
<script setup>
import { defineProps, defineExpose, ref } from 'vue'


const props = defineProps({
    data: {
        type: Array,
        required: true
    }
})

const all_data = ref(props.data)
defineExpose({
  all_data
})

</script>