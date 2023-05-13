<template>
    <div class="row justify-content-center align-items-center">
      <div class="col-md-6">
        <h1 class="text-center file-name">{{ props.name }}</h1>
      </div>
    </div>
  </template>
  
  <script setup>
  // Add any logic or data properties here
  import {defineProps} from "vue"
  const props = defineProps({
    name: {
    type: String,
    default: ""
    }
  })
  </script>
  
  <style scoped>
  .file-name {
    font-size: 1.5rem;
  }
  </style>
  