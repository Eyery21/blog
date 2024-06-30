<template>
  <div class="home">
    <div class="notes">
      <h2>{{ note.title }}</h2>
      <h2>{{ note.content }}</h2>
    </div>
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
  
  <style>

.notes {

  width: 200px;
  border: 1px solid red;
  background-color: beige;
}
</style>