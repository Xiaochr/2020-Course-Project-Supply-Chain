<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
        <div>使用说明，功能说明</div>
      </el-card>
    </el-col>
  </div>
</template>

<script>
import navcol from '../../components/navcol.vue'
import pageheader from '../../components/pageheader.vue'
export default {
  components: {
    navcol,
    pageheader
  },
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
  width: 1000px;
  margin: 50px auto;
}
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
  margin-bottom: 0;
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
