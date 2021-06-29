<template>
  <div class="purchase-element" @click="viewSetupButtons = !viewSetupButtons">
    <div class="purchase-element-wrapper">
      <div class="purchase-title-time">
        <b>{{  title }}</b>
        <p><span>{{  dateToView }}</span></p>
      </div>
      <div class="purchase-cost">
        <div class="purchase-cost-wrapper">
          <p>{{ cost }} ₽</p>
        </div>
      </div>
    </div>
    <div v-if="viewSetupButtons" class="purchase-setup-wrapper">
      <button disabled>edit</button> <button @click="handleDeletePurchase">delete</button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'purchase-element',
  props: {
    id: {
      type: Number,
      required: true
    },
    date: {
      type: String,
      default: ''
    },
    cost: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ' - '
    },
    deletePurchase: {
      type: Function,
      required: true
    }
  },
  data () {
    return {
      viewSetupButtons: false
    }
  },
  computed: {
    dateToView () {
      const date = new Date(this.date)

      return date.toLocaleString()
    }
  },
  methods: {
    handleDeletePurchase () {
      this.deletePurchase(this.id)
    }
  }
}
</script>
<style>

.purchase-element .purchase-element-wrapper {
  display: flex;
  justify-content: space-around;
}

.purchase-element .purchase-setup-wrapper {
  display: flex;
  justify-content: space-around;
  margin-bottom: 10px;
}

.purchase-element .purchase-element-wrapper .purchase-icon {
  display: block;
}

.purchase-element .purchase-element-wrapper .purchase-title-time {
  display: block;
}

.purchase-element .purchase-element-wrapper .purchase-cost {
  display: block;
  margin: 0;
}

.purchase-element .purchase-element-wrapper .purchase-cost .purchase-cost-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.purchase-cost .purchase-cost-wrapper p {
  display: block;
}
</style>
