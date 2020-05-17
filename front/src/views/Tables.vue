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

          <ChooseChart v-if="isChooseChart" @choose="chooseChartHandler"/>

          <div class="table-chart" v-if="isChart">
            <ChartTable/>
          </div>

          <div v-if="action" class="table-action">
            <div class="input-field col l4 action-1">
              <h4>Числовые столбцы</h4>
              <select ref="select" v-model="numberColumns" multiple>
                <option value="" disabled>Выберите колонку</option>
                <option :value="i" v-for="i in list">{{i}}</option>
              </select>
              <div class="check">
                <div class="check-1">
                  <div class="check_image" @click="action1check1"><svg v-if="action1_check1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Заменить NaN на среднее по столбцу</p>
                  </div>
                </div>
                <div class="check-2">
                  <div class="check_image" @click="action1check2"><svg v-if="action1_check2" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Удалить строки с NaN</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="input-field col l4 action-2">
               <h4>Категориальные столбцы</h4>
              <select ref="select2" v-model="categoricalColumns" multiple>
                <option value="" disabled>Выберите колонку</option>
                <option :value="i" v-for="i in list">{{i}}</option>
              </select>
              <div class="check">
                <div class="check-1">
                  <div class="check_image" @click="action2check1"><svg v-if="action2_check1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Заменить NaN значением, которое встречается в большинстве</p>
                  </div>
                </div>
                <div class="check-2">
                  <div class="check_image" @click="action2check2"><svg v-if="action2_check2" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Удалить строки с NaN</p>
                  </div>
                </div>
                <div class="check-3">
                  <div class="check_image" @click="action2check3"><svg v-if="action2_check3" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Привести текстовые категории в числовые</p>
                  </div>
                </div>
              </div>
              <div class="button">
                <button class="btn center" @click="changeFile">Применить</button>
              </div>
            </div>
            <div class="input-field col l4 action-3">
              <h4>Столбцы с текстовыми данными</h4>
              <select ref="select3" v-model="textDataColumns" multiple>
                <option value="" disabled>Выберите колонку</option>
                <option :value="i" v-for="i in list">{{i}}</option>
              </select>
              <div class="check">
                <div class="check-1">
                  <div class="check_image" @click="action3check1"><svg v-if="action3_check1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Привести заглавные буквы к маленьким</p>
                  </div>
                </div>
                <div class="check-2">
                  <div class="check_image" @click="action3check2"><svg v-if="action3_check2" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Убрать знаки препинания</p>
                  </div>
                </div>
                <div class="check-3">
                  <div class="check_image" @click="action3check3"><svg v-if="action3_check3" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                            width="26" height="26"
                            viewBox="0 0 172 172"
                            style=" fill:#000000;">
                    <g fill="none" fill-rule="nonzero" stroke="none" stroke-width="1"
                       stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10"
                       stroke-dasharray="" stroke-dashoffset="0" font-family="none"
                       font-weight="none" font-size="none" text-anchor="none"
                       style="mix-blend-mode: normal"><path d="M0,172v-172h172v172z"
                                                            fill="none"></path><g fill="#1abc9c">
                      <path d="M149.28546,31.29387l-11.86117,-8.0625c-3.28185,-2.22236 -7.77825,-1.36959 -9.97476,1.88642l-58.14303,85.74159l-26.71996,-26.71996c-2.79087,-2.79087 -7.33894,-2.79087 -10.12981,0l-10.15565,10.15565c-2.79087,2.79087 -2.79087,7.33894 0,10.15565l41.08774,41.08774c2.29988,2.29988 5.91767,4.05709 9.17368,4.05709c3.25601,0 6.53786,-2.04146 8.65685,-5.11658l69.97837,-103.23618c2.22235,-3.25601 1.36959,-7.72656 -1.91226,-9.94892z"></path>
                    </g></g></svg></div>
                  <div class="check_text">
                    <p>Удалить строки с NaN</p>
                  </div>
                </div>
              </div>
            </div>
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
  import ChartTable from "../components/ChartTable";
  import ChooseChart from "../components/ChooseChart";

  export default {
    name: 'tables',
    components: {
      ChartTable,
      ChooseChart
    },
    data:()=>({
      loader: true,
      file: '',
      action: false,
      isChooseChart: false,
      isChart:false,
      numberColumns: [],
      categoricalColumns: [],
      textDataColumns: [],
      list: '',
      action1_check1: false,
      action1_check2: false,
      action2_check1: false,
      action2_check2: false,
      action2_check3: false,
      action3_check1: false,
      action3_check2: false,
      action3_check3: false,
    }),
    methods: {
      uploadNewFile() {
        this.$router.push('/')
      },
      // Блок action
      async openAction() {
        await this.$store.dispatch('getList')
        this.list = this.$store.state.table.list.data
        this.action = !this.action
        this.isChooseChart = false
        this.isChart = false

        setTimeout(() => {
          M.FormSelect.init(this.$refs.select)
          M.FormSelect.init(this.$refs.select2)
          M.FormSelect.init(this.$refs.select3)
        }, 0)
      },
      action1check1() {
        this.action1_check1 = !this.action1_check1
        if (this.action1_check1 && this.action1_check2) {
          this.action1_check2 = false
        }
      },
      action1check2() {
        this.action1_check2 = !this.action1_check2
        if (this.action1_check2 && this.action1_check1) {
          this.action1_check1 = false
        }
      },
      action2check1() {
        this.action2_check1 = !this.action2_check1
        if (this.action2_check1 && this.action2_check2) {
          this.action2_check2 = false
        }
      },
      action2check2() {
        this.action2_check2 = !this.action2_check2
        if (this.action2_check1 && this.action2_check2) {
          this.action2_check1 = false
        }
      },
      action2check3() {
        this.action2_check3 = !this.action2_check3
      },
      action3check1() {
        this.action3_check1 = !this.action3_check1
      },
      action3check2() {
        this.action3_check2 = !this.action3_check2
      },
      action3check3() {
        this.action3_check3 = !this.action3_check3
      },
      async changeFile() {
        let formData = {
          numberColumns: this.numberColumns,
          categoricalColumns:this.categoricalColumns,
          textDataColumns: this.textDataColumns,
          action1_check1: this.action1_check1,
          action1_check2: this.action1_check2,
          action2_check1: this.action2_check1,
          action2_check2: this.action2_check2,
          action2_check3: this.action2_check3,
          action3_check1: this.action3_check1,
          action3_check2: this.action3_check2,
          action3_check3: this.action3_check3,
        }
        await this.$store.dispatch('changeFile', formData)
        this.action = !this.action
        this.numberColumns = []
        this.categoricalColumns = []
        this.textDataColumns = []
        this.action1_check1 = false
        this.action1_check2 = false
        this.action2_check1 = false
        this.action2_check2 = false
        this.action2_check3 = false
        this.action3_check1 = false
        this.action3_check2 = false
        this.action3_check3 = false
        this.loader = true
        this.file = this.$store.state.table.file.data
        setTimeout(() => {
          if (this.file.length !== 0) {
            this.loader = false
          }
        }, 500)
      },
      // Блок Chart
      openChooseChart() {
        this.isChart = false
        this.action = false
        this.isChooseChart = !this.isChooseChart
      },
      chooseChartHandler(isChart) {
        this.isChooseChart = !this.isChooseChart
        this.isChart = isChart
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
      .table-action {
        display: flex;
        border-radius: 5px;
        margin: 0 10px 20px 10px;
        box-shadow: 0 0 5px rgba(0,0,0,0.5);
        h4{
          font-size: 16px;
          text-align: center;
          font-weight: bold;
          margin: 10px 0;
        }
        .action-1 {
          margin: 10px 0;
          padding: 10px;
          /*border: 1px solid blue;*/
          .check {
            .check-1{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
            .check-2{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
          }
          .button {
            margin: 5px 0 10px 0;
            display: flex;
            justify-content: center;
          }
        }
        .action-2 {
          margin: 10px 0;
          padding: 10px;
          border-right: 1px solid grey;
          border-left: 1px solid grey;
          .check {
            .check-1{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
            .check-2{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
            .check-3{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
          }
          .button {
            margin: 5px 0 10px 0;
            display: flex;
            justify-content: center;
          }
        }
        .action-3 {
          margin: 10px 0;
          padding: 10px;
          /*border: 1px solid green;*/
          .check {
            .check-1{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
            .check-2{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
            .check-3{
              display: flex;
              align-items: center;
              .check_image{
                border: 1px solid grey;
                height: 26px;
                width: 26px;
                padding-right: 24px;
              }
              .check_text{
                margin-left: 10px;
              }
            }
          }
          .button {
            margin: 5px 0 10px 0;
            display: flex;
            justify-content: center;
          }
        }
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