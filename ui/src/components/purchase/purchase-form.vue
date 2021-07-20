<template>

  <div class="add-button-form">
    <v-btn
      @click="handleAddNewClick"
      :color="componentColor.get('primary-color')"
      :style="{color: '#fff'}"
    >add
    </v-btn>
  </div>

  <div class="overlay" v-if="showPurchaseForm" @click="() => setShowPurchaseForm(false)"></div>

  <div class="modal" v-if="showPurchaseForm">
    <v-card>
      <div class="form-wrapper">
        <div class="form-purchase">
          <div class="close-button">
            <v-btn
              @click="() => setShowPurchaseForm(false)"
              :style="{color: '#ffffff'}"
              :color="componentColor.get('danger-color')"
            >
              x
            </v-btn>
          </div>

          <div class="input-wrapper">
            <material-input :value="amountValue" :input-mode="'numeric'" type="number" label="cost ₽" :updater="updateAmount"/>
          </div>

          <div class="input-wrapper">
            <material-input :value="titleValue" :input-mode="'verbatim'" type="text" label="title" :updater="updateTitle"/>
          </div>

          <div class="add-button">
            <v-btn
              :style="{color: '#ffffff'}"
              :color="componentColor.get('primary-color')"
              @click="handleClick"
            >
              {{ buttonLabel }}
            </v-btn>
          </div>

        </div>
      </div>
    </v-card>
  </div>

</template>

<script>
import MaterialInput from '../material-input'
import { inject } from 'vue'
import { VCard } from 'vuetify'

export default {
  name: 'purchase-form',
  components: {
    MaterialInput,
    VCard
  },
  props: {
    handleCreate: {
      type: Function,
      required: true
    },
    handleUpdate: {
      type: Function,
      required: true
    }
  },
  setup () {
    return {
      componentColor: inject('component-colors'),
      showPurchaseForm: inject('show-purchase-form'),
      setShowPurchaseForm: inject('set-show-purchase-form'),
      setTmpPurchase: inject('set-tmp-purchase'),
      clearTmpPurchase: inject('clear-tmp-purchase'),
      tmpPurchase: inject('tmp-purchase')
    }
  },
  data () {
    return {
      showForm: false
    }
  },
  methods: {
    updateTitle (event) {
      this.setTmpPurchase('title', event.target.value)
    },
    updateAmount (event) {
      this.setTmpPurchase('amount', event.target.value)
    },
    handleClick () {
      if (this.tmpPurchase.id === undefined) {
        this.handleCreate()
      } else {
        this.handleUpdate()
      }
    },
    handleAddNewClick () {
      this.clearTmpPurchase()
      this.setShowPurchaseForm(true)
    }
  },
  computed: {
    amountValue () {
      return this.tmpPurchase.id === undefined ? '' : this.tmpPurchase.amount
    },
    titleValue () {
      return this.tmpPurchase.id === undefined ? '' : this.tmpPurchase.title
    },
    buttonLabel () {
      return this.tmpPurchase.id === undefined ? 'add' : 'update'
    }
  }
}
</script>

<style>
.form-wrapper {
  padding-top: 15px;
  height: 290px;
}

.form-purchase {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.overlay {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
}

.modal {
  position: absolute;
  width: 100%;
  z-index: 9999;
  align-items: center;
  padding-right: 24px
}

.form-wrapper .add-button {
  margin-top: 20px;
}

.form-wrapper .close-button {
  width: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  padding-right: 15px;
}

.form-wrapper .close-button .v-btn--size-default {
  min-width: 0 !important;
  padding: 0 10px;
  min-height: 0 !important;
  --v-btn-height: 22px !important;
}

.add-button-form {
  text-align: center;
  padding-top: 20px;
  padding-bottom: 20px;
}

</style>
