<template lang="html">
  <div class="navcol">
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
    <el-menu :default-active="index" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      <el-menu-item-group>
        <span slot="title">主页</span>
        <el-menu-item index="0" @click="backHome">
          <i class="el-icon-s-home"></i>
          <span slot="title">主页</span>
        </el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group>
        <span slot="title">库存</span>
        <el-menu-item index="1" @click="to_material_info">
          <i class="el-icon-menu"></i>
          <span slot="title">原料信息</span>
        </el-menu-item>
        <el-menu-item index="2" @click="to_stock">
          <i class="el-icon-menu"></i>
          <span slot="title">原料库存</span>
        </el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group>
        <span slot="title">订单</span>
        <el-menu-item index="3" @click="to_material_order">
          <i class="el-icon-document"></i>
          <span slot="title">原料订单</span>
        </el-menu-item>
        <el-menu-item index="4" @click="to_out_list">
          <i class="el-icon-document"></i>
          <span slot="title">出库清单</span>
        </el-menu-item>
      </el-menu-item-group>
      <el-menu-item-group>
        <span slot="title">退出</span>
        <el-menu-item index="5" @click.native="log_out">
          <i class="el-icon-switch-button"></i>
          <span slot="title">退出登录</span>
        </el-menu-item>
      </el-menu-item-group>
    </el-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isCollapse: true
    }
  },
  methods: {
    backHome() {
      location.assign('../index.html')
    },
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
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style lang="css">
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>