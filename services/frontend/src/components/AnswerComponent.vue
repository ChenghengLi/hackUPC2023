<!-- <template>
  <div style="height:1000px">
    <button id="floating-btn" class="btn-btn-outline-primary">{{props.answer}}</button>
  </div>


</template>
  
<script setup>
  import {defineProps} from 'vue'
const props = defineProps ({
    answer: {
        type: String,
        default: ""
    }
}) 
</script>
  
<style scoped>

#floating-btn {
  position: fixed;
  bottom: 0;
  right: 50px;
  transform: translateY(100%);
  opacity: 0;
  animation-name: floating;
  animation-duration: 10s;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  animation-fill-mode: forwards; /* Add this line */
}

@keyframes floating {
  0% {
    transform: translateY(100%);
    opacity: 0;
  }
  10% {
    transform: translateY(-50%);
    opacity: 1;
  }
  90% {
    transform: translateY(-50%);
    opacity: 1;
  }
  100% {
    transform: translateY(-100%);
    opacity: 0;
  }
}
</style> -->

<template>
  <div>
    <button v-if="showButton" class="floating-button" @click="onClick">{{ buttonText }}</button>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const buttonText = 'Click Me';
const showButton = ref(true);
let x = ref(0)
let y = ref(0)
const getRandomPosition = () => {
  x.value = Math.floor(Math.random() * window.innerWidth);
  y.value = Math.floor(Math.random() * window.innerHeight);
}

const moveButton = () => {
  getRandomPosition();
  setInterval(moveButton, 1000);
};

const onClick = () => {
  showButton.value = false;
};

onMounted(() => {
  moveButton();
  const timeoutId = setTimeout(() => {
    showButton.value = false;
    clearInterval(x.value, y.value);
  }, 5000);

  onUnmounted(() => {
    clearInterval(x.value, y.value);
    clearTimeout(timeoutId);
  });
});
</script>

<style scoped>
.floating-button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 50%;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}

.floating-button:hover {
  background-color: #0062cc;
}
</style>