<template>
  <div id="app">
    <pageheader></pageheader>
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
      <el-page-header @back="backHome" content="表格概览"></el-page-header>
      <el-divider></el-divider>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="mID" label="拥有者"></el-table-column>
        <el-table-column prop="mName" label="表名"></el-table-column>
        <el-table-column prop="mType" label="用户"></el-table-column>
        <el-table-column prop="price1" label="权限"></el-table-column>
      </el-table>
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
      location.assign('../homepage.html')
    }
  }
}
</script>

<style>
.table-card {
  width: 1000px;
  margin-top: 50px auto;
}
.data-table {
  margin-top: 500px auto;
}
.div-text {
  text-align: center;
}
.el-row {
  margin-bottom: 20px;
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
