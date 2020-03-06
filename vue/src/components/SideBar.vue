<template>
  <div class="w3-sidebar w3-bar-block w3-border-right" style="width:15%">
    <a href="#" class="w3-bar-item w3-button">Python</a>
    <a href="#" class="w3-bar-item w3-button">Java</a>
    <a href="#" class="w3-bar-item w3-button">JavaScript</a>
  </div>
</template>

<style>
</style>


<script>
// TODO
import axios from 'axios'
export default{
  data(){

  }
},
computed:{
  getNameFromDatabase(){
    const path = `http://127.0.0.1:5000/item` //TODO: talking to backend (flask)
    axios.get(path)
    .then(response => {

    })
  }
}
</script>
