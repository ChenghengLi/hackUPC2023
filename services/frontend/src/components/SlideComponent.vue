<template>
    <div class="container-fluid">
      <div :id="carouselId" class="carousel slide" data-bs-ride="carousel">
        <ol class="carousel-indicators">
          <li v-for="(slide, index) in slides" :key="index" :data-bs-target="`#${carouselId}`" :data-bs-slide-to="index" :class="{active: index === currentSlide}"></li>
        </ol>
        <div class="carousel-inner">
          <div v-for="(slide, index) in slides" :key="index" :class="{active: index === currentSlide}" class="carousel-item">
            <img :src="slide.imageUrl" class="d-block w-100" alt="slide image">
            <div class="carousel-caption d-none d-md-block">
              <h5>{{ slide.title }}</h5>
              <p>{{ slide.description }}</p>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" :data-bs-target="`#${carouselId}`" data-bs-slide="prev" @click="prevSlide()">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" :data-bs-target="`#${carouselId}`" data-bs-slide="next" @click="nextSlide()">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
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
  
  let currentSlide = 0;
  
  function nextSlide() {
    if (currentSlide < slides.length - 1) {
      currentSlide++;
    } else {
      currentSlide = 0;
    }
  }
  
  function prevSlide() {
    if (currentSlide > 0) {
      currentSlide--;
    } else {
      currentSlide = slides.length - 1;
    }
  }
  </script>
  
  <style scoped>
  .carousel-item {
    height: 100vh;
  }
  </style>