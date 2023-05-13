<template> 
    <button type="button" class="btn" @click="handleButtonClick">
    <img alt="upload the document here" src="../assets/upload.png" class="button-image">
  </button>
</template>

<script setup>

const handleButtonClick = () => {
  // add your button click event handler code here
  window.alert('Button clicked!');
}
</script>

<style>
.button-image{
    width: 300px;
    height: 250px;
}
</style>