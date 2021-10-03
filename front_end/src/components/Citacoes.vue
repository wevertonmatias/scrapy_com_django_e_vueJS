<template>
  <div>
    <h1 class="text-center text-info">Lista de citacoes </h1>
    
    <ul class="list-group-item" >
        <li class="list-group-item" v-for="citacao in citacoes" v-bind:key="citacao.id">
            <div class="card">
                    <div class="card-header">
                    Autor(a): {{ citacao.autor }}
                    </div>
                    <div class="card-body">
                        <p class="card-text">{{ citacao.citacao }}</p>
                    </div>
            </div>
        </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
export default {
  name: 'Citacoes',
  data(){
    return {
      citacoes:null
    }
  },
  mounted(){
    axios.get("http://127.0.0.1:8000/api/")
    .then(res=>this.citacoes = res.data)
  }
}
</script>

