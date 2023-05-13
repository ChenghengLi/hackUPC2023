<template>
  <div>
    <button v-if="showButton" type="button" class="btn" @click="onClick">
      <img alt="upload the document here" src="../assets/upload.png" class="button-image">
    </button>

    <FileComponent v-if="!showButton"/>
    <TextComponent v-if="!showButton"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import FileComponent from './FileComponent.vue';
import TextComponent from './TextComponent.vue';

const showButton = ref(true);

const onClick = () => {
  showButton.value = false;
}
</script>

<style>
.button-image{
  width: 300px;
  height: 250px;
}
</style>
