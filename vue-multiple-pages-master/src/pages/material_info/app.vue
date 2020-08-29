<template>
  <div id="app">
    <el-card class="table-card">
      <div slot="header">
        原料信息
      </div>
      <el-form>
        <el-form-item label="搜索">
          <el-col :span="18">
            <el-input v-model="searchContent" placeholder="搜索原料名称"></el-input>
          </el-col>
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-form-item>
      </el-form>
      <el-table :data="items" height="250" stripe border>
        <el-table-column prop="mID" label="原料编号"></el-table-column>
        <el-table-column prop="mName" label="原料名称"></el-table-column>
        <el-table-column prop="mType" label="原料类型"></el-table-column>
        <el-table-column prop="price1" label="价格1"></el-table-column>
        <el-table-column prop="price2" label="价格2"></el-table-column>
        <el-table-column prop="price3" label="价格3"></el-table-column>
        <el-table-column prop="unit" label="单位"></el-table-column>
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
    <el-button type="primary" plain @click="addMaterial()">添加</el-button>
    <el-button type="primary" plain @click="backHome">返回</el-button>
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
          <el-col :span="12">
            <el-form-item label="原料编号">
              <el-input v-model="cur_item.mID" placeholder="Please input id" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <el-form-item label="原料名称">
              <el-input v-model="cur_item.mName" placeholder="Please input name"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="7">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="原料类型">
              <el-input v-model="cur_item.mType" placeholder="Please input type"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="价格1">
              <el-input v-model="cur_item.price1" placeholder="Please input price"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="价格2">
              <el-input v-model="cur_item.price2" placeholder="Please input price"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="价格3">
              <el-input v-model="cur_item.price3" placeholder="Please input price"></el-input>
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
              <el-input v-model="cur_item.shelfLife" placeholder="Please input"></el-input>
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
export default {
  data() {
    return {
      items: [],
      cur_item: {},
      orig_item: {},
      curIndex: 1,
      curLen: 0,
      delVisible: false,
      addVisible: false,
      searchContent: '',
      addFlag: true,
      refreshFlag: 0
    }
  },
  methods: {
    backHome() {
      location.assign('../index.html')
    },
    closeAdd() {
      this.cur_item = Object.assign({}, this.orig_item)
      this.addVisible = false
      this.refreshFlag ++
    },
    closeDel() {
      this.delVisible = false
    },
    getItems() {
      this.$http.get('http://127.0.0.1:8000/backend/info/').then(
        function(data) {
          console.log(data);
          this.items = data.body
          this.curLen = this.items.length
        }
      )
    },
    editMaterial(row, curIndex) {
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
        }
      )
      this.delVisible = false
      this.$notify({
        title: 'Success',
        message: 'Success!',
        duration: 6000
      })
    },
    saveMaterial() {
      this.$http.post('http://127.0.0.1:8000/backend/info/add/', this.cur_item, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.refreshFlag ++
        }
      ),
      this.addVisible = false,
      this.$notify({
        title: 'Success',
        message: 'Success!',
        duration: 6000
      })
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
          //this.refreshFlag ++
          this.items = data.body
        }
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
