<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
      <el-page-header @back="backHome" content="数据表权限"></el-page-header>
      <el-divider></el-divider>

      <el-row>
        <el-col :span="8">
          <el-select v-model="searchUser" filterable placeholder="用户名">
            <el-option
              v-for="item in temp_items"
              :key="item.user"
              :label="item.user"
              :value="item.user">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="8">
          <el-select
            v-model="searchTable"
            filterable
            collapse-tags
            placeholder="数据表名">
            <el-option
              v-for="item in temp_items"
              :key="item.table"
              :label="item.table"
              :value="item.table">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="4">
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-col>
      </el-row>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="user" label="用户名"></el-table-column>
        <el-table-column prop="table" label="数据表名"></el-table-column>
        <el-table-column prop="Select" label="Select" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="insert" label="Insert" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="Update" label="Update" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="Delete" label="Delete" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="Drop" label="Drop" :formatter="stateFormat"></el-table-column>
        <el-table-column label="修改权限">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" icon="el-icon-edit" @click="editAuth(scope.row)">编辑</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    </el-col>

    <el-dialog title="修改权限" :visible="editVisible" @close="closeEdit()">
      <el-form>
        <el-row>
          <el-col :span="8">
            <el-form-item label="用户名">
              <el-input type="text" v-model="cur_item.user" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="7">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="数据表名">
              <el-input type="text" v-model="cur_item.table" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="Select权限">
              <el-select v-model="cur_item.Select" :formatter="stateFormat">
                <el-option label="有(Y)" value="Y"></el-option>
                <el-option label="无(N)" value="N"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Update权限">
              <el-select v-model="cur_item.Update">
                <el-option label="有(Y)" value="Y"></el-option>
                <el-option label="无(N)" value="N"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Delete权限">
              <el-select v-model="cur_item.Delete">
                <el-option label="有(Y)" value="Y"></el-option>
                <el-option label="无(N)" value="N"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="Insert权限">
              <el-select v-model="cur_item.insert">
                <el-option label="有(Y)" value="Y"></el-option>
                <el-option label="无(N)" value="N"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Drop权限">
              <el-select v-model="cur_item.Drop">
                <el-option label="有(Y)" value="Y"></el-option>
                <el-option label="无(N)" value="N"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="所有权限">
              <el-select v-model="cur_item.all">
                <el-option label="有(Y)" value="Y"></el-option>
                <el-option label="无(N)" value="N"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <span slot="footer">
        <el-button type="success" @click="saveEdit()">提交</el-button>
        <el-button type="primary" @click="resetEdit()">重置</el-button>
        <el-button type="primary" @click="closeEdit()">取消</el-button>
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
      items: [],
      temp_items: [
        {'user': 'agent1', 'table': 'test_table'}
      ],
      cur_item: {},
      orig_item: {},
      searchUser: "",
      searchTable: "",
      editVisible: false,
      refreshFlag: 0
    }
  },
  methods: {
    backHome() {
      location.assign('../homepage.html')
    },
    getItems() {
      this.$http.get('http://127.0.0.1:8000/backend/table/').then(
        function(data) {
          console.log(data);
          this.items = data.body
        }
      )
      .catch(
        function(data) {
          console.log(data)
          this.$notify({
            title: '错误',
            message: '获取数据失败！',
            duration: 6000
          })
        }
      )
    },
    searchName() {// 模糊搜索
      this.$http.post('http://127.0.0.1:8000/backend/table/search/', {'searchUser': this.searchUser, 'searchTable': this.searchTable}, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.items = data.body
        }
      )
      .catch(
        function(data) {
          console.log(data)
          this.$notify({
            title: '错误',
            message: '搜索失败！',
            duration: 6000
          })
        }
      )
    },
    editAuth(row) {
      this.editVisible = true
      this.cur_item = row
      this.orig_item = Object.assign({}, this.cur_item)
    },
    saveEdit() { // not finished
      this.$http.post('http://127.0.0.1:8000/backend/table/priv/', this.cur_item, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.refreshFlag ++
          this.editVisible = false
          this.$notify({
            title: '成功',
            message: '修改成功！',
            duration: 6000
          })
        }
      )
      .catch(
        function(data) {
          console.log(data)
          this.$notify({
            title: '错误',
            message: '操作失败！',
            duration: 6000
          })
        }
      )
    },
    resetEdit() {
      this.cur_item = Object.assign({}, this.orig_item)
    },
    closeEdit() {
      this.editVisible = false
    },
    stateFormat(row, column, cellValue) {
      if(cellValue == 'N') {
        return '无'
      }
      else if(cellValue == 'Y') {
        return '有'
      }
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
