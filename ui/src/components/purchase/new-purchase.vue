<template>

    <div class="new-purchase-button-container" >
      <v-card elevation="1" v-if="isAddNewPurchase">
      <div class="new-purchase-input-container" >
        <div class="input-wrapper">
          <material-input type="number" label="cost ₽" :updater="updateCost"/>
        </div>
        <div class="input-wrapper">
          <material-input type="text" label="title" :updater="updateTitle"/>
        </div>
        <div class="add-purchase">
          <v-btn
            :style="{color: '#ffffff'}"
            @click="addNewPurchase"
            :color="componentColor.get('primary-color')"
          >add
          </v-btn>
          <v-btn
            :color="componentColor.get('warning-color')"
            :style="{color: '#ffffff'}"
            @click="isAddNewPurchase = !isAddNewPurchase">
            cancel
          </v-btn>
        </div>
      </div>
      </v-card>
      <div v-else>
        <v-btn
          :style="{color: '#ffffff'}"
          :color="componentColor.get('primary-color')"
          @click="isAddNewPurchase= !isAddNewPurchase"
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
  name: 'new-purchase',
  components: {
    MaterialInput
  },
  setup () {
    return {
      addNew: inject('add-new-purchase'),
      componentColor: inject('component-colors')
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
    updateCost (e) {
      this.cost = e.target.value
    },
    updateTitle (e) {
      this.title = e.target.value
    },
    addNewPurchase () {
      this.isAddNewPurchase = false
      this.addNew({
        title: this.title,
        cost: this.cost,
        date: new Date(),
        description: ''
      })
      this.cost = ''
      this.title = ''
    }
  }
}
</script>

<style>
.new-purchase-button-container {
  padding-top: 5px;
  display: flex;
  justify-content: space-around;
}

.new-purchase-button-container div {
  margin-bottom: 20px;
}

.new-purchase-button-container .add-purchase {
  display: flex;
  justify-content: space-evenly;
  align-content: space-between;
  align-items: center;
  width: 300px;

}

.new-purchase-input-container {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center
}

.new-purchase-input-container input {
  height: 40px;
  text-align: center;
}

</style>
