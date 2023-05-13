<template>
    <div class="row justify-content-center align-items-center">
      <div class="col-md-6">

        <button class=" btn btn-outline-primary btn-style" @click="onClick" :disabled="props.file === 0">START</button>
      </div>
    </div>
  </template>
  
  <script setup>
 
  import {defineProps} from 'vue'
  const onClick = () => {
    
  
  };

  const props = defineProps({
    file:{
      type: FormData,
      default: null
    }
  })
  </script>
  
  <style scoped>
  .title-style {
    color: #007bff; /* Change color to blue */
    font-size: 3rem; /* Increase font size */
    font-weight: bold; /* Add bold font weight */
    text-transform: uppercase; /* Add uppercase text transformation */
    font-family: 'Roboto', sans-serif; /* Use Roboto font */
  }
  
  .btn-style {
    border: 1px solid rgb(23, 134, 218);
    margin: 0 15px;
    width: 140px;
    height: 50px;
    border-radius: 20px;
    -webkit-border-radius: 20px;
    -moz-border-radius: 20px;
    -ms-border-radius: 20px;
    -o-border-radius: 20px;
    font-size: 15px;
    font-weight: bold;
    letter-spacing: .7px;
    background-image:linear-gradient(top, #ffffff33 1px, #ffffff00 1px, #0000001a 100%);
    box-shadow: 0 60px 12px -18px rgba(0,0,0,0.1), 0 60px -12px rgba(0,0,0,0.1);
    margin-bottom: 10px;
    animation: anime 1s infinite ease-in-out alternate;
    -webkit-animation: anime 1s infinite ease-in-out alternate;
    animation-delay: .3s;
  }

  @keyframes anime {
    100% {
      transform: tranlateY(20px);
      -webkit-transform: tranlateY(20px);
      -moz-transform: tranlateY(20px);
      -ms-transform: tranlateY(20px);
      -o-transform: tranlateY(20px);
      box-shadow:0 40px 10px -18px rgba(0,0,0,0.2), 0 40px 16px -12px rgba(0,0,0,0.2);
    }
  
  }
  </style>
  