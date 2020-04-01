<template>
 <div>
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <SideBar></SideBar>
     <div class="HeaderAndBody">
        <Header v-bind:title="title"></Header>
        <br>
        <Body v-bind:items="items"></Body>
      </div>
 </div>
</template>


<script>
import axios from 'axios'
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

  data(){  //TODO - need to retrieve from database
    return {
      items: [], //talks with <Body v-bind>
      title: 'Items',
      selectedItem: null, //What title would be initially,
    }
  },

  methods:{  //TODO - get from Flask and return it
    getDocumentations(){
      const path = `http://localhost:5000/item/test`;
      axios.get(path)
        .then(response => {this.items = response.data.items});
      //const name = items.map(item => item.name );
    }
  },
  mounted(){
    this.getDocumentations();
    return this.items;
  }
}
</script>



<style scoped>
.HeaderAndBody {
  margin-left: 15%;
}
</style>
