<template>
  <div id="app">
    <el-card class="table-card">
      <div slot="header">
        原料订单
      </div>
      <el-form>
        <el-col :span="10">
          <el-form-item label="订单状态">
            <el-select v-model="filter" placeholder="请选择">
              <el-option label="所有" value=-1></el-option>
              <el-option label="运输中" value=0></el-option>
              <el-option label="已入库" value=1></el-option>
              <el-option label="已取消" value=2></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-form>
      <el-table :data="items" height="250" stripe border>
        <el-table-column prop="moID" label="订单编号"></el-table-column>
        <el-table-column prop="oDate" label="下单日期"></el-table-column>
        <el-table-column prop="aDate" label="（预计）到达日期"></el-table-column>
        <el-table-column prop="moState" label="订单状态" :formatter="stateFormat"></el-table-column>
        <el-table-column label="查看">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" @click="orderDetail(scope.row)">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <el-button type="primary" plain @click="addOrder()">新增订单</el-button>
    <el-button type="primary" plain @click="backHome">返回</el-button>
    <el-dialog title="订单详情" :visible="detailVisible" @close="closeDetail()">
      <el-table :data="order_detail" height="200" stripe border>
        <el-table-column prop="moID" label="订单编号"></el-table-column>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="amount" label="原料数量"></el-table-column>
        <el-table-column prop="unit" label="原料单位"></el-table-column>
        <el-table-column prop="price" label="原料价格"></el-table-column>
      </el-table>
      <span slot="footer">
        <el-button type="primary" @click="closeDetail()">返回</el-button>
      </span>
    </el-dialog>
    <el-dialog title="订单详情" :visible="cdetailVisible" @close="closeCDetail()">
      <el-table :data="order_detail" height="200" stripe border>
        <el-table-column prop="moID" label="订单编号"></el-table-column>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="amount" label="原料数量"></el-table-column>
        <el-table-column prop="unit" label="原料单位"></el-table-column>
        <el-table-column prop="price" label="原料价格"></el-table-column>
      </el-table>
      <span slot="footer">
        <el-button type="success" @click="confirmArrival()">确认到库</el-button>
        <el-button type="primary" @click="closeCDetail()">返回</el-button>
      </span>
    </el-dialog>
    <el-dialog title="新增订单" :visible="addVisible" @close="closeAdd()">
      <el-table :data="order_detail" height="200" stripe border>
        <el-table-column prop="moID" label="订单编号"></el-table-column>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="amount" label="原料数量"></el-table-column>
        <el-table-column prop="unit" label="原料单位"></el-table-column>
        <el-table-column prop="price" label="原料价格"></el-table-column>
        <el-table-column label="修改">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" @click="editMaterial(scope.row)">修改</el-button>
          </template>
        </el-table-column>
      </el-table>
      <span slot="footer">
        <el-button type="success" @click="addMaterial()">添加原料</el-button>
        <el-button type="success" @click="confirmOrder()">提交</el-button>
        <el-button type="primary" @click="closeAdd()">取消</el-button>
      </span>
    </el-dialog>
    <el-dialog title="添加原料" :visible="addMVisible" @close="closeMAdd()">
      <el-form>
        <el-form-item label="原料名称">
          <el-input v-model="cur_material.mName" placeholder="Please input material name"></el-input>
        </el-form-item>
        <el-form-item label="所需数量">
          <el-input v-model="cur_material.amount" placeholder="Please input amount"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer">
        <el-button type="success" @click="handleMAdd()">提交</el-button>
        <el-button type="primary" @click="closeMAdd()">取消</el-button>
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
      order_detail: [],
      cur_material: {},
      cur_detail: [],
      curIndex: 1,
      filter: "所有",
      detailVisible: false,
      cdetailVisible: false,
      addVisible: false,
      addMVisible: false,
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
      this.$http.get('http://127.0.0.1:8000/backend/morder/').then(
        function(data) {
          console.log(data);
          this.items = data.body
        }
      )
    },
    getFiltered() {
      if(this.filter==-1) {
        this.$http.get('http://127.0.0.1:8000/backend/morder/').then(
          function(data) {
            console.log(data);
            this.items = data.body
          }
        )
      }
      else {
        this.$http.post('http://127.0.0.1:8000/backend/morder/filter/', {'state': this.filter}, {emulateJSON: true}).then(
          function(data) {
            console.log(data);
            this.items = data.body
          }
        )
      }
    },
    orderDetail(row) {
      if(row.moState==0) {
        this.cdetailVisible = true
      }
      else {
        this.detailVisible = true
      }
      this.$http.post('http://127.0.0.1:8000/backend/morder/detail/', row, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.order_detail = data.body
        }
      )
    },
    closeDetail() {
      this.detailVisible = false
    },
    closeCDetail() {
      this.cdetailVisible = false
    },
    confirmArrival() {
      this.cdetailVisible = false
    },
    addOrder() {
      this.addVisible = true
    },
    confirmOrder() {
      this.addVisible = false
    },
    closeAdd() {
      this.addVisible = false
    },
    addMaterial() {
      this.addMVisible = true
    },
    editMaterial(row) {
      this.addMVisible = true
      this.cur_material.mName = row.mName
      this.cur_material.amount = row.amount
    },
    handleMAdd() {
      this.addMVisible = false
    },
    closeMAdd() {
      this.addMVisible = false
    },
    stateFormat(row) {
      if(row.moState == 0) {
        return '运输中'
      }
      else if(row.moState == 1) {
        return '已入库'
      }
      else {
        return '已取消'
      }
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
</style>
