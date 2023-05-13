<template>
    <div class="home full-screen-container d-flex flex-column justify-content-center">
      <QuestionComponent></QuestionComponent>
      <AnswerComponent></AnswerComponent>
    </div>
  </template>
  
  <script setup>
    import QuestionComponent from '@/components/QuestionComponent.vue'
    import AnswerComponent from '@/components/AnswerComponent.vue'
  </script>
  
  <style scoped>
    .full-screen-container {
      height: 100vh;
      width: 100%;
      overflow-y: hidden;
      clip-path: polygon(0 15%, 20% 0, 80% 0, 100% 15%, 100% 85%, 80% 100%, 20% 100%, 0 85%);
    }
  </style>
  