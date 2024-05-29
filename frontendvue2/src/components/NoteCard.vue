<template>
    <div class="home">
      <h2>{{ note.title }}</h2>
      <h2>{{ note.content }}</h2>
    </div>
  </template>
  
  <script>
  export default {
    name: "NoteCard",
    props: {
      note: Object,
    },
  };
  </script>
  
  </script>
  
  <style scoped>
  </style>