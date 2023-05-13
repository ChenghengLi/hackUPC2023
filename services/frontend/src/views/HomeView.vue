<template>
  <div class="home full-screen-container d-flex flex-column justify-content-center">
    <TitleComponent></TitleComponent>
    <UploadComponent></UploadComponent>

  </div>
</template>

<script setup>
// @ is an alias to /src
import TitleComponent from '@/components/TitleComponent.vue'
import UploadComponent from '@/components/UploadComponent.vue';



</script>



<style scoped>
.home {
  position: relative;
  z-index: 1;
}

.home::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("../assets/background.jpeg");
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
  opacity: 0.2;
  z-index: -1;
}

.full-screen-container {
  height: 100vh;
  width: 100%;
  overflow-y: hidden;
}
</style>
