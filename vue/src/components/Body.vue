<template>
  <div class="w3-container">
     {{updatedInfo}} <!-- need to grab from database dynamically -->
   </div>
</template>

<script>
export default{
  props: ['updatedInfo'],
}
</script>


<style scoped>
div {
  background-color: lightblue;
  width: 80%;
  padding: 25px;
  border: 5px solid black;
}
</style>
