<template>
  <div class="background">
    <div :id="carouselId" class="carousel slide" data-bs-ride="carousel">
      
      <div class="carousel-inner">
        <div v-for="(slide, index) in slides" :key="index" :class="{ active: index === currentSlide }"
          class="carousel-item">

          <div v-if="slide.types === 'Summary'" >
            <SummaryComponent :summary="slide.content"></SummaryComponent>
          </div>
          <div v-else-if="slide.types === 'Loading'" style="padding-top: 50px;">
            <div style="text-align: center; font-size: 30px;">
              {{ slide.content }}
              <br>
              <br>
              <br>
              {{ slide.phrase }}
            </div>
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
    types: "Loading",
    content: "Loading datas\n\n\n\n\n\n\n\n",
    phrase: ""
  }
])

const phrases =["Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill","Believe you can and you're halfway there. - Theodore Roosevelt",  "Don't watch the clock; do what it does. Keep going. - Sam Levenson",  "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",  "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",  "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",  "Strive not to be a success, but rather to be of value. - Albert Einstein",  "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",  "Don't let yesterday take up too much of today. - Will Rogers",  "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle. - Steve Jobs"]
function choosePhrase() {
  const randomNum = Math.floor(Math.random() * phrases.length);
  slides.value[0].phrase = phrases[randomNum]

}

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
  choosePhrase()
  axios.get('/data/')
    .then((res) => {
      console.log(res.data);
      setSlides(res.data);
      datos.value = res.data
      console.log(slides.value);
      slides.value.shift()
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
    height: 2000px;
    overflow: hidden;
  }
}

@media only screen and (max-width: 767px) {
  /* Styles for mobile devices */
  .background {
    max-width: 100%;
    height: 900px;
    overflow: hidden;
  }
}
</style>