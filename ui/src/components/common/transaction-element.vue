<template>
  <div class="transaction-element" @click="viewSetupButtons = !viewSetupButtons">
    <v-card elevation="1">
      <v-card-header>
        <v-card-header-text>
          <v-card-title>
            <div class="transaction-title">
              <div>{{ title }}</div>
              <div>{{ amount }} ₽</div>
            </div>

          </v-card-title>
          <v-card-subtitle>
            {{ dateToView }}
          </v-card-subtitle>
        </v-card-header-text>
      </v-card-header>
      <div v-if="viewSetupButtons" class="transaction-setup-wrapper">
        <div style="width: 100px">
          <v-btn :disabled="true"  block color="#3f51b5" :style="{color: '#ffffff'}">
            edit
          </v-btn>
        </div>
        <div style="width: 100px">
          <v-btn @click="handleDeleteTransaction"
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

import {
  VCard,
  VCardHeader,
  VCardTitle,
  VCardSubtitle,
  VCardHeaderText,
  VBtn
} from 'vuetify'

export default {
  name: 'transaction-element',
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
    amount: {
      type: Number,
      default: 0
    },
    title: {
      type: String,
      default: ' - '
    },
    deleteTransaction: {
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
    handleDeleteTransaction () {
      this.deleteTransaction(this.id)
    }
  }
}
</script>
<style>
.transaction-title {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  width: 100%;
  cursor: pointer;
}

.transaction-setup-wrapper {
  padding-top: 10px;
  padding-bottom: 10px;
  display: flex;
  justify-content: space-around;
}
</style>
