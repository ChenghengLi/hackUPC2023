<template>
  <div class="home">
    <TitleComponent></TitleComponent>
    <img alt="Vue logo" src="../assets/logo.png">
    <StartButtonComponent></StartButtonComponent>
    <HelloWorld msg="Welcome to Your Vue.js App"/>

    

  </div>
</template>

<script setup>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TitleComponent from '@/components/TitleComponent.vue'
import StartButtonComponent from '@/components/StartButtonComponent.vue'


</script>
