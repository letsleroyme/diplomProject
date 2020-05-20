<div class="col l12">
  <div class="table-chart">
    <canvas id="canvas"></canvas>
  </div>
</div>

<script>
  import {Bar} from 'vue-chartjs';
  export default {
    name: "ChartBar",
    data: () =>({
      chartData: ''
    }),
    extends: Bar,
    mounted() {
      this.chartData = this.$store.state.table.chartData

      const densityData = {
        label: 'Density of Planet (kg/m3)',
        data: [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638],
        backgroundColor: 'rgba(0, 99, 132, 0.6)',
        borderColor: 'rgba(0, 99, 132, 1)',
        yAxisID: "y-axis-density"
      };

      const gravityData = {
        label: 'Gravity of Planet (m/s2)',
        data: [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0],
        backgroundColor: 'rgba(99, 132, 0, 0.6)',
        borderColor: 'rgba(99, 132, 0, 1)',
        yAxisID: "y-axis-gravity"
      };

      const planetData = {
        labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
        datasets: [densityData, gravityData]
      };

      const chartOptions = {
        scales: {
          xAxes: [{
            barPercentage: 1,
            categoryPercentage: 0.6
          }],
          yAxes: [{
            id: "y-axis-density"
          }, {
            id: "y-axis-gravity"
          }]
        }
      };
      this.renderChart(planetData, chartOptions)
      // this.renderChart({
      //   labels: this.chartData.labels,
      //   datasets: [{
      //     label: this.chartData.labels,
      //     data: this.chartData.data,
      //     backgroundColor: [
      //       'rgba(255, 99, 132, 0.2)',
      //       'rgba(54, 162, 235, 0.2)',
      //       'rgba(255, 206, 86, 0.2)',
      //       'rgba(75, 192, 192, 0.2)',
      //       'rgba(153, 102, 255, 0.2)',
      //       'rgba(255, 159, 64, 0.2)'
      //     ],
      //     borderColor: [
      //       'rgba(255, 99, 132, 1)',
      //       'rgba(54, 162, 235, 1)',
      //       'rgba(255, 206, 86, 1)',
      //       'rgba(75, 192, 192, 1)',
      //       'rgba(153, 102, 255, 1)',
      //       'rgba(255, 159, 64, 1)'
      //     ],
      //     borderWidth: 1
      //   }]
      // })
    }
  }
</script>

<style scoped lang="scss">

</style>