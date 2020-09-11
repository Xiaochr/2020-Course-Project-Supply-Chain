<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
    <el-card class="table-card">
      <el-page-header @back="backHome" content="原料库存"></el-page-header>
      <el-divider></el-divider>
      
      <el-row>
        <el-col :span="16">
          <el-input v-model="searchContent" @keyup.enter.native="searchName()" placeholder="搜索原料名称"></el-input>
        </el-col>
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-box" plain @click="countInv()">盘库</el-button>
        </el-col>
      </el-row>
      <el-form>
        <el-col :span="10">
          <el-form-item label="原料状态">
            <el-select v-model="filter" placeholder="请选择">
              <el-option label="所有" value=-1></el-option>
              <el-option label="在仓库" value=0></el-option>
              <el-option label="已出库" value=1></el-option>
              <el-option label="被预订" value=2></el-option>
              <el-option label="已过期" value=3></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-form>

      <el-table class="data-table" :data="items" height="300" stripe border>
        <el-table-column prop="moID" label="订单批次"></el-table-column>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="mName" label="原料名称"></el-table-column>
        <el-table-column prop="arrival" label="入库日期"></el-table-column>
        <el-table-column prop="stock" label="库存量"></el-table-column>
        <el-table-column prop="mState" label="状态" :formatter="stateFormat"></el-table-column>
      </el-table>
    </el-card>
    </el-col>
    
    <el-dialog title="盘点库存" :visible="countVisible" @close="closeCount()">
      <el-table :data="inv_list" height="200" stripe border>
        <el-table-column prop="moID" label="订单批次"></el-table-column>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="mName" label="原料名称"></el-table-column>
        <el-table-column prop="arrival" label="入库日期"></el-table-column>
        <el-table-column prop="stock" label="库存量"></el-table-column>
        <el-table-column prop="mState" label="状态"></el-table-column>
      </el-table>
      <span slot="footer">
        <el-button type="success" @click="submitCount()">提交</el-button>
        <el-button type="primary" @click="closeCount()">关闭</el-button>
      </span>
    </el-dialog>
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
      items: [], //存储要在表格中显示的数据
      inv_list: [], //存储盘库得到的过期原料列表
      filter: "所有", //筛选
      countVisible: false, //是否显示盘库对话框
      searchContent: '', //存储需要搜索的内容
      refreshFlag: 0 //是否刷新页面
    }
  },
  methods: {
    backHome() {// 返回主页
      location.assign('../index.html')
    },
    getItems() {// 向后台发送请求，获取所有原料库存信息
      this.$http.get('http://127.0.0.1:8000/backend/stock/').then(
        function(data) {
          console.log(data);
          this.items = data.body
        }
      )
    },
    getFiltered() {// 向后台发送请求，获取筛选后的原料库存信息
      if(this.filter==-1) {
        this.$http.get('http://127.0.0.1:8000/backend/stock/').then(
          function(data) {
            console.log(data);
            this.items = data.body
          }
        )
      }
      else {
        this.$http.post('http://127.0.0.1:8000/backend/stock/filter/', {'state': this.filter}, {emulateJSON: true}).then(
          function(data) {
            console.log(data);
            this.items = data.body
          }
        )
      }
    },
    countInv() {// 盘库
      this.countVisible = true
      this.$http.get('http://127.0.0.1:8000/backend/stock/count/').then(
        function(data) {
          console.log(data);
          this.inv_list = data.body
        }
      )
    },
    submitCount() {// 向财务组发送盘库清单
      this.$http.post('http://127.0.0.1:8000/backend/stock/send/', this.inv_list, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.countVisible = false
          this.refreshFlag ++
          this.$notify({
            title: '成功',
            message: '成功提交盘库清单！',
            duration: 6000
          })
        }
      )
    },
    closeCount() {// 关闭盘库页面
      this.countVisible = false
      this.refreshFlag ++
    },
    stateFormat(row) {
      if(row.mState == 0) {
        return '在仓库'
      }
      else if(row.mState == 1) {
        return '已出库'
      }
      else if(row.mState == 2) {
        return '被预订'
      }
      else {
        return '已过期'
      }
    },
    searchName() {// 搜索功能
      this.$http.post('http://127.0.0.1:8000/backend/stock/search/', {'mName': this.searchContent}, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.items = data.body
        }
      )
    }
  },
  watch: {
    refreshFlag() {
      this.getItems()
    },
    filter() {
      this.getFiltered()
    }
  },
  mounted() {
    this.getItems()
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
