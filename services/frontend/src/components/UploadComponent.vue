<template>
  <div>
    <button type="button" class="btn" @click="handleButtonClick" v-if="showButton" style="border:none">
    <img alt="upload the document here" src="../assets/upload.png" class="button-image">
    <input type="file" accept="application/pdf" ref="fileInput" style="display: none;" @change="handleFileUpload">
  </button>

    <FileComponent v-if="!showButton" @click="cancelFile"/>
    <TextComponent v-if="!showButton" name="File uploaded successfully!"/>
    <StartButtonComponent :file="formData"/>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { inject } from "vue";

const axios = inject('axios');

import FileComponent from './FileComponent.vue'
import TextComponent from './TextComponent.vue'
import StartButtonComponent from '@/components/StartButtonComponent.vue'
const showButton = ref(true)
const formData = ref(null)
const selectedFile = ref("")
const fileInput = ref(null)
const handleButtonClick = () => {
  fileInput.value.click()
}
const cancelFile = () => {
  showButton.value = !showButton.value
}


function handleFileUpload(event) {
  selectedFile.value = event.target.files[0]
  console.log(selectedFile.value)
  if (!selectedFile.value || selectedFile.value.type !== 'application/pdf') {
    alert('Please select a PDF file.')
    fileInput.value.value = ''
    console.log("hola")
    return
  }else{
    console.log("hola2")
    showButton.value = false;
    formData.value = new FormData()
    formData.value.append('file', selectedFile.value)
    console.log("hola3")

    axios.post("/upload/", formData.value, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
      
    })
    .then(response => {
      console.log(response.data)
      console.log("horewrla4")
    })
    .catch(error => {
      console.log(error)
      console.log("hola43")
      showButton.value = true;
    })
    console.log("hola4")
  }
}
</script>

<style>
.button-image{
  width: 300px;
  height: 250px;
}
</style>
