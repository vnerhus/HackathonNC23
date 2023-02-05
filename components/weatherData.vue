<template>
  <div class="weather__container">
    <span class="weather__title">Weather forecast</span>
    <div class="weather__bar">
      <div class="weather__current">
        <p class="weather__day">
          Today:
        </p>
        <img class="weather__icon" v-if="currentWeatherType == 'cloudy'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
        <img class="weather__icon" v-if="currentWeatherType == 'cloudy_night'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
        <img class="weather__icon" v-if="currentWeatherType == 'partlycloudy'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
        <img class="weather__icon" v-if="currentWeatherType == 'partlycloudy_night'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
        <img class="weather__icon" v-if="currentWeatherType == 'clearsky_day'" src="https://cdn-icons-png.flaticon.com/512/106/106061.png"/>
        <img class="weather__icon" v-if="currentWeatherType == 'x'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
        <img class="weather__icon" v-if="currentWeatherType == 'x'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
        <p class="weather__temp" v-if="currentTemp !== null">
          {{ currentTemp }}°C
        </p>
      </div>

      <div class="divider"></div>

      <div class="weather__week">
        <div class="weather__week__block" v-for="day in nextThreeDays">
          <span class="weather__day">{{ day.date }}:</span>
          <span class="weather__temp">{{ day.temp }}°C</span>
          <img class="weather__icon" v-if="currentWeatherType == 'cloudy'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
          <img class="weather__icon" v-if="currentWeatherType == 'cloudy_night'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
          <img class="weather__icon" v-if="currentWeatherType == 'partlycloudy_night'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
          <img class="weather__icon" v-if="currentWeatherType == 'clearsky_day'" src="https://cdn-icons-png.flaticon.com/512/106/106061.png"/>
          <img class="weather__icon" v-if="currentWeatherType == 'clearsky_night'" src="https://cdn-icons-png.flaticon.com/512/106/106061.png"/>
          <img class="weather__icon" v-if="currentWeatherType == 'x'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
          <img class="weather__icon" v-if="currentWeatherType == 'x'" src="https://cdn-icons-png.flaticon.com/512/2932/2932445.png"/>
        </div>
      </div>
    </div>
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

<style>

.weather__current {
  display: flex;
  font-size: 20px;
  align-items: center;
  gap: 20px;
}

.weather__container {
  padding: 40px;
}

.weather__bar {
  display: flex;
  align-items: center;
  gap: 20px;
}

.weather__current .weather__temp {
  font-size: 40px
}

.weather__current .weather__icon {
  width: 80px;
}

.weather__current .weather__day {
  font-size: 40px;
}

.weather__day {

}



.weather__title{
  font-size: 30px;
}

.weather__icon {
  object-fit: contain;
  width: 40px;
}

.weather__week {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 20px;
}

.weather__week__block {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #e8efff;
  padding: 8px;
  border-radius: 10px;
}

.divider {
  width: 2px;
  height: 60px;
  background-color: #141448;
}

</style>