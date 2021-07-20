<template>
  <div class="material-input-container">
    <fieldset class="material">
      <input :value="value" :type=type autocomplete="off" @input="updater" :inputmode="inputMode" required>
      <hr>
      <label>{{ label }}</label>
    </fieldset>
  </div>
</template>
<script>
import colors from 'vuetify/lib/util/colors'

export default {
  name: 'material-input',
  props: {
    type: {
      type: String,
      required: true
    },
    label: {
      type: String,
      required: true
    },
    updater: {
      type: Function,
      required: true
    },
    inputMode: {
      type: String,
      required: true
    },
    value: {
      type: String,
      default: ''
    }
  },
  computed: {
    colors () {
      return colors
    }
  }
}
</script>
<style>
form {
  margin: 20px;
  padding: 20px;
  background: #fff;
}
.material {
  position: relative;
  padding: 0;
  margin: 5px;
  border: none;
  overflow: visible;
}
.material input {
  box-sizing: border-box;
  width: 100%;
  padding: 12px 10px 8px;
  border: none;
  border-radius: 0;
  box-shadow: none;
  border-bottom: 1px solid #ddd;
  font-size: 120%;
  outline: none;
  cursor: text;
}
.material input::-webkit-input-placeholder {
  -webkit-transition: color 300ms ease;
  transition: color 300ms ease;
}
.material input:not(:focus)::-webkit-input-placeholder {
  color: transparent;
}
.material hr {
  content: "";
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 2px;
  border: none;
  background: #3f51b5;
  font-size: 1px;
  will-change: transform, visibility;
  transition: all 200ms ease-out;
  transform: scaleX(0);
  visibility: hidden;
  z-index: 10;
}
.material input:focus ~ hr {
  transform: scaleX(1);
  visibility: visible;
}
.material label {
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 120%;
  color: #3f51b5;
  transform-origin: 0 -150%;
  transition: transform 300ms ease;
  pointer-events: none;
}
.material input:focus ~ label,
.material input:valid ~ label {
  transform: scale(0.6);
}

</style>
