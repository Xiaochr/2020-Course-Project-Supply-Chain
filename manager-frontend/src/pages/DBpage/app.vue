<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
      <el-page-header @back="backHome" content="数据库权限"></el-page-header>
      <el-divider></el-divider>
      <el-row>
        <el-col :span="12">
          <el-input v-model="searchUser" @keyup.enter.native="searchUsername()" placeholder="搜索用户名"></el-input>
        </el-col>
        
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="4">
          <el-button type="primary" icon="el-icon-search" plain @click="searchUsername()">搜索</el-button>
        </el-col>
      </el-row>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="user" label="用户名"></el-table-column>
        <el-table-column prop="select_priv" label="Select" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="update_priv" label="Update" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="delete_priv" label="Delete" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="create_priv" label="Create" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="drop_priv" label="Drop" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="trigger_priv" label="Trigger" :formatter="stateFormat"></el-table-column>
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
            <el-form-item></el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="所有权限">
              <el-select v-model="cur_item.all">
                <el-option label="有(Y)" value="1"></el-option>
                <el-option label="无(N)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="Select权限">
              <el-select v-model="cur_item.select_priv">
                <el-option label="有(Y)" value="1"></el-option>
                <el-option label="无(N)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Update权限">
              <el-select v-model="cur_item.update_priv">
                <el-option label="有(Y)" value="1"></el-option>
                <el-option label="无(N)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Delete权限">
              <el-select v-model="cur_item.delete_priv">
                <el-option label="有(Y)" value="1"></el-option>
                <el-option label="无(N)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="Create权限">
              <el-select v-model="cur_item.create_priv">
                <el-option label="有(Y)" value="1"></el-option>
                <el-option label="无(N)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Drop权限">
              <el-select v-model="cur_item.drop_priv">
                <el-option label="有(Y)" value="1"></el-option>
                <el-option label="无(N)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Trigger权限">
              <el-select v-model="cur_item.trigger_priv">
                <el-option label="有(Y)" value="1"></el-option>
                <el-option label="无(N)" value="0"></el-option>
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
      cur_item: {},
      orig_item: {},
      searchUser: "",
      editVisible: false
    }
  },
  methods: {
    backHome() {
      location.assign('../homepage.html')
    },
    getItems() {
      this.$http.get('http://127.0.0.1:8000/backend/db/').then(
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
    searchUsername() {// 模糊搜索
      this.$http.post('http://127.0.0.1:8000/backend/db/search/', {'searchUser': this.searchUser}, {emulateJSON: true}).then(
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
    saveEdit() {
      this.editVisible = false
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
