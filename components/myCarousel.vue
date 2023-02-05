<template>
  <Carousel class="abc" :transition="500" :autoplay="10000" :wrap-around="true">
    <Slide class="carousel__slide" v-for="event in events.events" :key="slide">
      <AfterdarkEvent class="carousel__item"
                      :title=event.title
                      :date=event.date
                      :from=event.time.from
                      :to=event.time.to
                      :imagesrc=event.imagesrc>
      </AfterdarkEvent>
    </Slide>
  </Carousel>
</template>

<script setup>
  import events from '../mockdata/afterdark.json'
  console.log(events)
</script>

<script>

import {Carousel, Navigation, Pagination, Slide} from "vue3-carousel";
import 'vue3-carousel/dist/carousel.css'
import {defineComponent} from 'vue';
import AfterdarkEvent from "./AfterdarkEvent";

export default defineComponent({
  name: 'Autoplay',
  components: {
    AfterdarkEvent,
    Carousel,
    Slide,
    Pagination,
    Navigation
  }
})

</script>

<style scoped>

.carousel__item {
  width: inherit;
  height: 100vh;
  background-color: #141448;
  color: white;
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1
}

.carousel__slide {
  height: inherit;
}

.abc {
  display: flex;
  flex: 1;
  overflow: auto;
}

</style>