<template>
  <div class="purchase-element" @click="viewSetupButtons = !viewSetupButtons">
    <v-card elevation="1">
      <v-card-header>
        <v-card-header-text>
          <v-card-title>
            <div class="purchase-title">
              <div>{{  title }}</div>
              <div>{{ cost }} ₽</div>
            </div>

          </v-card-title>
          <v-card-subtitle>
            {{ dateToView}}
          </v-card-subtitle>
        </v-card-header-text>
      </v-card-header>
    </v-card>
    <div v-if="viewSetupButtons" class="purchase-setup-wrapper">
      <button disabled>edit</button> <button @click="handleDeletePurchase">delete</button>
    </div>
  </div>
</template>
<script>
import {
  VCard,
  VCardHeader,
  VCardTitle,
  VCardSubtitle,
  VCardHeaderText
} from 'vuetify'
export default {
  name: 'purchase-element',
  components: {
    VCard,
    VCardHeader,
    VCardTitle,
    VCardSubtitle,
    VCardHeaderText
  },
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
  .purchase-title {
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    width: 100%;
    cursor: pointer;
  }
</style>
