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

      let counter = 0
      for( let n in this.chartData.data) {
        counter++
      }

      if (counter === 2) {
        const data1 = {
          label: this.chartData.header[1],
          data: this.chartData.data[1],
          backgroundColor: 'rgba(255, 99, 132, 0.5)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
          yAxisID: "y-axis-density"
        };
        const data2 = {
          label: this.chartData.header[2],
          data: this.chartData.data[2],
          backgroundColor: 'rgba(54, 162, 235, 0.5)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
          yAxisID: "y-axis-gravity"
        };
        const allData = {
          labels: this.chartData.labels[2],
          datasets: [data1, data2]
        }
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
        }
        this.renderChart(allData, chartOptions)
      } else if (counter === 1){
        this.renderChart({
          labels: this.chartData.labels[1],
          datasets: [{
            label: this.chartData.header[1],
            data: this.chartData.data[1],
            backgroundColor: [
              'rgba(255, 99, 132, 0.5)',
              'rgba(54, 162, 235, 0.5)',
              'rgba(255, 206, 86, 0.5)',
              'rgba(75, 192, 192, 0.5)',
              'rgba(153, 102, 255, 0.5)',
              'rgba(255, 159, 64, 0.5)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
          }]
        })
      }

    }
  }
</script>

<style scoped lang="scss">

</style>