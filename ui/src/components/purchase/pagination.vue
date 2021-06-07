<template>
  <div class="pagination-container">
    <div class="pagination-button-wrapper">
      <button :disabled="!isCanViewPrevButton"  @click="loadPrevPurchasePage">prev</button>
    </div>
    <div class="pagination-current-page-wrapper">
      <p>{{ currentPage }}</p>
    </div>
    <div class="pagination-button-wrapper">
      <button :disabled="!isCanViewNextButton" @click="loadNextPurchasePage">next</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'pagination',
  props: {
    loadNextPurchasePage: {
      type: Function,
      required: true
    },
    loadPrevPurchasePage: {
      type: Function,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    },
    count: {
      type: Number,
      required: true
    }
  },
  computed: {
    isCanViewNextButton () {
      const totalPages = parseInt(String(this.count / 25))
      return this.currentPage < totalPages
    },
    isCanViewPrevButton () {
      return this.currentPage > 1
    }
  }
}
</script>

<style>
.pagination-container {
  margin-bottom: 20px;
  margin-top: 20px;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>
