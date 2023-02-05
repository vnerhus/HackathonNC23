<template>
    <div>
      <p>Temperature: {{ temperature }}°C</p>
      <p>Weather type: {{ weatherType }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        temperature: null,
        weatherType: null,
      };
    },
    mounted() {
      this.fetchWeatherData();
    },
    methods: {
      async fetchWeatherData() {
        try {
          const response = await axios.get('https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.91202&lon=19.7374');
          const data = response.data;
          this.temperature = data.properties.timeseries[0].data.instant.details.air_temperature;
          this.weatherType = data.properties.timeseries[0].data.next_1_hours.summary.symbol_code;
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
  </script>
  