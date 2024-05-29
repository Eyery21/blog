<template>
  <div>
    hello !

    <Spotify />
  </div>
</template>

<script>
import Spotify from "../components/Spotify.vue";
export default {
  name: "HomeView",
  components: {
    Spotify,
  },
};
</script>