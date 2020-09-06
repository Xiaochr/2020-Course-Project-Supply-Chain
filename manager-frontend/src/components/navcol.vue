<template lang="html">
  <div class="navcol">
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
    <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
      
      <el-menu-item index="0" @click="toHomepage">
        <i class="el-icon-s-home"></i>
        <span slot="title">主页</span>
      </el-menu-item>
      <el-menu-item index="1" @click="toAuthSearch">
        <i class="el-icon-search"></i>
        <span slot="title">权限查询</span>
      </el-menu-item>
      <el-menu-item index="2" @click="toUserAuth">
        <i class="el-icon-user-solid"></i>
        <span slot="title">用户权限</span>
      </el-menu-item>
      <el-menu-item index="3" @click="toTables">
        <i class="el-icon-s-platform"></i>
        <span slot="title">表格概览</span>
      </el-menu-item>
      <el-menu-item index="4" @click.native="log_out">
        <i class="el-icon-switch-button"></i>
        <span slot="title">退出登录</span>
      </el-menu-item>
      
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
    toHomepage() {
      location.assign('../homepage.html')
    },
    toAuthSearch() {
      location.assign('../auth_search.html')
    },
    toUserAuth() {
      location.assign('../user_auth.html')
    },
    toTables() {
      location.assign('../tables.html')
    },
    log_out() {
      this.$notify({
        title: 'Success',
        message: 'You have successfully logged out. See you!',
        duration: 6000
      })
      location.assign('../index.html')
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