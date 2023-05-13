<template>
  <div>
    <button type="button" class="btn" @click="handleButtonClick" v-if="showButton" style="border:none">
    <img alt="upload the document here" src="../assets/upload.png" class="button-image">
    <input type="file" accept="application/pdf" ref="fileInput" style="display: none;" @change="handleFileUpload">
  </button>

    <FileComponent v-if="!showButton" @click="cancelFile"/>
    <TextComponent v-if="!showButton" name="File uploaded successfully!"/>
    <StartButtonComponent :file="formData"/>

    <div class="row justify-content-center align-items-center">
      <div class="col-md-6">

        <button class="btn btn-outline-primary btn-style" @click="onClick" :disabled="formData === null">START</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { inject } from "vue";
import FileComponent from './FileComponent.vue'
import TextComponent from './TextComponent.vue'

const axios = inject('axios');
import { useRouter } from 'vue-router'
const router = useRouter()


const msg = ref("")
const toGame = () => {
  router.push({ path: '/slide',
    name: 'slide', params: { QandA: msg.value }})
}

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



  const onClick = () => {
    console.log("starte")
    axios.get('/data/')
    .then((res) => {
      console.log(res.data)
      msg.value = res.data;
      
    })
    .catch((error) => {
      console.log("err")
      console.error(error);
    });
    console.log(msg.value)
    console.log("starte2")
    toGame()
  };



function handleFileUpload(event) {
  selectedFile.value = event.target.files[0]
  console.log(selectedFile.value)
  if (!selectedFile.value || selectedFile.value.type !== 'application/pdf') {
    alert('Please select a PDF file.')
    fileInput.value.value = ''

    return
  }else{
    console.log("hola2")
    showButton.value = false;
    formData.value = new FormData()
    formData.value.append('pdf_file', selectedFile.value)


    axios.post("/upload/", formData.value, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
      
    })
    .then(response => {
      console.log(response.data)

    })
    .catch(error => {
      console.log(error)
      showButton.value = true;
    })

  }
}
</script>

<style>
.button-image{
  width: 300px;
  height: 250px;
}

.title-style {
    color: #007bff; /* Change color to blue */
    font-size: 3rem; /* Increase font size */
    font-weight: bold; /* Add bold font weight */
    text-transform: uppercase; /* Add uppercase text transformation */
    font-family: 'Roboto', sans-serif; /* Use Roboto font */
  }
  
  .btn-style {
    margin-top: 1rem; /* Add margin at the top */
    font-size: 2rem; /* Increase font size */
    font-weight: bold; /* Add bold font weight */
    text-transform: uppercase; /* Add uppercase text transformation */
    border-radius: 50px; /* Add border radius to make it round */
    padding: 1rem 2rem; /* Add padding */
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15); /* Add box shadow */
  }
</style>
