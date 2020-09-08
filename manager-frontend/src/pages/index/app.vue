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
      <el-button type="primary" plain @click="backHome">登录</el-button>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: '',
      pswd: '',
      passFlag: false
    }
  },
  methods: {
    login() {
      this.$http.post('http://127.0.0.1:8000/backend/login/', {'id': this.id, 'pswd': this.pswd}, {emulateJSON: true}).then(
        function(data) {
          console.log(data)
          this.passFlag = data.body
        }
      )
      if (this.passFlag) {
        location.assign('../homepage.html')
      }
      else {
        this.$notify({
          title: 'Error',
          message: 'The wrong password!',
          duration: 6000
        })
      }
    },
    backHome() {
      location.assign('../homepage.html')
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
