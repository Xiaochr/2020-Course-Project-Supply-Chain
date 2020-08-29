<template>
  <div id="app">
    <el-card class="table-card">
      <div slot="header">
        原料库存
      </div>
      <el-form>
        <el-form-item label="搜索原料名称">
          <el-col :span="18">
            <el-input v-model="searchContent" placeholder="search"></el-input>
          </el-col>
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-form-item>
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
      <el-table :data="items" height="250" stripe border>
        <el-table-column prop="moID" label="订单批次"></el-table-column>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="mName" label="原料名称"></el-table-column>
        <el-table-column prop="arrival" label="入库日期"></el-table-column>
        <el-table-column prop="stock" label="库存量"></el-table-column>
        <el-table-column prop="mState" label="状态" :formatter="stateFormat"></el-table-column>
      </el-table>
    </el-card>
    <el-button type="primary" plain @click="countInv()">盘库</el-button>
    <el-button type="primary" plain @click="backHome">返回</el-button>
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
        <el-button type="success" @click="closeCount()">提交</el-button>
        <el-button type="primary" @click="closeCount()">取消</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      temp_list: [],
      inv_list: [],
      cur_item: {},
      orig_item: {},
      curIndex: 1,
      filter: -1,
      countVisible: false,
      searchContent: '',
      refreshFlag: 0,
      addFlag: true
    }
  },
  methods: {
    backHome() {
      location.assign('../index.html')
    },
    getItems() {
      this.$http.get('http://127.0.0.1:8000/backend/stock/').then(
        function(data) {
          console.log(data);
          this.items = data.body
        }
      )
    },
    getFiltered() {
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
    countInv() {
      this.countVisible = true
      this.$http.get('http://127.0.0.1:8000/backend/stock/count/').then(
        function(data) {
          console.log(data);
          this.inv_list = data.body
        }
      )
    },
    submitCount() {
      this.$http.post('http://127.0.0.1:8000/backend/stock/receive/', this.inv_list, {emulateJSON: true}).then(
        function(data) {
          console.log(data);
          this.items = data.body
        }
      )
    },
    closeCount() {
      this.countVisible = false
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
    searchName() {
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
  width: 800px;
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
</style>
