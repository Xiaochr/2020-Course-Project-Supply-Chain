<template>
  <div id="app">
    <img src="../../assets/logo.png">
    <el-card class="index-card">
      <div slot="header">
        权限查询
      </div>
      <el-button type="primary" plain @click="to_material_info">权限查询</el-button>
    </el-card>
    <el-button type="primary" plain @click.native="log_out">退出登录</el-button>
  </div>
</template>

<script>
import modal from '../../components/modal.vue'
export default {
  components: {
    modal
  },
  data() {
    return {
      msg: 'Use Vue 2.0 Today!'
    }
  },
  methods: {
    to_material_info() {
      location.assign('../material_info.html')
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}
body {
  background: #FFF5EE;
}
</style>
