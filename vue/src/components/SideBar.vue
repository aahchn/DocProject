<template>
  <div class="w3-sidebar w3-bar-block w3-border-right" style="width:15%">
   <ul>
    <li v-for="articleItem in articleItems" :key="articleItem.name"> <!-- TODO -->
      {{articleItem.name}}
      <!-- <a href="#" class="w3-bar-item w3-button">Python</a>
      <a href="#" class="w3-bar-item w3-button">Java</a>
      <a href="#" class="w3-bar-item w3-button">JavaScript</a> -->
    </li>
  </ul>
  </div>
</template>

<style>
</style>


<script>

export default{
  props: {
    articleItems: {
      type: Array,
    }
  }
}

</script>
