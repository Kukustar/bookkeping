<template>
  <div class="purchase-list-container container">
    <purchase-element
      v-for="(purchase, index) in this.list"
      :key="index"
      :cost="purchase.cost"
      :date="purchase.date"
      :title="purchase.title"
      :id="purchase.id"
      :delete-purchase="deletePurchase"
    />
  </div>
</template>

<script>
import { inject } from 'vue'
import PurchaseElement from './purchase-element'

export default {
  name: 'purchase-list',
  components: { PurchaseElement },
  setup () {
    return {
      list: inject('purchase-list'),
      deletePurchase: inject('delete-purchase')
    }
  }
}
</script>

<style>
.purchase-list-container .purchase-element{
  margin-top: 10px;
}
</style>
