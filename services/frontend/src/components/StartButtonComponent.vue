<template>
    <div class="row justify-content-center align-items-center">
      <div class="col-md-6">

        <button class="btn btn-primary btn-style" @click="onClick">START</button>
      </div>
    </div>
  </template>
  
  <script setup>
  const onClick = () => {
    // Add your click event logic here
  };
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
    margin-top: 1rem; /* Add margin at the top */
    font-size: 2rem; /* Increase font size */
    font-weight: bold; /* Add bold font weight */
    text-transform: uppercase; /* Add uppercase text transformation */
    background-color: #007bff; /* Change background color to blue */
    border-color: #007bff; /* Change border color to blue */
    border-radius: 50px; /* Add border radius to make it round */
    padding: 1rem 2rem; /* Add padding */
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15); /* Add box shadow */
  }
  </style>
  