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
      <el-menu-item index="1" @click="toDB">
        <i class="el-icon-s-platform"></i>
        <span slot="title">数据库权限</span>
      </el-menu-item>
      <el-menu-item index="2" @click="toForms">
        <i class="el-icon-s-order"></i>
        <span slot="title">表权限</span>
      </el-menu-item>
      <el-menu-item index="3" @click="toUsers">
        <i class="el-icon-user-solid"></i>
        <span slot="title">用户管理</span>
      </el-menu-item>
      <el-menu-item index="4" @click.native="logoutVisible = true">
        <i class="el-icon-switch-button"></i>
        <span slot="title">退出登录</span>
      </el-menu-item>
    </el-menu>
    <el-dialog title="提示" :visible="logoutVisible" @close="logoutVisible = false">
      <span>确认退出？</span>
      <span slot="footer">
        <el-button type="danger" @click="confirmLogout()">退出</el-button>
        <el-button type="primary" @click="logoutVisible = false">取消</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isCollapse: true,
      logoutVisible: false
    }
  },
  methods: {
    toHomepage() {
      location.assign('../homepage.html')
    },
    toDB() {
      location.assign('../DBpage.html')
    },
    toForms() {
      location.assign('../Formpage.html')
    },
    toUsers() {
      location.assign('../Userpage.html')
    },
    confirmLogout() {
      this.logoutVisible = false
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