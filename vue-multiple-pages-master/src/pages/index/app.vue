<template>
  <div id="app">
    <img src="../../assets/logo.png">
    <el-card class="index-card">
      <div slot="header">
        库存
      </div>
      <el-button type="primary" plain @click="to_material_info">原料信息</el-button>
      <el-button type="primary" plain @click="to_stock">原料库存</el-button>
    </el-card>
    <el-card class="index-card">
      <div slot="header">
        订单
      </div>
      <el-button type="primary" plain @click="to_material_order">原料订单</el-button>
      <el-button type="primary" plain @click="to_out_list">出库清单</el-button>
    </el-card>
    <el-button type="primary" plain @click.native="log_out">退出登录</el-button>
  </div>
</template>

<script>
import modal from '../../components/modal.vue'
export default {
  components: {
    modal
  },
  data() {
    return {
      msg: 'Use Vue 2.0 Today!'
    }
  },
  methods: {
    to_material_info() {
      location.assign('../material_info.html')
    },
    to_stock() {
      location.assign('../stock.html')
    },
    to_material_order() {
      location.assign('../material_order.html')
    },
    to_out_list() {
      location.assign('../out_list.html')
    },
    log_out() {
      this.$notify({
        title: 'Success',
        message: 'You have successfully logged out. See you!',
        duration: 6000
      })
    }
  }
}
</script>

<style lang="postcss">
.index-card {
  width: 400px;
  margin: 50px auto;
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
