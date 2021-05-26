<template>
  <input placeholder="username" v-model="username"/>
  <input placeholder="password" v-model="password" type="password"/>
  <button @click="singUp">Sing UP</button>
</template>
<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    singUp () {
      fetch('http://localhost:3003/api/token/', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: this.username,
          password: this.password
        })
      })
        .then(r => r.json())
        .then(r => {
          const { refresh, access } = r
          const nowDate = new Date()
          const expireDate = new Date(nowDate.getTime() + 5 * 60000)
          const unixExpireDate = +new Date(expireDate)
          console.info(unixExpireDate)
          console.info(nowDate)
          localStorage.setItem('refresh', refresh)
          localStorage.setItem('access', access)
          localStorage.setItem('expireDate', String(unixExpireDate))
          this.$router.push('/')
        })
        .catch(e => console.info(e))
    }
  }
}
</script>
<style>
html {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
