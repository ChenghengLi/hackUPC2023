<template>
  <div>
    <button type="button" class="btn" @click="handleButtonClick" v-if="showButton" style="border:none">
    <img alt="upload the document here" src="../assets/upload.png" class="button-image">
    <input type="file" accept="application/pdf" ref="fileInput" style="display: none;" @change="handleFileUpload">
  </button>

    <FileComponent v-if="!showButton" @click="cancelFile"/>
    <TextComponent v-if="!showButton" name="File uploaded successfully!"/>

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
    name: 'slide', params: { data: msg.value }})
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
    axios.get('/data')
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
    border: 1px solid rgb(23, 134, 218);
    margin: 0 15px;
    width: 140px;
    height: 50px;
    border-radius: 20px;
    -webkit-border-radius: 20px;
    -moz-border-radius: 20px;
    -ms-border-radius: 20px;
    -o-border-radius: 20px;
    font-size: 15px;
    font-weight: bold;
    letter-spacing: .7px;
    background-image:linear-gradient(top, #ffffff33 1px, #ffffff00 1px, #0000001a 100%);
    box-shadow: 0 60px 12px -18px rgba(0,0,0,0.1), 0 60px -12px rgba(0,0,0,0.1);
    margin-bottom: 10px;
    animation: anime 1s infinite ease-in-out alternate;
    -webkit-animation: anime 1s infinite ease-in-out alternate;
    animation-delay: .3s;
  }

  @keyframes anime {
    100% {
      transform: tranlateY(20px);
      -webkit-transform: tranlateY(20px);
      -moz-transform: tranlateY(20px);
      -ms-transform: tranlateY(20px);
      -o-transform: tranlateY(20px);
      box-shadow:0 40px 10px -18px rgba(0,0,0,0.2), 0 40px 16px -12px rgba(0,0,0,0.2);
    }
  
  }
</style>
