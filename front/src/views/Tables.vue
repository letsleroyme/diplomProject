<template>
  <div class="container">
    <div class="row tables">
      <div v-if="loader" class="center col l12 preloader">
        <div class="preloader-wrapper big active">
          <div class="spinner-layer spinner-green-only">
            <div class="circle-clipper left">
              <div class="circle"></div>
            </div><div class="gap-patch">
            <div class="circle"></div>
          </div><div class="circle-clipper right">
            <div class="circle"></div>
          </div>
          </div>
        </div>
      </div>

        <div v-else class="table-main">
          <div class="table-button">
            <button class="btn" @click="openAction">Предварительная обработка данных</button>
            <button class="btn" @click="openChooseChart">График</button>
            <button class="btn" @click="uploadNewFile">Загрузить новый файл</button>
            <button class="btn">Кнопка 4</button>
          </div>

          <ChangeTable v-if="action" @changetable="changeTable"/>

          <ChooseChart v-if="isChooseChart" @choose="chooseChartHandler"/>

          <div class="table-chart" v-if="isChartLine">
            <ChartLine />
          </div>

          <div class="table-chart" v-if="isChartBar">
            <ChartBar/>
          </div>

          <div class="table-chart" v-if="isChartPie">
            <ChartPie />
          </div>

          <div class="table-body">
            <table>
              <tr v-for="i in file">
                  <td v-for="j in i" >{{j}}</td>
              </tr>

            </table>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  import ChartLine from "../components/ChartLine";
  import ChartBar from "../components/ChartBar";
  import ChartPie from "../components/ChartPie";
  import ChooseChart from "../components/ChooseChart";
  import ChangeTable from "../components/ChangeTable";

  export default {
    name: 'tables',
    components: {
      ChangeTable,
      ChartLine,
      ChartBar,
      ChartPie,
      ChooseChart
    },
    data:()=>({
      loader: true,
      file: '',
      action: false,
      isChooseChart: false,
      isChartLine: false,
      isChartBar:false,
      isChartPie: false,
    }),
    methods: {
      uploadNewFile() {
        this.$router.push('/')
      },
      // Блок action
      async openAction() {
        this.action = !this.action
        this.isChooseChart = false
        this.isChartLine = false
        this.isChartPie = false
        this.isChartBar = false
      },
      async changeTable() {
        this.action = !this.action
        this.loader = true
        this.file = this.$store.state.table.file.data
        console.log(this.file)
        setTimeout(() => {
          if (this.file.length !== 0) {
            this.loader = false
          }
        }, 500)
      },
      // Блок Chart
      openChooseChart() {
        this.isChartLine = false
        this.isChartPie = false
        this.isChartBar = false
        this.action = false
        this.isChooseChart = !this.isChooseChart
      },
      chooseChartHandler() {
        this.isChooseChart = !this.isChooseChart
        let chartType = this.$store.state.table.chartData
        if (chartType.GraphType === 'Line') {
          this.isChartLine = true
        } else if (chartType.GraphType === 'Bar') {
          this.isChartBar = true
        } else if(chartType.GraphType === 'Pie') {
          this.isChartPie = true
        }
      }
    },
    mounted() {
      this.file = this.$store.state.table.file.data

      setTimeout(() => {
        if (this.file.length !== 0) {
          this.loader = false
        }
      }, 500)
    }
  }
</script>

<style lang="scss" scoped>
  .tables{
    min-height: 600px;
    margin-top: 30px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    .preloader {
      padding-top: 200px;
    }
    .table-main {
      .table-button {
        padding: 20px;
        display: flex;
        justify-content: space-between;
        height: 100px;
      }
      .table-chart {
        margin: 10px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
        height: 600px;
        overflow: scroll;
      }

      .table-body {
        padding: 0 10px;
        overflow: scroll;
        height: 500px;
        margin-bottom: 0;
        table {
          tr:first-child{
            background-color: lightgrey;
          }
          td{
            border: 1px solid darkgrey;
          }
          td:first-child {
            background-color: lightgrey;
          }
          .grey {
            background-color: grey;
          }
        }
      }
    }
  }
</style>