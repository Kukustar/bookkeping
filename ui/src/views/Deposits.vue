<template>
  <new-transaction
    :add-new="addDeposit"
  />
  <VDivider></VDivider>

  <deposits-list/>

</template>
<script>
import { onMounted, provide, ref } from 'vue'
import { useRouter } from 'vue-router'

import { VDivider } from 'vuetify'

import NewTransaction from '../components/common/new-transaction'
import DepositsList from '../components/deposits/deposits-list'
import ApiService from '../services/api'
import { API_HOST } from '../constants'

export default {
  components: { DepositsList, NewTransaction, VDivider },
  setup () {
    const router = useRouter()

    const depositList = ref([])

    const loadDeposits = async (page) => {
      const { results } = await ApiService.get(`${API_HOST}/deposits/?page=${page}`, {}, router)
      depositList.value = results
    }

    const addDeposit = async (title, amount, date) => {
      const newDeposit = { title, amount, date, description: '' }
      await ApiService.post(`${API_HOST}/deposits/`, newDeposit)
    }

    const deleteDeposit = async (id) => {
      await ApiService.delete(`${API_HOST}/deposits/`, id)
      await loadDeposits(1)
    }

    onMounted(() => {
      loadDeposits(1)
    })

    provide('deposits-list', depositList)
    provide('delete-deposit', deleteDeposit)

    return {
      addDeposit
    }
  }
}
</script>
