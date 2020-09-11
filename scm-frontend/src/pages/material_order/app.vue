<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
    <el-card class="table-card">
      <el-page-header @back="backHome" content="原料订单"></el-page-header>
      <el-divider></el-divider>
      <el-form>
        <el-col :span="20">
          <el-form-item label="订单状态">
            <el-select v-model="filter" placeholder="请选择">
              <el-option label="所有" value=-1></el-option>
              <el-option label="运输中" value=0></el-option>
              <el-option label="已入库" value=1></el-option>
              <el-option label="已取消" value=2></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="4">
          <el-button type="primary" plain icon="el-icon-circle-plus-outline" @click="addOrder()">新增订单</el-button>
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
    </el-col>

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
        <el-table-column prop="moID_id" label="订单编号"></el-table-column>
        <el-table-column prop="mID_id" label="原料编号"></el-table-column>
        <el-table-column prop="mName" label="原料名称"></el-table-column>
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
        <el-table-column prop="mName" label="原料名称"></el-table-column>
        <el-table-column prop="amount" label="原料数量"></el-table-column>
        <el-table-column prop="unit" label="原料单位"></el-table-column>
        <el-table-column prop="price" label="原料价格"></el-table-column>
        <el-table-column label="删除">
          <template slot-scope="scope">
            <el-button type="danger" size="mini" @click="delMaterial(scope.$index)">删除</el-button>
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
        <el-row>
        <el-col :span="10">
          <el-form-item label="原料名称">
            <el-select v-model="cur_material.mName" filterable placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.mName"
                :label="item.mName"
                :value="item.mName">
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="4">
          <el-form-item></el-form-item>
        </el-col>
        <el-col :span="10">
          <el-form-item label="所需数量">
            <el-input type="number" v-model="cur_material.amount" placeholder="请输入数量"></el-input>
          </el-form-item>
        </el-col>
        </el-row>
      </el-form>
      <span slot="footer">
        <el-button type="success" @click="handleMAdd()">提交</el-button>
        <el-button type="primary" @click="closeMAdd()">取消</el-button>
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
      items: [], //存储一系列订单信息
      order_detail: [], //存储单个订单中各种原料的信息
      cur_material: {}, //order_detail中单个原料的信息
      morder_post: {},
      options: [],
      cur_moID: 0,
      filter: "所有",
      detailVisible: false,
      cdetailVisible: false,
      addVisible: false,
      addMVisible: false,
      searchContent: '',
      refreshFlag: 0
    }
  },
  methods: {
    backHome() {// 返回主页
      location.assign('../index.html')
    },
    getItems() {// 向后台发送请求，获取所有原料订单信息
      this.$http.get('http://127.0.0.1:8000/backend/morder/').then(
        function(data) {
          console.log(data);
          this.items = data.body
        }
      )
    },
    getFiltered() {// 向后台发送请求，获取筛选后的原料订单信息
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
    orderDetail(row) {// 显示订单详情对话框
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
    closeDetail() {// 关闭订单详情对话框
      this.detailVisible = false
    },
    closeCDetail() {// 关闭订单详情对话框
      this.cdetailVisible = false
    },
    confirmArrival() {// 确认到库 not finished
      this.cdetailVisible = false
      console.log(this.order_detail[0])
      this.$http.post('http://127.0.0.1:8000/backend/morder/stockin/', {'moID': this.order_detail[0].moID_id}, {emulateJSON: true}).then(
        function(data) {
          console.log(data);
          this.$notify({
            title: '成功',
            message: '确认到库成功！',
            duration: 6000
          })
        }
      )
    },
    addOrder() {// 添加新订单
      this.addVisible = true
      this.cur_moID = parseInt(this.items[this.items.length - 1].moID) + 1
      this.order_detail = []
    },
    confirmOrder() {// 确认下单 not finished
      this.addVisible = false
      this.morder_post = {'moID': this.cur_moID, 'data': this.order_detail}
      console.log(this.order_detail)
      this.$http.post('http://127.0.0.1:8000/backend/morder/add/', this.order_detail).then(
        function(data) {
          console.log(data);
          this.items = data.body
          this.refreshFlag ++
        }
      )
    },
    closeAdd() {// 关闭添加新订单对话框
      this.addVisible = false
      this.order_detail = []
    },
    addMaterial() {//not finished 在新增订单中打开添加原料窗口
      this.addMVisible = true
      this.$http.get('http://127.0.0.1:8000/backend/info/').then(
        function(data) {
          console.log(data);
          this.options = data.body
        }
      )
    },
    delMaterial(index) {// 删除原料
      this.order_detail.splice(index)
    },
    handleMAdd() {// 确认添加原料 not finished
      //post_data = {'mName': this.cur_material.mName, 'amount': this.cur_material.amount, 'moID': this.cur_moID}
      this.cur_material.moID = this.cur_moID
      this.$http.post('http://127.0.0.1:8000/backend/morder/detail/add/', this.cur_material, {emulateJSON: true}).then(
        function(data) {
          console.log(data);
          this.order_detail.push(data.body)
        }
      )
      this.addMVisible = false
    },
    closeMAdd() {// 关闭添加原料对话框
      this.cur_material = {}
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
