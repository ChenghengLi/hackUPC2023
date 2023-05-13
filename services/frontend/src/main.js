import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import App from './App.vue';
import router from './router';
import axios from "axios";
import VueAxios from "vue-axios";



const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'https://backend-chenghengli.cloud.okteto.net/';  // the FastAPI backend  https://backend-chenghengli.cloud.okteto.net/  http://localhost:5000/

app.use(router);
app.mount("#app");

// Axios Plugin
app.use(VueAxios, axios);
app.provide("axios", app.config.globalProperties.axios);