<template>
  <div class="header-container">
    <h1>balance: {{balance}}</h1>
  </div>

  <new-transaction
    :add-new="addNewPurchase"
  />
  <VDivider></VDivider>
  <purchase-list/>

  <pagination
    v-if="purchaseCount > 0"
    :load-next-page="handleClickNextPage"
    :load-prev-page="handleClickPrevPage"
    :current-page="currentPage"
    :count="purchaseCount"
  />
</template>
<script>
import { ref, onMounted, provide } from 'vue'
import { useRouter } from 'vue-router'

import { VDivider } from 'vuetify'

import PurchaseList from '../components/purchase/purchase-list'
import ApiService from '../services/api'
import NewTransaction from '../components/common/new-transaction'
import Pagination from '../components/purchase/pagination'

import { API_HOST } from '../constants'

export default {
  name: 'Home',
  components: { Pagination, NewTransaction, PurchaseList, VDivider },
  setup () {
    const router = useRouter()

    const purchaseList = ref([])
    const currentPage = ref(1)
    const purchaseCount = ref(0)
    const balance = ref(0)

    const setCurrentPage = (page) => {
      currentPage.value = page
    }

    const loadBalance = async () => {
      const { results } = await ApiService.get(`${API_HOST}/balance/`, {}, router)
      balance.value = results[0].mount
    }

    const loadPurchaseList = async (page) => {
      const { results, count } = await ApiService.get(`${API_HOST}/purchases/?page=${page}`, {}, router)
      purchaseCount.value = count
      purchaseList.value = results
    }
    /**
     *
     * @param title
     * @param amount
     * @param date
     * @returns {Promise<void>}
     */
    const addNewPurchase = async (title, amount, date) => {
      const newPurchase = { title, amount, date, description: '' }
      await ApiService.post(`${API_HOST}/purchases/`, newPurchase)
      await loadPurchaseList(currentPage.value)
      await loadBalance()
    }
    /**
     *
     * @param id
     * @returns {Promise<void>}
     */
    const deletePurchase = async (id) => {
      await ApiService.delete(`${API_HOST}/purchases/`, id)
      await loadPurchaseList(currentPage.value)
      await loadBalance()
    }

    onMounted(() => {
      loadPurchaseList(currentPage.value)
      loadBalance()
    })

    provide('purchase-list', purchaseList)
    provide('delete-purchase', deletePurchase)
    provide('current-page', currentPage)

    return {
      loadPurchaseList,
      currentPage,
      setCurrentPage,
      purchaseCount,
      balance,
      addNewPurchase
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
  justify-content: space-around;
  min-width: 350px;
}

.header-container h1 {
  margin-left: 20px;
}
</style>
