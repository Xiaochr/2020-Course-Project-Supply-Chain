<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
        <el-header>
          <h3>欢迎来到供应链管理系统</h3>
        </el-header>
        <el-divider></el-divider>
        <homepicture></homepicture>
      </el-card>
    </el-col>
  </div>
</template>

<script>
import navcol from '../../components/navcol.vue'
import homepicture from '../../components/homepicture.vue'
export default {
  components: {
    navcol,
    homepicture
  },
  data() {
    return {
      msg: 'Use Vue 2.0 Today!'
    }
  }
}
</script>

<style lang="postcss">
.table-card {
  width: 1000px;
  margin-top: 50px auto;
  text-align: center;
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
