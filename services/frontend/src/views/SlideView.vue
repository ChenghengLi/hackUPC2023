<template>
  <div class="container-fluid">
    <div :id="carouselId" class="carousel slide" data-bs-ride="carousel">
      
      <div class="carousel-inner">
        <div v-for="(slide, index) in slides" :key="index" :class="{ active: index === currentSlide }"
          class="carousel-item">

          <div v-if="slide.types === 'Summary'">
            <SummaryComponent :summary="slide.content"></SummaryComponent>
          </div>
          <div v-else>
            <GameComponent :question="slide.question" :answer="slide.answer" :wrong-answer="slide.wrongAnswer" @childEvent="getAcabat"></GameComponent>
          </div>
        </div>
        <img src="@/assets/background.jpeg" class="d-block w-100" alt="slide image">
      </div>
      <a class="carousel-control-next" :class="{ 'disable': slides[currentSlide].types !== 'Summary' && !acabarExercici }" href="#" :data-bs-target="`#${carouselId}`" data-bs-slide="next"
        @click="nextSlide()" >
        <span class="carousel-control-next-icon" :class="{ 'disable': slides[currentSlide].types !== 'Summary'  && !acabarExercici }" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </a>
      <button class="btn btn-outline-info backHome" @click="backHome">Back</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import * as bootstrap from 'bootstrap'
import SummaryComponent from '@/components/SummaryComponent.vue'
import GameComponent from '@/components/GameComponent.vue'

import { useRoute } from 'vue-router'

const route = useRoute()



const slides = ref([
  {
    types: "Summary",
    content: route.params.data
  },
  {
    types: "Game",
    question: "What is SO?",
    answer: "Operation System",
    wrongAnswer: ["Opera Song", "Open Source","Salty Ocean"]
  },
  {
    types: "Game",
    question: "What is difficult to collect, environmentally harmful to reprocess, often made of and contaminated by toxic materials, and not economical to recycle?",
    answer: "waste",
    wrongAnswer: ['Wasting', 'Precious Time', 'Spend']
  }
])

const carouselId = 'carousel-' + Math.floor(Math.random() * 1000)
const currentSlide = ref(0);
const acabarExercici = ref(false)

function nextSlide() {
  if (currentSlide.value < slides.value.length - 1) {
    currentSlide.value++;
    acabarExercici.value=false;
  }
}
const backHome = () => {
  router.push('/')
}
function getAcabat(data) {
  acabarExercici.value = data;
}
onMounted(() => {
  new bootstrap.Carousel(document.querySelector(`#${carouselId}`), {
    interval: 2000,
    keyboard: true,
    ride: false,
    pause: 'hover'
  });

  const carouselItems = document.querySelectorAll(`#${carouselId} .carousel-item`);
  carouselItems.forEach(item => {
    item.style.height = window.innerHeight + 'px'
  });
});
</script>

<style scoped>
.carousel-item {
  height: 100%
}

.disable {
  display: none
}

.backHome {
  background-color: rgb(144, 30, 167);
  border: 1px solid;
  margin:0 15px;
  width: 140px;
  height: 50px;
  border-radius: 20px;
  -moz-border-radius:20px;
  -o-border-radius: 20px;
  color:#fff;
  font-size: 15px;
  font-weight: bold

@media only screen and (max-width: 768px) {
  .backHome {
    font-size: 14px;
    padding: 8px 16px;
  }
}


</style>