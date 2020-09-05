<template>
  <div id="app">
    <el-card class="table-card">
      <div slot="header">
        出库清单
      </div>
      <el-form>
        <el-col :span="10">
          <el-form-item label="订单状态">
            <el-select v-model="stateFilter" placeholder="请选择">
              <el-option label="所有" value=-1></el-option>
              <el-option label="已出库" value=0></el-option>
              <el-option label="进行中" value=1></el-option>
              <el-option label="已取消" value=2></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="10">
          <el-form-item label="订单类型">
            <el-select v-model="typeFilter" placeholder="请选择">
              <el-option label="所有" value=-1></el-option>
              <el-option label="堂食" value=0></el-option>
              <el-option label="外卖" value=1></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-form>
      <el-table :data="searchVisible?temp_list:items" height="250" stripe border>
        <el-table-column prop="order_id" label="订单编号"></el-table-column>
        <el-table-column prop="order_type" label="订单类型"></el-table-column>
        <el-table-column prop="koState" label="订单状态"></el-table-column>
        <el-table-column label="查看">
          <template>
            <el-button type="primary" size="mini" @click="orderDetail()">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <el-button type="primary" plain @click="backHome">返回</el-button>
    <el-dialog title="订单详情" :visible="detailVisible" @close="closeDetail()">
      <el-table :data="order_detail" height="200" stripe border>
        <el-table-column prop="order_id" label="订单编号"></el-table-column>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="mName" label="原料名称"></el-table-column>
        <el-table-column prop="amount" label="原料数量"></el-table-column>
      </el-table>
      <span slot="footer">
        <el-button type="primary" @click="closeDetail()">取消</el-button>
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
      cur_item: {},
      orig_item: {},
      curIndex: 1,
      stateFilter: "所有",
      typeFilter: "所有",
      detailVisible: false,
      addVisible: false,
      searchVisible: false,
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
      this.$http.get('http://127.0.0.1:8000/backend/korder/').then(
        function(data) {
          console.log(data);
          this.items = data.body
        }
      )
    },
    orderDetail() {
      this.detailVisible = true
      this.$http.post('http://127.0.0.1:8000/backend/korder/detail/', this.cur_item["moID"], {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.order_detail = data.body
        }
      )
    },
    closeDetail() {
      this.detailVisible = false
    }
  },
  watch: {
    refreshFlag() {
      this.getItems()
    }
  },
  mounted() {
    this.getItems()
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
  background: #F5F5F5;
}
</style>
