<template>
  <div class="background">
    <div :id="carouselId" class="carousel slide" data-bs-ride="carousel">
      
      <div class="carousel-inner">
        <div v-for="(slide, index) in slides" :key="index" :class="{ active: index === currentSlide }"
          class="carousel-item">

          <div v-if="slide.types === 'Summary'" style="display:flex align-items: center justify-content:center">
            <SummaryComponent :summary="slide.content"></SummaryComponent>
          </div>
          <div v-else>
            <GameComponent :question="slide.question" :answer="slide.answer" :wrong-answer="slide.wrongAnswer" @childEvent="getAcabat"></GameComponent>
          </div>
        </div>
      </div>
      <a class="carousel-control-next" :class="{ 'disable': slides[currentSlide].types !== 'Summary' && !acabarExercici }" href="#" :data-bs-target="`#${carouselId}`" data-bs-slide="next"
        @click="nextSlide()" >
        <span class="carousel-control-next-icon" :class="{ 'disable': slides[currentSlide].types !== 'Summary'  && !acabarExercici }" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </a>
      <button class="btn btn-outline-dark backHome" @click="backHome">Back</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, inject } from 'vue'
import * as bootstrap from 'bootstrap'
import SummaryComponent from '@/components/SummaryComponent.vue'
import GameComponent from '@/components/GameComponent.vue'

const axios = inject('axios');
const datos = ref(null);
import { useRouter } from 'vue-router'

const router = useRouter()

const slides = ref([
  {
    types: "Summary",
    content: "Loading datas"
  }
])

console.log(datos.value)


function setSlides(datos) {

 
    slides.value.push({
      types: "Summary",
      content: datos.topic
    })
    console.log(Object.keys(datos.question).length)
    for (let i = 0; i < Object.keys(datos.question).length; i++) {
    
      slides.value.push({
      types: "Games",
      question: datos.question[i].question,
      answer: datos.question[i].answer,
      wrongAnswer: datos.question[i].options
    })

}
}


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

  alert("Loading the summaries please wait a few seconds")

  axios.get('/data/')
    .then((res) => {
      console.log(res.data);
      setSlides(res.data);
      datos.value = res.data
      console.log(slides.value);

      const carouselItems = document.querySelectorAll(`#${carouselId} .carousel-item`);
      carouselItems.forEach(item => {
      item.style.height = window.innerHeight + 'px'
  })
    
    })
    .catch((error) => {
      console.error(error);
    })

  
  
  new bootstrap.Carousel(document.querySelector(`#${carouselId}`), {
    interval: 2000,
    keyboard: true,
    ride: false,
    pause: 'hover'
  })

  



  





})
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
  font-weight: bold;
  position: fixed;
  bottom: 0;
  left: 0;
  padding: 12px 24px;
  color: white;
  font-size: 16px;
  border: none;
  outline: none;
  cursor: pointer;
  font-weight: bold;
  margin-left: 30px;
  margin-bottom: 20px;
}

@media only screen and (max-width: 768px) {
  .backHome {
    font-size: 14px;
    padding: 8px 16px;
  }
}

.background {
  background-image: url("../assets/purple.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}


@media only screen and (min-width: 768px) {
  /* Styles for laptops and desktops */
  .background {
    max-width: 100%;
    height: 100%;
  }
}

@media only screen and (max-width: 767px) {
  /* Styles for mobile devices */
  .background {
    max-width: 100%;
    height: 900px;
  }
}
</style>