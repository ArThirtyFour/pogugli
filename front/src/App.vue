<template>
  <Main/>
  <Input :updateZapros="updateZapros"/>
  <button disabled v-if="zapros === ''">Нет ввода!</button>
  <button @click="GetZapros" v-else>Отправить запрос</button>
  <p v-if="responseMessage !== ''">Ваш результат находится в 127.0.0.1:5000/search/{{ responseMessage }}</p>
</template>

<style scoped>
button {
  margin: 10px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: auto;
  background-color: #002d80;
  color: white;
  border: 2px solid hsl(0, 0%, 0%);
  font-size: 20px;
  box-shadow: 0 2px 4px rgba(3, 93, 204, 0.55);
  border-radius: 10px;
}
p {
  text-align: center;
  color: #fafafa;
  font-size: 20px;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
button:disabled {
  background-color: #002d808b;
}
</style>

<script>
import axios from 'axios'
import Input from './components/Input.vue'
import Main from './components/Main.vue'

export default {
  components: { Main, Input },
  data() {
    return {
      zapros: '',
      responseMessage: ''  
    }
  },
  methods: {
    updateZapros(zapros) {
      this.zapros = zapros;
    },
    async GetZapros() {
      try {
        const result = await axios.post('http://127.0.0.1:5500/api/get_url',
          new URLSearchParams({ zapros: this.zapros }),
        );
        this.responseMessage = result.data;
      } catch (error) {
        console.log(error)  
      }
    }
  }
}
</script>
