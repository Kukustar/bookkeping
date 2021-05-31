<template>
  <h1>Purchase list</h1>
  <new-purchase/>
  <purchase-list/>
</template>
<script>
import { ref, onMounted, provide } from 'vue'
import { useRouter } from 'vue-router'

import PurchaseList from '../components/purchase/purchase-list'
import ApiService from '../services/api'
import NewPurchase from '../components/purchase/new-purchase'

export default {
  name: 'Home',
  components: { NewPurchase, PurchaseList },
  setup () {
    const router = useRouter()

    const purchaseList = ref([])
    const loadPurchaseList = async () => {
      purchaseList.value = await ApiService.get('http://localhost:3003/purchases/', {}, router)
    }
    const addNewPurchase = async (purcachse) => {
      await ApiService.post('http://localhost:3003/purchases/', purcachse)
    }
    onMounted(loadPurchaseList)

    provide('purchase-list', purchaseList)
    provide('add-new-purchase', addNewPurchase)
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
