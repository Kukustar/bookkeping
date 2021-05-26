<template>
  <h1>Home</h1>
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
      .then(res => res.json())
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
