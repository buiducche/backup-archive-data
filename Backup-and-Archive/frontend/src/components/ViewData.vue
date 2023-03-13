<template>
<div >
  <b-navbar toggleable type="dark" variant="dark">
    <b-navbar-brand class="nav-bar">Data Collection</b-navbar-brand>
    <b-navbar-nav class=ml-auto>
        <b-nav-item class="link" href="/">Backup</b-nav-item>
    </b-navbar-nav>
  </b-navbar>

    <div id="first">
      <table class="table table-hover">
                <tr>
                  <th scope="col">Name</th>
                  <th scope="col">Time</th>
                  <th scope="col">Status</th>
                </tr>
              <tbody>
               
                  <tr v-for="(data, index) in data" :key="index">
                  <td class="td1">{{ data.filename }}</td>
                  <td class="td2">{{ data.Date }}</td>
                  <td class="td2">{{ data.StatusStorage }}</td>

                
                </tr>
              </tbody>
    </table>
    <b-modal ref="editDataModal" id="edit-update-modal" title="Update" hide-footer>
      <div class="updateContainer">
       <b-form @submit.prevent="updatesubmit">
       
       <b-form-group id="input-12" label="IP Name" label-for="input-2">
      <b-form-input
          id="input-2"
          type="String"
          v-model="editentry.IP"
          placeholder="IP Name"
        ></b-form-input>
        </b-form-group>

        <b-form-group id="input-12" label="Path File" label-for="input-2">
        <b-form-input
          id="input-2"
          type="String"
          v-model="editentry.Path"  
          placeholder="Path file"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-12" label="Policy storage" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="editentry.Policy"
          placeholder="Type Policy"
          rows=8
        ></b-form-textarea>
      </b-form-group>
    <b-button pill v-on:Click.stop="updatesubmit" @click="$bvModal.hide('edit-update-modal')" id="button-2" type="submit" variant="dark">Update</b-button>
     
  </b-form>
  </div>
    </b-modal>
    
    
    
  </div>    
    </div>
    
</template>


<script>
import axios from 'axios';
export default {
    data(){
        return{
            
            data: [],
            editentry:{
              _id:"",
              IP:"",
              Path:"",
              Policy:"",

            },
        };
        

    },
    
    methods:{
     
        getData(){
          
           const path = 'http://127.0.0.1:5000/view';
            axios.get(path)
             .then((res) => {
                 this.data = res.data;
                 console.log(this.data);
                 
             })
             .catch((error) => {
                 console.error(error);
             });
        },

        onDeleteData(data){
          
          const finalData = JSON.parse(JSON.stringify(data));
          this.removeData(finalData._id)
        },

        removeData(dataid){
         
         const path = 'http://127.0.0.1:5000/dataview/'+dataid.$oid;
         console.log(path)
         axios.delete(path).then(()=>{
           console.log("deleted")
           this.getData();
         })
         .catch(error => {
           console.log(error);
           this.getData();
         })
        },
        
        editData(data){
          this.editentry = data;
        
        },

        updatesubmit(){
          const finalData = JSON.parse(JSON.stringify(this.editentry));
          
          const id=finalData._id.$oid
         
          const path = 'http://127.0.0.1:5000/dataview/'+id;

          axios.put(path,{
            IP       : this.editentry.IP,
            Path   : this.editentry.Path,
            Policy        : this.editentry.Policy,
          })
          .then(()=>{
            this.getData();
            
          })
          .catch(error =>{
            console.error(error);
            this.getData();
          })
        }
       
    },
    created(){
           
            this.getData();
        },
    
}
</script>

<style>

#first{
margin-right: 25px;
margin-left: 25px;
}


#input-12{
 align-content: center;
 width:100%;
 padding-left:20px;
 font-weight:bold;
  
}
#button-2{
  align-content: center;
  margin-left:40%;
}

.nav-bar{
  padding-left: 50px;;
}
.link{
  padding-right:100px;
  font-size: 20px;
 
}
.td1{
  width:15%;
}
.td2{
  width:70%;
  
}
</style>
