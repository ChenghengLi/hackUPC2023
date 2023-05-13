<template>
  <div>
    <p>{{ msg1 }}</p>
  </div>
  <UploadComponent></UploadComponent>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import { inject} from "vue";
import UploadComponent from './UploadComponent.vue';

const axios = inject('axios');

const msg1 = ref("adhoolios")

function getMessage() {
  axios.get('/')
    .then((res) => {
      msg1.value = res.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(async () => {
  getMessage();
});



</script>