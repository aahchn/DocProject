<template>
 <div>
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <SideBar :articleItems="articleItems" @emitTitle="updateTitle($event)" @emitInfo="updateInfo($event)"/> <!-- TODO, MOVE THIS TO HEADER VIA PROP -->

     <div class="HeaderAndBody">
        <Header :updatedTitle="selectedTitle"/> <!-- Header calls the getItemName function -->
        <br>
        {{articleItems}}
        <br>
        <Body :updatedInfo="selectedInfo"/>
      </div>
 </div>
</template>


<script>
import axios from 'axios';
import SideBar from './components/SideBar';
import Header from './components/Header';
import Body from './components/Body';

export default{
  //name: 'App',
  components: {
    SideBar: SideBar,
    Header: Header,
    Body: Body
  },

  data(){
    return { articleItems:[], selectedTitle: null, selectedInfo: null };
  },

  methods:{
    updateTitle(updatedTitle){  //TODO
      this.selectedTitle = updatedTitle;
      console.log(this.selectedTitle);
    },
    updateInfo(updatedInfo){
      this.selectedInfo = updatedInfo;
      console.log(this.selectedInfo);
    },
    getItemList(){
      axios.get("http://localhost:5000/items")
        .then(response => {
          this.articleItems = response.data.items;
          console.log(this.articleItems);
          for (var i = 0; i < this.articleItems.length; ++i){
            console.log(this.articleItems[i].name); //returns 'test'
            console.log(this.articleItems[i].price); //returns 15.99
            //Can also do params to get just the name or price
          }
      })
    },
    /* getItemName(){
      axios.get("http://localhost:5000/item/JavaScript")
        .then(response => {
          this.name = response.data.name;
          console.log(this.name + " - hello i am here"); //returns 'JavaScript'
        })
    }, */
  },
  mounted(){
    this.getItemList();
    //this.getItemName();
  }
}
</script>



<style scoped>
.HeaderAndBody {
  margin-left: 15%;
}
</style>
