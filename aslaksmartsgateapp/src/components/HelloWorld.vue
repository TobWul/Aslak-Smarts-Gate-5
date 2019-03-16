<template>
  <div>
    <h1>Heia!</h1>
    <div>
      {{ electricity }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      electricity: null
    }
  },
  mounted () {
    axios
      .get(process.env.API_URL + 'electricity')
      .then(response => (
        this.electricity = response
      ))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
