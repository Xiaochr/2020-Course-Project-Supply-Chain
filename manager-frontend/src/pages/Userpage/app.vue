<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
      <el-page-header @back="backHome" content="用户权限"></el-page-header>
      <el-divider></el-divider>
      <el-row>
        <el-col :span="16">
          <el-input v-model="searchUser" @keyup.enter.native="searchUsername()" placeholder="搜索用户名"></el-input>
        </el-col>
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-search" plain @click="searchUsername()">搜索</el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-circle-plus-outline" plain @click="addUser()">添加用户</el-button>
        </el-col>
      </el-row>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="user" label="用户"></el-table-column>
        <el-table-column prop="account_locked" label="是否锁定" :formatter="stateFormat"></el-table-column>
        <el-table-column label="锁定/解锁">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" icon="el-icon-lock" @click="lockUser(scope.row)">操作</el-button>
          </template>
        </el-table-column>
        <el-table-column label="修改密码">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" icon="el-icon-edit" @click="editUser(scope.row)">修改</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    </el-col>

    <el-dialog title="修改用户密码" :visible="editVisible" @close="closeEdit()">
      <el-form>
        <el-row>
          <el-col :span="8">
            <el-form-item label="用户名">
              <el-input type="text" v-model="cur_item.user" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="4">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="密码">
              <el-input type="text" v-model="cur_item.pswd"></el-input>
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

    <el-dialog title="添加用户" :visible="addVisible" @close="closeAdd()">
      <el-form>
        <el-row>
          <el-col :span="6">
            <el-form-item label="用户名">
              <el-input type="text" v-model="cur_item.user"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="密码">
              <el-input type="text" v-model="cur_item.pswd"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="是否锁定">
              <el-select v-model="cur_item.account_locked">
                <el-option label="是(Y)" value="Y"></el-option>
                <el-option label="否(N)" value="N"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <span slot="footer">
        <el-button type="success" @click="saveAdd()">提交</el-button>
        <el-button type="primary" @click="resetAdd()">重置</el-button>
        <el-button type="primary" @click="closeAdd()">取消</el-button>
      </span>
    </el-dialog>

    <el-dialog title="修改用户状态" :visible="lockVisible" @close="closeLock()">
      <span>确认修改？</span>
      <span slot="footer">
        <el-button type="danger" @click="handleLock()">修改</el-button>
        <el-button type="primary" @click="closeLock()">取消</el-button>
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
      cur_item: {},
      orig_item: {},
      searchUser: "",
      editVisible: false,
      addVisible: false,
      lockVisible: false,
      refreshFlag: 0
    }
  },
  methods: {
    backHome() {
      location.assign('../homepage.html')
    },
    getItems() {
      this.$http.get('http://127.0.0.1:8000/backend/user/').then(
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
    editUser(row) {
      this.editVisible = true
      this.cur_item = row
      this.orig_item = Object.assign({}, this.cur_item)
    },
    lockUser(row) {
      this.lockVisible = true
      this.cur_item = row
    },
    handleLock() {// finished
      this.$http.post('http://127.0.0.1:8000/backend/user/lock/', this.cur_item, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.refreshFlag ++
          this.lockVisible = false
          if (this.cur_item.account_locked == 'Y') {
            this.$notify({
              title: '成功',
              message: '解锁用户成功！',
              duration: 6000
            })
          }
          else {
            this.$notify({
              title: '成功',
              message: '锁定用户成功！',
              duration: 6000
            })
          }
          
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
    closeLock() {
      this.lockVisible = false
    },
    saveEdit() {// finished
      this.$http.post('http://127.0.0.1:8000/backend/user/pswd/', this.cur_item, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.refreshFlag ++
          this.editVisible = false
          this.$notify({
            title: '成功',
            message: '修改密码成功！',
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
    addUser() {
      this.addVisible = true
      this.cur_item = {}
      this.orig_item = {}
    },
    saveAdd() {// finished
      this.$http.post('http://127.0.0.1:8000/backend/user/create/', this.cur_item, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.addVisible = false
          this.refreshFlag ++
          this.$notify({
            title: '成功',
            message: '添加用户成功！',
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
    resetAdd() {
      this.cur_item = Object.assign({}, this.orig_item)
    },
    closeAdd() {
      this.addVisible = false
    },
    searchUsername() {// 模糊搜索
      this.$http.post('http://127.0.0.1:8000/backend/user/search/', {'searchUser': this.searchUser}, {emulateJSON: true}).then(
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
    stateFormat(row, column, cellValue) {
      if(cellValue == 'N') {
        return '否'
      }
      else if(cellValue == 'Y') {
        return '是'
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
