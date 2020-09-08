<template>
  <div id="app">
    <el-col :span="4">
      <navcol></navcol>
    </el-col>
    <el-col :span="20">
      <el-card class="table-card">
        <homepicture></homepicture>
      </el-card>
    </el-col>
  </div>
</template>

<script>
import navcol from '../../components/navcol.vue'
import homepicture from '../../components/homepicture.vue'
export default {
  components: {
    navcol,
    homepicture
  },
  data() {
    return {
      msg: 'Use Vue 2.0 Today!'
    }
  },
  methods: {
    toMaterialInfo() {
      location.assign('../material_info.html')
    }
  }
}
</script>

<style lang="postcss">
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.table-card {
  width: 1000px;
  margin-top: 50px auto;
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
