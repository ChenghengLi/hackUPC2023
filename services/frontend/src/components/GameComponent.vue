<template>
    <div class="question">{{ props.question }}</div>
    <button class="floating-button" :class="{'disable': acabat }" :style="{ bottom: buttonPosition.bottom, left: buttonPosition.left }" @click="correctButton">
      {{props.answer}}
    </button>
    <div v-for="(i,index) in props.wrongAnswer" :key="index">
      <button class="floating-button" :class="{'disable': acabat }" :style="{ bottom: wrongButtonPositions[index].bottom, left: wrongButtonPositions[index].left }" @click="wrongButton">
        {{i}}
      </button>
    </div>
    <div v-if="acabat">
        {{ description }}
      </div>
  </template>
  
  <script setup>
    
import { ref, onMounted } from 'vue';
  import { defineProps } from 'vue';
  import { defineEmits } from 'vue';

const emits = defineEmits(['childEvent']);

function handleClick(e) {
  const data = e;
  emits('childEvent', data);
}
  let description = ref("")
  let acabat = ref(false)
  const props = defineProps({
    question: {
      type: String,
      default: ''
    },
    answer: {
      type: String,
      default: ''
    },
    wrongAnswer: {
      type: Array,
      default: () => []
    }
  });

  const correctButton = () => {
    description = "You are correct!"
    acabat = true
    handleClick(true)

  }

  const wrongButton = () => {
    description = "You are wrong!"
    acabat = true
    handleClick(true)

  }
  const buttonPosition = ref({
    bottom: Math.floor(Math.random() * (window.innerHeight - 50)) + 'px',
    left: Math.floor(Math.random() * (window.innerWidth - 50)) + 'px'
  });
  
  const wrongButtonPositions = ref([]);
  for (let i = 0; i < props.wrongAnswer.length; i++) {
    wrongButtonPositions.value[i] = {
      bottom: Math.floor(Math.random() * (window.innerHeight - 50)) + 'px',
      left: Math.floor(Math.random() * (window.innerWidth - 50)) + 'px'
    };
  }
  
  const moveButton = () => {
    buttonPosition.value.bottom = parseInt(buttonPosition.value.bottom) - 3 + 'px';
    if (parseInt(buttonPosition.value.bottom) < -50) {
      buttonPosition.value.bottom = window.innerHeight + 'px';
      buttonPosition.value.left = Math.floor(Math.random() * (window.innerWidth - 50)) + 'px';
    }
    for (let i = 0; i < props.wrongAnswer.length; i++) {
      wrongButtonPositions.value[i].bottom = parseInt(wrongButtonPositions.value[i].bottom) - 3 + 'px';
      if (parseInt(wrongButtonPositions.value[i].bottom) < -50) {
        wrongButtonPositions.value[i].bottom = window.innerHeight + 'px';
        wrongButtonPositions.value[i].left = Math.floor(Math.random() * (window.innerWidth - 50)) + 'px';
      }
    }
  };
  
  onMounted(() => {
    setInterval(moveButton, 10);
  });
  </script>
  
  <style scoped>
  .question {
    font-size: 30px;
  }
  
  .floating-button {
    position: fixed;
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

  .disable {
    display :none;
  }
  </style>