<template>
  <form :onsubmit="singUp" class="login-form-container">
    <input placeholder="username" v-model="username"/>
    <input placeholder="password" v-model="password" type="password"/>
    <button @click="singUp">Sing UP</button>
<!--    <button @click="singUpAdmin">Sing UP admin</button>-->
  </form>
</template>
<script>
import { API_HOST } from '../constants'
import { JwtTokenWorker } from '../jwt-guard'

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
      fetch(`${API_HOST}/api/token/`, {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: this.username,
          password: this.password
        })
      })
        .then(r => {
          const { status } = r
          if (status === 200) {
            return r.json()
          } else {
            throw new Error('wrong password')
          }
        })
        .then(r => {
          const { refresh, access } = r
          const JWTGuard = new JwtTokenWorker()
          JWTGuard.updateAccessTokenContext(access)
          JWTGuard.updateRefreshTokenContext(refresh)
          this.$router.push('/home')
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
