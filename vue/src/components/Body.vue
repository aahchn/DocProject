<template>
  <div class="w3-container">
     Python is an interpreted, high-level, general-purpose programming
     language. Created by Guido van Rossum and first released in 1991, Python's
     design philosophy emphasizes code readability with its notable use of
     significant whitespace. <!-- need to grab from database dynamically -->
   </div>
</template>

<script>
export default{
  name: 'Body',
  props: {
    items:{
      type: Array, //Should be a string --> need to isolate the String
      required: true
    }
  },
  computed: { //TODO - turns data into viewable stuff
    
  }
};
</script>


<style scoped>
div {
  background-color: lightblue;
  width: 80%;
  padding: 25px;
  border: 5px solid black;
}
</style>
