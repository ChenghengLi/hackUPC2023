<template>
  <div>
    <button v-if="showButton" type="button" class="btn" @click="onClick">
      <img alt="upload the document here" src="../assets/upload.png" class="button-image">
      <input type="file" accept="application/pdf,application/vnd.ms-excel" ref="fileInput" style="display: none;" @change="handleFileUpload">
  </button>

    <FileComponent v-if="!showButton"/>
    <TextComponent v-if="!showButton"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import FileComponent from './FileComponent.vue';
import TextComponent from './TextComponent.vue';
import axios from 'axios'
const showButton = ref(true);

const onClick = () => {
  showButton.value = false;
}

const fileInput = ref(null)

function handleFileUpload(event) {
  const selectedFile = event.target.files[0]
  if (!selectedFile || selectedFile.type !== 'application/pdf') {
    alert('Please select a PDF file.')
    fileInput.value.value = ''
    return
  }else{
    const formData = new FormData()
    formData.append('file', selectedFile)
    
    // send the form data to the backend using axios
    axios.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(response => {
      console.log(response.data)
      // handle the response from the server here
    })
    .catch(error => {
      console.log(error)
      // handle any errors that occur here
    })
  }
  showButton.value = false;
}
</script>

<style>
.button-image{
  width: 300px;
  height: 250px;
}
</style>
