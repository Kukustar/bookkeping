<template>
  <div class="purchase-list-container container">
    <transaction-element
      v-for="(deposit, index) in this.list"
      :key="index"
      :cost="deposit.amount"
      :date="deposit.date"
      :title="deposit.title"
      :id="deposit.id"
      :delete-transaction="deleteDeposit"
    />
  </div>
</template>

<script>
import { inject } from 'vue'
import TransactionElement from '../common/transaction-element'

export default {
  name: 'deposits-list',
  components: { TransactionElement },
  setup () {
    return {
      list: inject('deposits-list'),
      deleteDeposit: inject('delete-deposit')
    }
  }
}
</script>

<style>
.purchase-list-container .transaction-element {
  margin-top: 10px;
}
</style>
