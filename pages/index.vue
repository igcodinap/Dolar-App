<template id="">
  <div class="container">
    <h1 class="title">Valores dolar</h1>
    <div class="columns"
      <ValorCard :valor="valor" v-for="valor in valores" :key="valor.id"/>
  </div>
  </div>
</template>

<script>
import axios from 'axios';
import env from '../config/env';
import ValorCard from '../components/ValorCard'
  export default {
    name: 'IndexPage',
    components: {
      ValorCard
    },
    data(){
      return {
        valores: [],
      }
    },
    created(){
      axios.get(`${env.endpoint}`).then(response=>{
        this.valores = response.data;
      })
    }
  }
</script>

<style scoped>

</style>
