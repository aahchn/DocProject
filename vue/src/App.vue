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
      access_token: `` //TODO
    }
  },

  methods:{  //TODO - get from Flask and return it
    //need to get AUTH access token first
    authentication(){
      const path = `http://localhost:5000/auth`;
      axios.post(path, {
         access_token: 'Finn',  //TODO
         //lastName: 'Williams'
       })
      .then((response) => {console.log(response);
      },(error) => {console.log(error);
      });
    },

    /* authentication(){
      const path = `http://localhost:5000/auth`;
      axios.post(path) //TODO change the response => bc it is a POST method not a GET
       .then(response => {this.access_token = response.data.access_token});
    }, */

    getDocumentations(/* access token */){ //TODO
      const path = `http://localhost:5000/item/test`;
      axios.get(path)
        .then(response => {this.items = response.data.items});
      //const name = items.map(item => item.name );
    }
  },
  mounted(){
    this.authentication();
    this.getDocumentations(this.access_token);
    return this.items;
  }
}
</script>



<style scoped>
.HeaderAndBody {
  margin-left: 15%;
}
</style>
