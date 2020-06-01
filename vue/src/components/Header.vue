<template>
  <div class="w3-container w3-dark-grey">
      <h1> <!-- need to output articleItem[i].name when i is selected -->
        Title: {{updatedTitle}}<br>
      </h1>
  </div>
</template>

<style scoped>
div {
  padding: 7px;
  width: 100%  /* want to be dynamic with the text (text + 5%) */
}
</style>

<script>
export default{
  props: ['updatedTitle'],
}
</script>
