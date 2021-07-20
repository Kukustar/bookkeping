<template>
  <div class="header-container">
    <h1>balance: {{balance}}</h1>
  </div>

  <PurchaseForm
    :handle-create="addNewPurchase"
    :handle-update="updatePurchase"
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
import PurchaseForm from '../components/purchase/purchase-form'
import Pagination from '../components/purchase/pagination'

import { API_HOST } from '../constants'

export default {
  name: 'Home',
  components: { Pagination, PurchaseForm, PurchaseList, VDivider },
  setup () {
    const router = useRouter()

    const showPurchaseForm = ref(false)

    const purchaseList = ref([])
    const currentPage = ref(1)
    const purchaseCount = ref(0)
    const balance = ref(0)
    const purchaseTypes = ref([])
    const tmpPurchase = ref({})

    const setCurrentPage = (page) => {
      currentPage.value = page
    }

    const setTmpPurchase = (field, value) => {
      tmpPurchase.value[field] = value
    }

    const clearTmpPurchase = () => {
      tmpPurchase.value = {}
    }

    const setShowPurchaseForm = (value) => {
      showPurchaseForm.value = value
    }

    const loadPurchaseTypes = async () => {
      const { results } = await ApiService.get(`${API_HOST}/purchase-types/`, {}, router)
      purchaseTypes.value = results
    }

    const loadBalance = async () => {
      const { results } = await ApiService.get(`${API_HOST}/balance/`, {}, router)
      balance.value = results.find(balance => balance.name === 'general').mount
    }

    const loadPurchaseList = async (page) => {
      const { results, count } = await ApiService.get(`${API_HOST}/purchases/?page=${page}`, {}, router)
      purchaseCount.value = count
      purchaseList.value = results
    }

    const updatePurchase = async () => {
      const pyrchase = {
        title: tmpPurchase.value.title,
        amount: tmpPurchase.value.amount,
        id: tmpPurchase.value.id,
        date: new Date(),
        description: ''
      }
      await ApiService.put(`${API_HOST}/purchases/${tmpPurchase.value.id}/`, pyrchase)
      showPurchaseForm.value = false
      await loadPurchaseList(currentPage.value)
      await loadBalance()
    }

    const addNewPurchase = async () => {
      const newPurchase = {
        title: tmpPurchase.value.title,
        amount: tmpPurchase.value.amount,
        date: new Date(),
        description: ''
      }
      await ApiService.post(`${API_HOST}/purchases/`, newPurchase)
      showPurchaseForm.value = false
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
    provide('purchase-types', purchaseTypes)
    provide('load-purchase-types', loadPurchaseTypes)
    provide('set-show-purchase-form', setShowPurchaseForm)
    provide('show-purchase-form', showPurchaseForm)
    provide('set-tmp-purchase', setTmpPurchase)
    provide('clear-tmp-purchase', clearTmpPurchase)
    provide('tmp-purchase', tmpPurchase)

    return {
      loadPurchaseList,
      currentPage,
      setCurrentPage,
      purchaseCount,
      balance,
      addNewPurchase,
      updatePurchase
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
