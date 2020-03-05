<template>
 <div>
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <SideBar></SideBar>
     <div class="SideBarAndBody">
        <Header></Header>
        <br>
        <Body></Body>
      </div>
 </div>
</template>


<script>
import SideBar from './components/SideBar';
import Header from './components/Header';
import Body from './components/Body';
export default{
  name: 'App',
  components: {
    SideBar: SideBar,
    Header: Header,
    Body: Body
  },
};
</script>



<style scoped>
.SideBarAndBody {
  margin-left: 15%;
}
</style>
