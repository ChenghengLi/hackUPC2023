<template>
    <div class="container-fluid">
      <div :id="carouselId" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div v-for="(slide, index) in slides" :key="index" :class="{active: index === currentSlide}" class="carousel-item">
            <img :src="slide.imageUrl" class="d-block w-100" alt="slide image">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{ slide.title }}</h5>
              <p>{{ slide.description }}</p>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#" :data-bs-target="`#${carouselId}`" data-bs-slide="prev" @click="prevSlide()">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </a>
        <a class="carousel-control-next" href="#" :data-bs-target="`#${carouselId}`" data-bs-slide="next" @click="nextSlide()">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </a>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import * as bootstrap from 'bootstrap';
  
  const slides = [
    {
      imageUrl: 'https://via.placeholder.com/800x400?text=Slide+1',
      title: 'Slide 1 Title',
      description: 'Slide 1 Description'
    },
    {
      imageUrl: 'https://via.placeholder.com/800x400?text=Slide+2',
      title: 'Slide 2 Title',
      description: 'Slide 2 Description'
    },
    {
      imageUrl: 'https://via.placeholder.com/800x400?text=Slide+3',
      title: 'Slide 3 Title',
      description: 'Slide 3 Description'
    }
  ];
  
  const carouselId = 'carousel-' + Math.floor(Math.random() * 1000);
  
  const currentSlide = ref(0);
  
  function nextSlide() {
    if (currentSlide.value < slides.length - 1) {
      currentSlide.value++;
    } else {
      currentSlide.value = 0;
    }
  }
  
  function prevSlide() {
    if (currentSlide.value > 0) {
      currentSlide.value--;
    } else {
      currentSlide.value = slides.length - 1;
    }
  }
  </script>
  
  <style>
  .carousel-item {
    height: 100%;
  }
  </style>