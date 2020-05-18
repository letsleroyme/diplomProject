<div class="col l12">
  <div class="table-chart">
    <canvas id="canvas" width="400" height="300"></canvas>
  </div>
</div>

<script>
  import {Bar, Pie} from 'vue-chartjs';
  export default {
    name: "ChartTable",
    data: () =>({
      chartData: ''
    }),
    extends: Bar,
    mounted() {
      this.chartData = this.$store.state.table.chartData
      console.log(this.chartData.data)
      this.renderChart({
        labels: this.chartData.labels,
        datasets: [{
          label: this.chartData.labels,
          data: this.chartData.data,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
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
      // const canvas = document.querySelector('canvas')
      // canvas.style.width = 80 + '%'
      // canvas.style.height = 80 + '%'
    }
  }
</script>

<style scoped lang="scss">

</style>