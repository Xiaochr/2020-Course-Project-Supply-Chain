<template>
  <div id="app">
    <pageheader></pageheader>
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <img src="../../assets/logo.png">
    </el-col>
  </div>
</template>

<script>
import navcol from '../../components/navcol.vue'
import pageheader from '../../components/pageheader.vue'
export default {
  components: {
    navcol,
    pageheader
  },
  data() {
    return {
      items: []
    }
  },
  methods: {
    backHome() {
      location.assign('../index.html')
    }
  }
}
</script>

<style>
.table-card {
  width: 1200px;
  margin: 100px auto;
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
