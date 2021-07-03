<template>
  <div class="purchase-element" @click="viewSetupButtons = !viewSetupButtons">
    <v-card elevation="1">
      <v-card-header>
        <v-card-header-text>
          <v-card-title>
            <div class="purchase-title">
              <div>{{ title }}</div>
              <div>{{ cost }} ₽</div>
            </div>

          </v-card-title>
          <v-card-subtitle>
            {{ dateToView }}
          </v-card-subtitle>
        </v-card-header-text>
      </v-card-header>
      <div v-if="viewSetupButtons" class="purchase-setup-wrapper">
        <div style="width: 100px">
          <v-btn :disabled="true"  block color="#3f51b5" :style="{color: '#ffffff'}">
            edit
          </v-btn>
        </div>
        <div style="width: 100px">
          <v-btn @click="handleDeletePurchase"
                 block
                 :color="componentColors.get('danger-color')"
                 :style="{color: '#ffffff'}">
            delete
          </v-btn>
        </div>
      </div>
    </v-card>

  </div>
</template>
<script>
import { inject } from 'vue'
// import { primaryColor, dangerColor } from '../../services/color-servise'

import {
  VCard,
  VCardHeader,
  VCardTitle,
  VCardSubtitle,
  VCardHeaderText,
  VBtn
} from 'vuetify'

export default {
  name: 'purchase-element',
  setup () {
    return {
      componentColors: inject('component-colors')
    }
  },
  components: {
    VCard,
    VCardHeader,
    VCardTitle,
    VCardSubtitle,
    VCardHeaderText,
    VBtn
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

.purchase-setup-wrapper {
  padding-top: 10px;
  padding-bottom: 10px;
  display: flex;
  justify-content: space-around;
}
</style>
