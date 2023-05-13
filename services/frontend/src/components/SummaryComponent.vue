<template>
    <div>
        {{ props.summary }}
    </div>
</template>


<script setup>
import {defineProps} from 'vue'
const props = defineProps ({
    summary:{
        type: String,
        default: ""
    }

}) 

</script>

<style scoped>

div {
    font-size: 30px;
    padding-top: 10px;
}
</style>