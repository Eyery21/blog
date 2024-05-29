<template>
  <div id="app">
    
    <NavBar />
    <router-view />

  </div>
</template>
<script>
import NavBar from "./components/NavBar.vue";
import HomeView from "./views/HomeView.vue";

export default {
  name: "App.vue",
  components: {
    HomeView,
    NavBar,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
