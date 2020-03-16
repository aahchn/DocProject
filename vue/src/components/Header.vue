<template>
  <div class="w3-container w3-dark-grey">
      <h1> {{title}} </h1> <!-- need to grab from database dynamically  {{title}} -->
  </div>
</template>

<style scoped>
div {
  padding: 7px;
  width: 20%  /* want to be dynamic with the text (text + 5%) */
}
</style>

<script>
export default{
  props:{
    title:{
      type: String,
      required: true
    }
  },
  data(){
    return{

    }
  },
};
</script>
