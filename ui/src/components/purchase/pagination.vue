<template>
  <div class="pagination-container">
    <div class="pagination-button-wrapper">
      <v-btn
        :style="{color: '#ffffff'}"
        :color="componentColor.get('primary-color')"
        :disabled="!isCanViewPrevButton"
        @click="loadPrevPage">
        prev
      </v-btn>
    </div>
    <div class="pagination-current-page-wrapper">
      <p>{{ currentPage }}</p>
    </div>
    <div class="pagination-button-wrapper">
      <v-btn
        :style="{color: '#ffffff'}"
        :color="componentColor.get('primary-color')"
        :disabled="!isCanViewNextButton"
        @click="loadNextPage">
        next
      </v-btn>
    </div>
  </div>
</template>

<script>
import { inject } from 'vue'
export default {
  name: 'pagination',
  setup () {
    return {
      componentColor: inject('component-colors')
    }
  },
  props: {
    loadNextPage: {
      type: Function,
      required: true
    },
    loadPrevPage: {
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
      return this.count - this.currentPage * 25 > 0
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
