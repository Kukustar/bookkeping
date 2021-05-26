<template>
  <div class="purchase-list-container container">
    <purchase-element/>
  </div>
</template>

<script>
import PurchaseElement from './purchase-element'

export default {
  name: 'purchase-list',
  components: { PurchaseElement }
}
</script>

<style>
.purchase-list-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.purchase-list-container .purchase-element {
  display: block;
  width: auto;
  max-width: 300px;
  border: solid;
  border-radius: 15px;
}

.purchase-list-container :not(.purchase-element:first-child) {
  margin-top: 10px;
}
</style>
