<template>
  <div id="app">
    <el-card class="index-card">
      <div slot="header">
        权限查询界面
      </div>
    </el-card>
    <el-button type="primary" plain @click="backHome()">返回</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: []
    }
  },
  methods: {
    backHome() {
      location.assign('../index.html')
    }
  }
}
</script>

<style>
.table-card {
  width: 1200px;
  margin: 100px auto;
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
