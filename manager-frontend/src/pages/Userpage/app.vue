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
          <el-input v-model="searchContent" @keyup.enter.native="searchName()" placeholder="搜索用户名"></el-input>
        </el-col>
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="primary" icon="el-icon-circle-plus-outline" plain @click="addUser()">添加用户</el-button>
        </el-col>
      </el-row>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="user_name" label="用户"></el-table-column>
        <el-table-column prop="pswd" label="密码"></el-table-column>
        <el-table-column prop="locked" label="是否锁定" :formatter="stateFormat"></el-table-column>
        <el-table-column label="编辑">
          <template slot-scope="scope">
            <el-button type="primary" size="mini" icon="el-icon-edit" @click="editUser(scope.row)">编辑</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    </el-col>

    <el-dialog :title="addVisible?'添加用户':'编辑用户'" :visible="editVisible" @close="closeEdit()">
      <el-form>
        <el-row>
          <el-col :span="6">
            <el-form-item label="用户名">
              <el-input type="text" v-model="cur_item.user_name"></el-input>
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
              <el-select v-model="cur_item.locked">
                <el-option label="是" value="1"></el-option>
                <el-option label="否" value="0"></el-option>
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
      items: [
        {
          'user_name': 'u1',
          'pswd': 'u1u1',
          'locked': 0
        },
        {
          'user_name': 'u2',
          'pswd': 'u2u2',
          'locked': 1
        }
      ],
      cur_item: {},
      orig_item: {},
      searchContent: "",
      editVisible: false,
      addVisible: false
    }
  },
  methods: {
    backHome() {
      location.assign('../homepage.html')
    },
    editUser(row) {
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
    addUser() {
      this.editVisible = true
      this.addVisible = true
      this.cur_item = {}
      this.orig_item = {}
    },
    stateFormat(row, column, cellValue) {
      if(cellValue == 0) {
        return '否'
      }
      else if(cellValue == 1) {
        return '是'
      }
    }
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
