<template> 
    <button type="button" class="btn" @click="handleButtonClick">
    <img alt="upload the document here" src="../assets/upload.png" class="button-image">
    <input type="file" ref="fileInput" style="display: none;" @change="handleFileUpload">
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
    formData.append('pdf', selectedFile)
    
    const path = 'http://localhost:8080/upload/'
    // send the form data to the backend using axios
    axios.post(path, formData, {
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
  // do something with the selected files
}
</script>

<style>
.button-image{
    width: 300px;
    height: 250px;
}
</style>