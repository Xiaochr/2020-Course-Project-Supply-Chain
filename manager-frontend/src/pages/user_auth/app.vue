<template>
  <div id="app">
    <pageheader></pageheader>
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
      <el-page-header @back="backHome" content="用户权限"></el-page-header>
      <el-divider></el-divider>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="mID" label="表名"></el-table-column>
        <el-table-column prop="mName" label="用户名"></el-table-column>
        <el-table-column prop="mType" label="增加"></el-table-column>
        <el-table-column prop="price1" label="删除"></el-table-column>
        <el-table-column prop="price2" label="查询"></el-table-column>
        <el-table-column prop="price3" label="修改"></el-table-column>
        <el-table-column prop="unit" label="拥有者"></el-table-column>
        <el-table-column label="编辑">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" icon="el-icon-edit" @click="editMaterial(scope.row, scope.$index)">编辑</el-button>
          </template>
        </el-table-column>
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
