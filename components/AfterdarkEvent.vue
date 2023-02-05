<template>
  <div class="event_container">
    <div class="event__info">
      <span class="event__title">{{title}}</span>
      <div class="divider"></div>
      <span class="event__date">Date: {{date}}</span>
      <span class="event__time">Time: {{from}} - {{to}}</span>
    </div>
    <img class="event__image" :src="imagesrc">
  </div>
</template>

<script>

export default {
  props: ['title', 'date', 'from', 'to', 'imagesrc']
}

</script>

<style scoped>
  .divider {
    height: 2px;
    width: 100px;
    background-color: coral;
    margin-top: 5px;
    margin-bottom: 5px;
  }

  .event_container {
    display: flex;
    flex-direction: column;
    padding: 60px;
    align-items: center;
    width: 100%;
  }

  .event__info {
    display: flex;
    flex-direction: column;
    align-self: start;
    align-items: start;
    padding: 8px;
  }

  .event__title {
    font-size: 45px;
  }

  .event__image {
    height: 400px;
    width: 100%;
    object-fit: cover;
  }

  .event__date {
    font-family: GeomanistLight, sans-serif;
  }

  .event__time {
    font-family: GeomanistLight, sans-serif;
  }
</style>