<script setup lang="ts">
  import { RouterView } from 'vue-router'
  import HeaderBar from '@/components/header.vue'
  import Footer from '@/components/footer.vue'
</script>

<template>
  <main>
    <RouterView />
  </main>
</template>

<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1 0 auto;
}

body {
  margin: 0;
  padding: 0;
  font-family: 'Inter', sans-serif;
}
</style>