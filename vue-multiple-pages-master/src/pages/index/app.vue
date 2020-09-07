<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
        <div>欢迎来到供应链管理系统！</div>
        <img src="../../assets/logo.png">
        <div>简介文本</div>
      </el-card>
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
      msg: 'Use Vue 2.0 Today!'
    }
  }
}
</script>

<style lang="postcss">
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.table-card {
  width: 1000px;
  margin-top: 50px auto;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 20px;
}
body {
  background: #F5F5F5;
}
</style>
