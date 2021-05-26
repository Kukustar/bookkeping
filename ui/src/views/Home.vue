<template>
  <h1>Purchase list</h1>
  <purchase-list/>
</template>
<script>
import PurchaseList from '../components/purchase-list'

export default {
  name: 'Home',
  components: { PurchaseList },
  created () {
    const token = localStorage.getItem('access')

    fetch('http://localhost:3003/purchases/', {
      mode: 'cors',
      headers:
        {
          Authorization: `Bearer ${token}`
        }
    })
      .then(res => {
        const { status, statusText } = res
        if (status === 401 && statusText === 'Unauthorized') {
          localStorage.removeItem('access')
          localStorage.removeItem('expireDate')
          localStorage.removeItem('refresh')
          this.$router.push('/login')
        }
        return res.json()
      })
      .then(res => console.info(res))
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
