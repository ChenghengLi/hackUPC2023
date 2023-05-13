<template>
<div :class="clicked ? 'helloworld' : 'another'">
    {{ hello }}
</div>
<button @click="clickme"> I am a button</button>
</template>



<script setup>
import {ref} from 'vue' 

const hello = ref('hello world')
let clicked = ref(false)


const clickme = () => {
    hello.value = 'bye'
    clicked.value = !clicked.value
}

</script>


<style>

.helloworld {
    color: aqua;
}

.another {
    color: red;
}

</style>