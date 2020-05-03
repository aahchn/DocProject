<template>
  <div class="w3-sidebar w3-bar-block w3-border-right" style="width:15%">
   <ul>
    <li v-for="(articleItem, index) in articleItems" :key="index" v-on:click="emitInfo(index)">
      {{articleItem.name}} <!-- shows the list of items in SideBar -->
    </li>
  </ul>
  </div>
</template>

<style>
</style>


<script>

export default{
  props: ['articleItems'],
  methods:{
    emitInfo(index){
      // on click --> get item index --> and put it into this.articleItems[i].name
      this.$emit('emitInfo', this.articleItems[index].name); //TODO
      //this.$emit('emitInfo', 'THIS IS A TEST');
    }
  }
}

</script>
