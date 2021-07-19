<template>
  <div class="purchase-list-container container">
    <transaction-element
      v-for="(purchase, index) in this.list"
      :key="index"
      :amount="purchase.amount"
      :date="purchase.date"
      :title="purchase.title"
      :id="purchase.id"
      :delete-transaction="deletePurchase"
    />
  </div>
</template>

<script>
import { inject } from 'vue'
import TransactionElement from '../common/transaction-element'

export default {
  name: 'purchase-list',
  components: { TransactionElement },
  setup () {
    return {
      list: inject('purchase-list'),
      deletePurchase: inject('delete-purchase')
    }
  }
}
</script>

<style>
.purchase-list-container .transaction-element {
  margin-top: 10px;
}
</style>
