<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">moi</router-link> |
    <router-link to="/projets">projets</router-link> |
    <router-link to="/posts">posts</router-link> |
    <router-link to="/notes">notes</router-link> |
    <router-link to="">templates</router-link> |
    <router-link to="">cv</router-link> |
  </nav>
</template>


<script>


</script>
<style>
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>