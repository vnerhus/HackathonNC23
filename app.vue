<template>
  <div class="app_container">
    <div class="static_container half_container">
      <div class="clock">
        <span>18:48</span>
        <img class="clockimg" src="https://cdn-icons-png.flaticon.com/512/2088/2088617.png">
      </div>
      <weatherData></weatherData>
      <MyTable></MyTable>
    </div>
    <div class="half_divider"></div>
    <div class="carousel_container half_container">
      <myCarousel></myCarousel>
    </div>
  </div>
</template>

<script setup>
  import events from './mockdata/afterdark.json'
</script>

<style>

@font-face {
  font-family: GeomanistBlack;
  src: url('assets/fonts/GeomanistBlack.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: GeomanistBold;
  src: url('assets/fonts/GeomanistBold.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: GeomanistLight;
  src: url('assets/fonts/GeomanistLight.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: GeomanistRegular;
  src: url('assets/fonts/GeomanistRegular.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}

body {
  font-family: 'GeomanistBold', sans-serif;
  margin: 0
}

.app_container {
  display: flex;
  flex-direction: row;
  width: 100%;
}

.half_container {
  flex: 1;
  overflow: clip;
}

.static_container {
  max-height: inherit;
}

.carousel_container {
  display: flex;
}

.clock {
  padding: 40px;
  background-color: coral;
  font-size: 40px;
  align-items: center;
  display: flex;
  gap: 20px;
}

.clockimg {
  width: 40px;
  margin-bottom: 4px;
}

.half_divider {
  height: 10px;
  background-color: #141448;
}

</style>