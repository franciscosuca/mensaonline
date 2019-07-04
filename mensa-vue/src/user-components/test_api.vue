<template>
  <div>
  <form @submit.prevent="submitNote">
  <!-- <form> -->
    <label>Title</label>
    <input type="text" v-model="formData.title">
    <label>Content</label>
    <textarea v-model="formData.content"></textarea>
    <br>
    <!-- <button type="submit" v-on:click="submitNote">Submit</button> -->
    <button type="submit">Submit</button>
  </form>
  <h1>POST Result</h1>
  <p>{{msg}}</p>
  <br>
  <h1>All notes</h1>
  <ul>
    <li v-for="note in notes" :key="note.id">
      <h3>{{note.title}}</h3>
      <h5>{{note.created}}</h5>
      <p>{{note.content}}</p>
    </li>
  </ul>
  </div>
</template>

<script>
import api from './api/index.js'
export default {
 
  data () {
    return {
      msg: '',
      formData:{
        title:'',
        content:'',
      },
      notes: []
    }
  },
  methods:{
    submitNote(){
      api.fetchNotes('post',null,this.formData).then(res => {
        this.msg = 'Saved'
        console.log(this.formData)
      }).catch((e) => {
        this.msg = e.response
      })
    },
    fetchAllNotes(){
      api.fetchNotes('get',null,null).then(res => {
        this.notes = res.data
        // Check the data from the console
        console.log(this.notes)
      }).catch((e) => {
        console.log(e)
      })
    }
  },
  mounted(){
    // fetch all notes once component is mounted
    this.fetchAllNotes()
  }
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  max-width: 500px;
  margin: 0 auto;
  text-align: left;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  /* display: inline-block; */
  margin: 0 10px;
}

a {
  color: #42b983;
}

input, textarea{
  width: 100%;
  display: block;
  padding: 6px 10 px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

label{
  margin-top: 15px;
  display: block;
  padding: 5px 5px;
}

button{
  background: #000;
  color: #fff;
  border-radius: 3px;
  padding: 6px 3px;
}

</style>
