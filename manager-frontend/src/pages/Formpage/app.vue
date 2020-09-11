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
              v-for="item in items"
              :key="item.user_name"
              :label="item.user_name"
              :value="item.user_name">
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
              v-for="item in items"
              :key="item.table_name"
              :label="item.table_name"
              :value="item.table_name">
            </el-option>
          </el-select>
        </el-col>
        <el-col :span="1"><p> </p></el-col>
        <el-col :span="4">
          <el-button type="primary" icon="el-icon-search" plain @click="searchName()">搜索</el-button>
        </el-col>
      </el-row>
      <el-table class="data-table" :data="items" height="350" stripe border>
        <el-table-column prop="user_name" label="用户名"></el-table-column>
        <el-table-column prop="table_name" label="数据表名"></el-table-column>
        <el-table-column prop="select" label="Select" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="insert" label="Insert" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="update" label="Update" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="delete" label="Delete" :formatter="stateFormat"></el-table-column>
        <el-table-column prop="drop" label="Drop" :formatter="stateFormat"></el-table-column>
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
            <el-form-item>
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="数据表名">
              <el-input type="text" v-model="cur_item.table_name" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <el-form-item label="Select权限">
              <el-select v-model="cur_item.select" :formatter="stateFormat">
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
            <el-form-item label="Insert权限">
              <el-select v-model="cur_item.insert">
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
            <el-form-item label="所有权限">
              <el-select v-model="cur_item.all">
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
          'table_name': 'table1',
          'select': 1,
          'insert': 0,
          'update': 0,
          'delete': 1,
          'drop': 1,
          'all': 0
        },
        {
          'user_name': 'u1',
          'table_name': 'table2',
          'select': 1,
          'insert': 0,
          'update': 0,
          'delete': 1,
          'drop': 1,
          'all': 0
        },
        {
          'user_name': 'u2',
          'table_name': 'table2',
          'select': 1,
          'insert': 1,
          'update': 1,
          'delete': 1,
          'drop': 1,
          'all': 1
        }
      ],
      cur_item: {},
      orig_item: {},
      searchUser: "",
      searchTable: "",
      editVisible: false,
      options: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }, {
        value: '选项4',
        label: '龙须面'
      }, {
        value: '选项5',
        label: '北京烤鸭'
      }],
      value1: [],
      value2: []
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
