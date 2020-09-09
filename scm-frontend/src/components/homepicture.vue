<template lang="html">
  <div class="homepicture">
    <el-carousel :interval="5000" type="card" height="400px">
      <el-carousel-item v-for="(item, index) in carouselList" :key="index">
        <div>
          <el-image :src="item.path" alt="找不到图片" @click="toPath(item.url)" class="carousel_image_type"></el-image>
          <span style="position: absolute; top: 0; left: 0;" class="pic_name">
            <el-tag effect="dark" size="medium">{{item.name}}</el-tag>
          </span> 
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data() {
    return {
      carouselList: [
        {path: require("../assets/material.jpg"), name: "原料信息", url: "../material_info.html"},
        {path: require("../assets/stock.jpg"), name: "原料库存", url: "../stock.html"},
        {path: require("../assets/logistic.jpg"), name: "原料订单", url: "../material_order.html"}
      ]
    }
  },
  methods: {
    toPath(url) {
      location.assign(url)
    }
  }
}
</script>

<style lang="css">
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .carousel_image_type {
    height: 400px;
  }
  .pic_name {
    font-size: 30;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
</style>