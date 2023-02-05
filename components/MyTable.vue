<template>
    <div>
      <table>
        <tr v-for="row in csvData">
          <td v-for="cell in row">{{ cell }}</td>
        </tr>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        csvData: []
      }
    },
    mounted() {
      fetch('/Users/eliaslarsen/Development/hackaton/HackathonNC23/content/ukemenu5til7clean.csv')
        .then(response => response.text())
        .then(csv => {
          const rows = csv.split('\n');
          this.csvData = rows.map(row => row.split(','));
        });
    }
  }
  </script>