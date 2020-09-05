<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    
    <el-col :span="20">
      <div class="div-img">
        <img src="../../assets/pic1.jpg">
      </div>
    </el-col>
  </div>
</template>

<script>
import navcol from '../../components/navcol.vue'
export default {
  components: {
    navcol
  },
  data() {
    return {
      isCollapse: true,
      msg: 'Use Vue 2.0 Today!'
    }
  },
  methods: {
    to_material_info() {
      location.assign('../material_info.html')
    },
    to_stock() {
      location.assign('../stock.html')
    },
    to_material_order() {
      location.assign('../material_order.html')
    },
    to_out_list() {
      location.assign('../out_list.html')
    },
    log_out() {
      this.$notify({
        title: 'Success',
        message: 'You have successfully logged out. See you!',
        duration: 6000
      })
    }
  }
}
</script>

<style lang="postcss">
.index-card {
  width: 400px;
  margin: 50px auto;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.div-img {
  text-align: center;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  //text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
body {
  background: #F5F5F5;
}
</style>
