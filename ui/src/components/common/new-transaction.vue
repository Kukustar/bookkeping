<template>

    <div class="new-transaction-button-container" >
      <v-card elevation="1" v-if="isAddNewTransaction">
      <div class="new-transaction-input-container" >
        <div class="input-wrapper">
          <material-input :input-mode="'numeric'" type="number" label="cost ₽" :updater="updateAmount"/>
        </div>
        <div class="input-wrapper">
          <material-input :input-mode="'verbatim'" type="text" label="title" :updater="updateTitle"/>
        </div>
        <div class="add-transaction">
          <v-btn
            :style="{color: '#ffffff'}"
            @click="addNewTransaction"
            :color="componentColor.get('primary-color')"
          >add
          </v-btn>
          <v-btn
            :color="componentColor.get('warning-color')"
            :style="{color: '#ffffff'}"
            @click="isAddNewTransaction = !isAddNewTransaction">
            cancel
          </v-btn>
        </div>
      </div>
      </v-card>
      <div v-else>
        <v-btn
          :style="{color: '#ffffff'}"
          :color="componentColor.get('primary-color')"
          @click="isAddNewTransaction= !isAddNewTransaction"
        >
          add
        </v-btn>
      </div>
    </div>

</template>

<script>
import { inject } from 'vue'
import MaterialInput from '../material-input'

export default {
  name: 'new-transaction',
  components: {
    MaterialInput
  },
  setup () {
    return {
      componentColor: inject('component-colors')
    }
  },
  props: {
    addNew: {
      type: Function,
      required: true
    }
  },
  data () {
    return {
      isAddNewTransaction: false,
      amount: '',
      title: ''
    }
  },
  methods: {
    updateAmount (e) {
      this.amount = e.target.value
    },
    updateTitle (e) {
      this.title = e.target.value
    },
    addNewTransaction () {
      this.isAddNewTransaction = false
      this.addNew(this.title, this.amount, new Date())
      this.amount = ''
      this.title = ''
    }
  }
}
</script>

<style>
.new-transaction-button-container {
  padding-top: 5px;
  display: flex;
  justify-content: space-around;
}

.new-transaction-button-container div {
  margin-bottom: 20px;
}

.new-transaction-button-container .add-transaction {
  display: flex;
  justify-content: space-evenly;
  align-content: space-between;
  align-items: center;
  width: 300px;

}

.new-transaction-input-container {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center
}

.new-transaction-input-container input {
  height: 40px;
  text-align: center;
}

</style>
