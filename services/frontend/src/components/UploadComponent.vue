<template> 
    <button type="button" class="btn" @click="handleButtonClick">
    <img alt="upload the document here" src="../assets/upload.png" class="button-image">
    <input type="file" accept="application/pdf,application/vnd.ms-excel" ref="fileInput" style="display: none;" @change="handleFileUpload">
  </button>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
const fileInput = ref(null)
const handleButtonClick = () => {
  // add your button click event handler code here
  fileInput.value.click()
}

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
}
</script>

<style>
.button-image{
    width: 300px;
    height: 250px;
}
</style>