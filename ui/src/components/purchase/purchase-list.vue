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
      :handle-update-click="handleUpdateClick"
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
      deletePurchase: inject('delete-purchase'),
      openModal: inject('set-show-purchase-form'),
      setTmpPurchase: inject('set-tmp-purchase')
    }
  },
  methods: {
    handleUpdateClick (id) {
      const purchaseObject = this.list.find(purchase => purchase.id === id)

      this.setTmpPurchase('title', purchaseObject.title)
      this.setTmpPurchase('amount', purchaseObject.amount)
      this.setTmpPurchase('id', purchaseObject.id)

      this.openModal(true)
    }
  }
}
</script>

<style>
.purchase-list-container .transaction-element {
  margin-top: 10px;
}
</style>
