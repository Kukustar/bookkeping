<template>
  <div class="new-purchase-button-container">
    <div class="new-purchase-input-container" v-if="isAddNewPurchase">
      <div class="input-wrapper"><input placeholder="cost ₽" type="number" v-model="cost"/> </div>
      <div class="input-wrapper"><input placeholder="title" v-model="title"/></div>
      <div class="add-purchase"><button @click="addNewPurchase">add</button></div>
    </div>
    <div v-else>
      <button @click="isAddNewPurchase= !isAddNewPurchase">add</button>
    </div>
  </div>

</template>

<script>
import { inject } from 'vue'
export default {
  name: 'new-purchase',
  setup () {
    return {
      addNew: inject('add-new-purchase')
    }
  },
  data () {
    return {
      isAddNewPurchase: false,
      cost: '',
      title: ''
    }
  },
  methods: {
    addNewPurchase () {
      this.isAddNewPurchase = false
      this.addNew({
        title: this.title,
        cost: this.cost,
        date: new Date(),
        description: ''
      })
    }
  }
}
</script>

<style>
.new-purchase-button-container {
  display: flex;
  justify-content: space-around;
}

.new-purchase-button-container div {
  margin-bottom: 20px;
}

.new-purchase-input-container{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center
}

</style>
