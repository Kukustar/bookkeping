<template>
  <form :onsubmit="singUp" class="login-form-container">
      <div style="width: 250px">
        <material-input type="text" label="username" :updater="updateUserName"/>
      </div>

      <div style="width: 250px">
        <material-input type="password" label="password" :updater="updatePassword"/>
      </div>

      <div style="width: 250px">
        <v-btn @click="singUp" block color="#3f51b5" :style="{color: '#ffffff'}">
          Sing UP
        </v-btn>
      </div>
  </form>
</template>
<script>
import { ref } from 'vue'
import { API_HOST } from '../constants'
import { JwtTokenWorker } from '../jwt-guard'
import MaterialInput from '../components/material-input'

export default {
  name: 'Login',
  components: { MaterialInput },

  setup () {
    const username = ref('')
    const password = ref('')

    const updateUserName = (event) => {
      username.value = event.target.value
    }

    const updatePassword = (event) => {
      password.value = event.target.value
    }

    return {
      username,
      password,
      updatePassword,
      updateUserName
    }
  },
  methods: {
    singUp (e) {
      e.preventDefault()
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
          this.$router.replace('/home')
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
  align-items: center;
  justify-content: center;
  height: 500px;
}

</style>
