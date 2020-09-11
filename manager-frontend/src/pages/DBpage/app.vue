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
          <el-input v-model="searchContent" placeholder="搜索用户名"></el-input>
        </el-col>
        
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="4">
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-col>
      </el-row>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="user_name" label="用户名"></el-table-column>
        <el-table-column prop="select" label="Select" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="update" label="Update" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="delete" label="Delete" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="create" label="Create" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="drop" label="Drop" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="trigger" label="Trigger" :formatter="stateFormat"></el-table-column>
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
              <el-input type="text" v-model="cur_item.user_name" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="7">
            <el-form-item></el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="所有权限">
              <el-select v-model="cur_item.all">
                <el-option label="有(1)" value="1"></el-option>
                <el-option label="无(0)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="Select权限">
              <el-select v-model="cur_item.select">
                <el-option label="有(1)" value="1"></el-option>
                <el-option label="无(0)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Update权限">
              <el-select v-model="cur_item.update">
                <el-option label="有(1)" value="1"></el-option>
                <el-option label="无(0)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Delete权限">
              <el-select v-model="cur_item.delete">
                <el-option label="有(1)" value="1"></el-option>
                <el-option label="无(0)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="Create权限">
              <el-select v-model="cur_item.create">
                <el-option label="有(1)" value="1"></el-option>
                <el-option label="无(0)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Drop权限">
              <el-select v-model="cur_item.drop">
                <el-option label="有(1)" value="1"></el-option>
                <el-option label="无(0)" value="0"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="6">
            <el-form-item label="Trigger权限">
              <el-select v-model="cur_item.trigger">
                <el-option label="有(1)" value="1"></el-option>
                <el-option label="无(0)" value="0"></el-option>
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
          'select': 1,
          'update': 0,
          'delete': 1,
          'create': 1,
          'drop': 1,
          'trigger': 0,
          'all': 0
        },
        {
          'user_name': 'u2',
          'select': 1,
          'update': 1,
          'delete': 1,
          'create': 1,
          'drop': 1,
          'trigger': 1,
          'all': 0
        }
      ],
      cur_item: {},
      orig_item: {},
      searchContent: "",
      editVisible: false
    }
  },
  methods: {
    backHome() {
      location.assign('../homepage.html')
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
      if(cellValue == 0) {
        return '无'
      }
      else if(cellValue == 1) {
        return '有'
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
