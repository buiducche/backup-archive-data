<template>
<div id="app">
    <b-navbar toggleable type="dark" variant="dark">
    <b-navbar-brand class="nav-bar">Data Collection</b-navbar-brand>
    <b-navbar-nav class=ml-auto>
        <b-nav-item class="link" href="/view">Storage at Bucket</b-nav-item>
    </b-navbar-nav>
  </b-navbar>

 <h3>Enter your Data</h3>
    <b-form @submit="submit">

      <b-form-group id="input-group-2" label="Object" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="dataentry.Object"
          placeholder="Type your Object you want"
        ></b-form-textarea>
      </b-form-group>
      <b-form-group id="input-group-2" label="Bucket" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="dataentry.Bucket"
          placeholder="Where do Object storage ?"
          
        ></b-form-textarea>
      </b-form-group>
            <b-form-group id="input-group-2" label="Folder" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="dataentry.Folder"
          placeholder="Do you want save ?"
          
        ></b-form-textarea>
      </b-form-group>
            
    <b-button pill v-on:Click="submit" id="button-1" type="submit" variant="dark">Submit</b-button>
     
  </b-form>
    
  </div>

</template>
<script>
import axios from 'axios';
export default{
 
  data(){
    return {
       dataentry:{
        Object:"",
        Bucket:"",
        Folder:"",
      },
    };
  },
  methods:{
    submit:function(){
      const path = 'http://127.0.0.1:5000/dataentry'
      axios.post(path, {
        Object       : this.dataentry.Object,
        Bucket   : this.dataentry.Bucket,
        Folder        : this.dataentry.Folder,
        }
      ).then (this.$toasted.show("Success Backup"))
      .catch(err =>{
        console.log(err);
      });
    },
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Castoro&display=swap');
#app {
  font-family: 'Lato', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
#input-group-1 {
  margin-left:25%;
  margin-bottom: 20px;
  width: 50%;
  padding-left: 80px;
  margin-top: 50px;
  font-weight:bold;
 
}
h3{
  margin-left:40%;
  margin-top:20px;
  font-family: 'Castoro', serif;
}
#input-group-2{
  margin-left:25%;
  margin-bottom: 20px;
  width:50%;
  padding-left:80px;
 
  font-weight:bold;
}
#button-1{
margin-left:50%;
} 
.nav-bar{
  padding-left: 50px;;
}
.link{
  padding-right:100px;
  font-size: 20px;
  color:white;
}
</style>