<template>
  <div>
    <button type="button" class="btn" @click="handleButtonClick" v-if="showButton" style="border:none">
    <img alt="upload the document here" src="../assets/upload.png" class="button-image">
    <input type="file" accept="application/pdf,application/vnd.ms-excel" ref="fileInput" style="display: none;" @change="handleFileUpload">
  </button>

    <FileComponent v-if="!showButton" @click="cancelFile"/>
    <TextComponent v-if="!showButton" name="File uploaded successfully!"/>
    <StartButtonComponent :file="formData"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import FileComponent from './FileComponent.vue';
import TextComponent from './TextComponent.vue';
import StartButtonComponent from '@/components/StartButtonComponent.vue'
const showButton = ref(true);
const formData = ref(null)
const selectedFile = ref("")
const fileInput = ref(null)
const handleButtonClick = () => {
  // add your button click event handler code here
  fileInput.value.click()
}
const cancelFile = () => {
  showButton.value = !showButton.value
}


function handleFileUpload(event) {
  selectedFile.value = event.target.files[0]
  if (!selectedFile.value || selectedFile.value.type !== 'application/pdf') {
    alert('Please select a PDF file.')
    fileInput.value.value = ''
    return
  }else{
    showButton.value = false;
    formData.value = new FormData()
    formData.value.append('file', selectedFile)
  }
}
</script>

<style>
.button-image{
  width: 300px;
  height: 250px;
}
</style>
