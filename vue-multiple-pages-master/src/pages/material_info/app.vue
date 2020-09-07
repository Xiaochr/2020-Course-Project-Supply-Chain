<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>

    <el-col :span="20">
    <el-card class="table-card">
      <el-page-header @back="backHome" content="原料信息"></el-page-header>
      <el-divider></el-divider>
      <el-row>
        <el-col :span="16">
          <el-input v-model="searchContent" placeholder="搜索原料名称"></el-input>
        </el-col>
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-circle-plus-outline" plain @click="addMaterial()">添加原料</el-button>
        </el-col>
      </el-row>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="mName" label="原料名称"></el-table-column>
        <el-table-column prop="mType" label="原料类型"></el-table-column>
        <el-table-column prop="price1" label="价格1"></el-table-column>
        <el-table-column prop="price2" label="价格2"></el-table-column>
        <el-table-column prop="price3" label="价格3"></el-table-column>
        <el-table-column prop="unit" label="单位"></el-table-column>
        <el-table-column prop="shelfLife" label="保质期/天"></el-table-column>
        <el-table-column label="编辑">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" icon="el-icon-edit" @click="editMaterial(scope.row, scope.$index)">编辑</el-button>
          </template>
        </el-table-column>
        <el-table-column label="删除">
          <template slot-scope="scope">
            <el-button type="danger" size="mini" icon="el-icon-delete" @click="delMaterial(scope.row, scope.$index)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    </el-col>

    <el-dialog title="提示" :visible="delVisible" @close="closeDel()">
      <span>确认删除？</span>
      <span slot="footer">
        <el-button type="danger" @click="handleDel()">删除</el-button>
        <el-button type="primary" @click="delVisible = false">取消</el-button>
      </span>
    </el-dialog>

    <el-dialog :title="addFlag?'新增原料':'修改原料'" :visible="addVisible" @close="closeAdd()">
      <el-form>
        <el-row>
          <el-col :span="8">
            <el-form-item label="原料名称">
              <el-input type="text" v-model="cur_item.mName" placeholder="Please input name" oninput="if(value.length>10) value=value.slice(0,10)"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="7">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="原料类型">
              <el-select v-model="cur_item.mType">
                <el-option label="肉类" value="肉类"></el-option>
                <el-option label="海鲜" value="海鲜"></el-option>
                <el-option label="蔬菜" value="蔬菜"></el-option>
                <el-option label="主食" value="主食"></el-option>
                <el-option label="其他" value="其他"></el-option>
                <el-option label="酒水" value="酒水"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="价格1">
              <el-input type="number" v-model="cur_item.price1" placeholder="Please input price" min=0></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="价格2">
              <el-input type="number" v-model="cur_item.price2" placeholder="Please input price" min=0></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="价格3">
              <el-input type="number" v-model="cur_item.price3" placeholder="Please input price" min=0></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <el-form-item label="单位">
              <el-input v-model="cur_item.unit" placeholder="Please input unit"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="7">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="保质期">
              <el-input type="number" v-model="cur_item.shelfLife" placeholder="Please input"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <el-form-item label="安全库存策略">
              <el-select v-model="cur_item.safetyType">
                <el-option label="平均" value=0></el-option>
                <el-option label="最高" value=1></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="7">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="出库策略">
              <el-select v-model="cur_item.outType">
                <el-option label="FIFO" value=0></el-option>
                <el-option label="LIFO" value=1></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <span slot="footer">
        <el-button type="success" @click="saveMaterial()">提交</el-button>
        <el-button type="primary" @click="resetMaterial()">重置</el-button>
        <el-button type="primary" @click="closeAdd()">取消</el-button>
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
      cur_item: {}, //当前的一条记录
      orig_item: {}, //修改时暂存原先未修改的记录
      curIndex: 1, //当前的index
      curLen: 0, //当前数据数量
      delVisible: false, //是否显示删除对话框
      addVisible: false, //是否显示添加对话框
      searchContent: '', //存储需要搜索的内容
      addFlag: true, //判断需要弹出的是修改对话框还是添加对话框
      refreshFlag: 0 //是否刷新页面
    }
  },
  methods: {
    backHome() { //返回主页
      location.assign('../index.html')
    },
    closeAdd() { //关闭添加对话框
      this.cur_item = Object.assign({}, this.orig_item)
      this.addVisible = false
      this.refreshFlag ++
    },
    closeDel() { //关闭删除对话框
      this.delVisible = false
    },
    getItems() { //向后台发送请求，获取所有原料信息
      this.$http.get('http://127.0.0.1:8000/backend/info/').then(
        function(data) {
          console.log(data);
          this.items = data.body
          this.curLen = this.items[this.items.length - 1].mID
        }
      )
    },
    editMaterial(row, curIndex) { //弹出编辑对话框
      this.addVisible = true,
      this.addFlag = false,
      this.cur_item = row,
      this.orig_item = Object.assign({}, this.cur_item),
      this.curIndex = curIndex
    },
    delMaterial(row, curIndex) {
      this.delVisible = true,
      this.cur_item = row,
      this.curIndex = curIndex
    },
    handleDel() {
      this.$http.post('http://127.0.0.1:8000/backend/info/del/', this.cur_item, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.refreshFlag ++
          this.delVisible = false
          this.$notify({
            title: 'Success',
            message: 'Successfully deleted!',
            duration: 6000
          })
        },
        this.$notify({
          title: 'Error',
          message: 'Delete error!',
          duration: 6000
        })
      )
    },
    saveMaterial() {
      this.$http.post('http://127.0.0.1:8000/backend/info/add/', this.cur_item, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.refreshFlag ++
          this.addVisible = false,
          this.$notify({
            title: 'Success',
            message: 'Successfully saved!',
            duration: 6000
          })
        },
        this.$notify({
          title: 'Error',
          message: 'Save error! No empty values, please. ',
          duration: 6000
        })
      )
    },
    resetMaterial() {
      this.cur_item = Object.assign({}, this.orig_item)
      console.log(this.cur_item)
      console.log(this.orig_item)
    },
    addMaterial() {
      this.addVisible = true,
      this.addFlag = true,
      this.cur_item = {},
      this.curLen ++,
      this.cur_item.mID = this.curLen,
      this.orig_item = {},
      this.curIndex = this.items.length
    },
    searchName() {
      this.$http.post('http://127.0.0.1:8000/backend/info/search/', {'mName': this.searchContent}, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.items = data.body
        },
        this.$notify({
          title: 'Error',
          message: 'Search error!',
          duration: 6000
        })
      )
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
