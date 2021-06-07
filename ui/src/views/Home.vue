<template>
  <div class="header-container">
    <h1>Purchase list</h1>
    <button @click="handleExitButton">exit</button>
  </div>
  <new-purchase/>
  <purchase-list/>
  <pagination
    :load-next-purchase-page="handleClickNextPage"
    :load-prev-purchase-page="handleClickPrevPage"
    :current-page="currentPage"
    :count="purchaseCount"
  />
</template>
<script>
import { ref, onMounted, provide } from 'vue'
import { useRouter } from 'vue-router'

import PurchaseList from '../components/purchase/purchase-list'
import ApiService from '../services/api'
import NewPurchase from '../components/purchase/new-purchase'
import Pagination from '../components/purchase/pagination'

export default {
  name: 'Home',
  components: { Pagination, NewPurchase, PurchaseList },
  setup () {
    const router = useRouter()

    const purchaseList = ref([])
    const currentPage = ref(1)
    const purchaseCount = ref(0)

    const setCurrentPage = (page) => {
      currentPage.value = page
    }
    const loadPurchaseList = async (page) => {
      const { results, count } = await ApiService.get(`http://localhost:3003/purchases/?page=${page}`, {}, router)
      purchaseCount.value = count
      purchaseList.value = results
    }
    const addNewPurchase = async (purcachse) => {
      await ApiService.post('http://localhost:3003/purchases/', purcachse)
      await loadPurchaseList(currentPage.value)
    }
    onMounted(() => loadPurchaseList(currentPage.value))

    provide('purchase-list', purchaseList)
    provide('add-new-purchase', addNewPurchase)
    provide('current-page', currentPage)

    return {
      loadPurchaseList,
      currentPage,
      setCurrentPage,
      purchaseCount
    }
  },
  methods: {
    handleClickNextPage () {
      this.setCurrentPage(this.currentPage + 1)
      this.loadPurchaseList(this.currentPage)
    },
    handleClickPrevPage () {
      this.setCurrentPage(this.currentPage - 1)
      this.loadPurchaseList(this.currentPage)
    },
    handleExitButton () {
      localStorage.removeItem('refresh')
      localStorage.removeItem('access')
      localStorage.removeItem('expireDate')
      this.$router.push('/login')
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
.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between
}
</style>
