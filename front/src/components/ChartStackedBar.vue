<div class="col l12">
  <div class="table-chart">
    <canvas id="canvas"></canvas>
  </div>
</div>

<script>
  import {Bar} from 'vue-chartjs';
  export default {
    name: "ChartStackedBar",
    data: () =>({
      chartData: ''
    }),
    extends: Bar,
    mounted() {
      this.chartData = this.$store.state.table.chartData

      const chartOptions = {
          scales: {
            xAxes: [{
              stacked: true
            }],
            yAxes: [{
            stacked: true
            }]
          }
        }

      const allData = {
          labels: ['1Class', '2Class', '3Class'],
          datasets: [{
         label: 'Died',
         data: [80, 97, 372],
         backgroundColor: '#22aa99'
      }, {
         label: 'Survived',
         data: [136, 87, 119],
         backgroundColor: '#994499'
      }]
        }

      this.renderChart(allData, chartOptions)
   }
}

</script>

<style scoped lang="scss">

</style>
