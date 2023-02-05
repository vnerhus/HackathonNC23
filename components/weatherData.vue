<template>
  <div>
    <h2>Temperaturer</h2>
    <p v-if="currentTemp !== null">
      Dagens temperatur nå: {{ currentTemp }}°C, {{ currentWeatherType }}
    </p>
    <p v-else>Kunne ikke hente dagens temperatur</p>
    <p>Værtype og temperatur for de neste 3 dagene kl 12:</p>
    <ul>
      <li v-for="day in nextThreeDays">
        {{ day.date }}: {{ day.temp }}°C, {{ day.weatherType }}
      </li>
    </ul>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      currentTemp: null,
      currentWeatherType: null,
      nextThreeDays: []
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      const response = await axios.get(
        "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.91202&lon=19.7374"
      );
      const forecasts = response.data.properties.timeseries;
      const now = new Date();
      const currentForecast = forecasts.find(
        f => f.time.slice(0, 9) === now.toISOString().slice(0, 9)
      );
      if (currentForecast && currentForecast.data) {
        this.currentTemp = currentForecast.data.instant.details.air_temperature;
        this.currentWeatherType = currentForecast.data.next_1_hours.summary.symbol_code;
      } else {
        this.currentTemp = null;
        this.currentWeatherType = null;
      }

      let currentDay = null;

      for (let forecast of forecasts) {
        const forecastTime = new Date(forecast.time);

        if (forecastTime.getUTCHours() === 12) {
          if (currentDay === null || currentDay.getUTCDate() !== forecastTime.getUTCDate()) {
            this.nextThreeDays.push({
              date: this.getWeekday(forecastTime.getDay()),
              temp: forecast.data.instant.details.air_temperature,
              weatherType: forecast.data.next_1_hours.summary.symbol_code
            });

            if (this.nextThreeDays.length === 3) break;

            currentDay = forecastTime;
          }
        }
      }
    },
    getWeekday(time) {
        const weekdays = ['Søndag', 'Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lørdag'];
        return weekdays[time];
      },
  }
};
</script>