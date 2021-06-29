<template>
  <v-app style="background-color: #fafafa">
    <v-app-bar :style="{backgroundColor: colors.indigo.base, color: '#ffffff'}" app>

      <v-app-bar-nav-icon
        v-if="isCanViewMenuButton"
        @click="this.drawer = !this.drawer"
        :style="{backgroundColor: colors.indigo.base}"
      ></v-app-bar-nav-icon>
      <div v-else style="width: 48px"></div>

      <VAppBarTitle >Login</VAppBarTitle>

    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <section class="container">
        <ul>
          <li class="list-item"
              v-for="item in items"
              :key="item.title"
              @click="handleMenuClick(item.link);"
          >
            {{ item.title }}
          </li>
        </ul>
      </section>

      <section class="container-footer">
        <ul>
          <li class="list-item"
              @click="logout"
          >
            exit
          </li>
        </ul>
      </section>

    </v-navigation-drawer>

    <v-main>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import {
  VMain,
  VApp,
  VAppBar,
  VContainer,
  VAppBarNavIcon,
  VNavigationDrawer,
  VAppBarTitle
} from 'vuetify'
import colors from 'vuetify/lib/util/colors'

export default {
  name: 'App',
  components: {
    VMain,
    VApp,
    VAppBar,
    VContainer,
    VAppBarNavIcon,
    VNavigationDrawer,
    VAppBarTitle
  },
  computed: {
    colors () {
      return colors
    },
    isCanViewMenuButton () {
      return this.$route.path !== '/login'
    }
  },
  methods: {
    handleMenuClick (link) {
      this.drawer = !this.drawer
      this.$router.push(link)
    },
    logout () {
      this.drawer = !this.drawer
      this.$router.replace('/login')
    }
  },
  data: () => ({
    drawer: false,
    group: null,
    items: [
      { title: 'Purchases', icon: 'mdi-view-dashboard', link: '/home' }
    ]
  })
}
</script>

<style>
button .mdi-menu {
  color: white;
}

.container {
  margin: auto;
}

.list-item {
  background: #fff;
  box-shadow: 0 1px 2px #999;
  height: 30px;
  line-height: 30px;
  list-style: none;
  margin: 5px 0;
  text-align: center;
  transform: translateZ(0);
  transition: box-shadow 0.25s ease-in;
}

.list-item:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  cursor: pointer;
}
</style>
