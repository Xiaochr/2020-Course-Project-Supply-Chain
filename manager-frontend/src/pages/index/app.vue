<template>
  <div id="app">
    <img src="../../assets/logo.png">
    <el-card class="index-card">
      <div slot="header">
        用户登录
      </div>
      <el-form>
        <el-form-item label="账号">
          <el-input v-model="id" placeholder="请输入账号"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="pswd" placeholder="请输入密码"></el-input>
        </el-form-item>
      </el-form>
      <el-button type="primary" plain @click="login" show-password @keyup.enter.native="login">登录</el-button>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: 'admin1',
      pswd: '',
      correct_id: 'admin1',
      correct_pswd: '123'
    }
  },
  methods: {
    login() {
      if (this.id == this.correct_id && this.pswd == this.correct_pswd) {
        location.assign('../homepage.html')
      }
      else {
        this.$notify({
          title: '错误',
          message: '请输入正确的用户名和密码！',
          duration: 6000
        })
      }
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
body {
  background: #F5F5F5;
}
</style>
