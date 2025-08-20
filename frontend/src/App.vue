<script setup>
import { ref, onMounted } from "vue";

const message = ref("");   // create a reactive variable

onMounted(() => {
  fetch("https://render-backend-test-afu8.onrender.com/")   // Flask backend URL
    .then(res => res.text())   // use res.json() if Flask returns JSON
    .then(data => {
      message.value = data;    // update reactive variable
    })
    .catch(err => console.error("Error:", err));
});
</script>

<template>
  <h1>Welcome Roylkrishna</h1>
  <p>Backend says: {{ message }}</p>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
