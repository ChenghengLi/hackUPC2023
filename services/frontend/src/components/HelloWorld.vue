<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script setup>
import {onMounted, ref} from 'vue';

import { inject } from "vue";

const axios = inject('axios');

const msg = ref("hola")

function getMessage() {
  axios.get('/')
    .then((res) => {
      msg.value = res.data;
    })
    .catch((error) => {
      console.error(error);
    });
}

onMounted(async () => {
  getMessage();
});


</script>