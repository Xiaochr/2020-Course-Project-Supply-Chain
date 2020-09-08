<template lang="html">
  <div class="homepicture">
    <el-carousel :interval="5000" type="card" height="400px">
      <el-carousel-item v-for="(item, index) in carouselList" :key="index">
        <img :src="item.path" alt="找不到图片" @click="to_material_info" class="carousel_image_type">
        <h3 class="medium">{{ item.name }}</h3>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data() {
    return {
      carouselList: [
        {path: require("../assets/material.jpg"), name: 2},
        {path: require("../assets/stock.jpg"), name: 3},
        {path: require("../assets/logistic.jpg"), name: 4}
      ]
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
</style>