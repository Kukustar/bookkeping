<template>
  <div class="purchase-element">
    <div class="purchase-element-wrapper">
      <div class="purchase-icon">
        icon
      </div>
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
  </div>
</template>
<script>
export default {
  name: 'purchase-element',
  props: {
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
    }
  },
  computed: {
    dateToView () {
      const date = new Date(this.date)

      return date.toLocaleString()
    }
  }
}
</script>
<style>

.purchase-element .purchase-element-wrapper {
  display: flex;
  justify-content: space-around;
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
