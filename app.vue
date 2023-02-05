<template>
  <div class="app_container">
    <div class="static_container half_container">
      <AfterdarkEvent :title=events.events[0].title
                 :date=events.events[0].date
                 :from=events.events[0].time.from
                 :to=events.events[0].time.to
                 :imagesrc=events.events[0].imagesrc
      ></AfterdarkEvent>
    </div>
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


</style>