<template>
  <form :onsubmit="singUp" class="login-form-container">
    <input placeholder="username" v-model="username"/>
    <input placeholder="password" v-model="password" type="password"/>
    <button @click="singUp">Sing UP</button>
    <button @click="singUpAdmin">Sing UP admin</button>
  </form>
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
    singUpAdmin () {
      fetch('http://localhost:3003/api/token/', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: 'admin',
          password: 'admin'
        })
      })
        .then(r => r.json())
        .then(r => {
          const { refresh, access } = r
          const nowDate = new Date()
          const expireDate = new Date(nowDate.getTime() + 5 * 60000)
          const refreshTokenExpireDate = new Date(nowDate.getTime() + 1440 * 60000)
          const unixRefreshTokenExpireDate = +new Date(refreshTokenExpireDate)
          const unixExpireDate = +new Date(expireDate)

          localStorage.setItem('refresh', refresh)
          localStorage.setItem('access', access)
          localStorage.setItem('expireDate', String(unixExpireDate))
          localStorage.setItem('expireRefreshTokenExpireDate', String(unixRefreshTokenExpireDate))
          this.$router.push('/')
        })
        .catch(e => console.info(e))
    },
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

.login-form-container {
  display: flex;
  flex-direction: column;
  align-content: flex-start;
  height: 500px;
  justify-content: center;
}

.login-form-container input,
.login-form-container button {
  margin-top: 5px;
  height: 40px;
  text-align: center;
}

</style>
