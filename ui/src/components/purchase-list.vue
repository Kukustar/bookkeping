<template>
  <div class="purchase-list-container container">
    <div class="purchase-element">
      <div class="purchase-element-wrapper">
        <div class="purchase-icon">
          icon
        </div>
        <div class="purchase-title-time-container">
        </div>
      </div>
    </div>
    <div class="purchase-element">
      purchase list
    </div>
    <div class="purchase-element">
      purchase list
    </div>

  </div>
</template>

<script>
export default {
  name: 'purchase-list'
}
</script>

<style scoped>
.purchase-list-container {
  display: flex;
  flex-direction: column;
}

.purchase-list-container .purchase-element {
  display: block;
}

.purchase-list-container .purchase-element .purchase-element-wrapper {
  display: flex;
}

.purchase-list-container .purchase-element .purchase-element-wrapper .purchase-icon {
  display: block;
}

.purchase-list-container .purchase-element .purchase-element-wrapper .purchase-title-time {
  display: block;
}
</style>
