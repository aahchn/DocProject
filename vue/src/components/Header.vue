<template>
  <div class="w3-container w3-dark-grey">
      <h1 :value="articleItem" @input="updateTitle"> <!-- need to output articleItem[i].name when i is selected -->
        Output: {{title}}<br>
        {{articleItem}}
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
  props: ['articleItems'],
  data(){
    return{
      title: '' //TODO needs to be array instead of String
    }
  },
  methods:{
    updateTitle(event){
      this.title = event.target.value;
      this.$emit('titleChanged', this.title);
    }
  }
};
</script>
