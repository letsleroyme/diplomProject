<template>
  <div class="choose">
    <div class="chooseChart col l6">
      <div @change="chooseChartLine">
        <label>
          <input type="checkbox" v-model="isLine"/>
          <span>Линейный график</span>
        </label>
      </div>
      <div @change="chooseChartBar">
        <label>
          <input type="checkbox" v-model="isBar"/>
          <span>Столбчатая диаграмма</span>
        </label>
      </div>
      <div @change="chooseChartPie">
        <label>
          <input type="checkbox" v-model="isPie"/>
          <span>Круговая диаграмма</span>
        </label>
      </div>
      <div @change="chooseChartStackedBar">
        <label>
          <input type="checkbox" v-model="isStackedBar"/>
          <span>Гистограмма с прирощением</span>
        </label>
      </div>
    </div>
    <div class="input-field col l6 chooseColumn">

      <div>
        <select ref="select" v-model="selectColumn" multiple >
          <option value="" disabled>Выберите колонку</option>
          <option :value="i" v-for="i in list">{{i}}</option>
        </select>
      </div>

      <div class="selectStackedBar">
        <p>Колонки для гистограммы с приращением</p>
        <select ref="selectX" v-model="columnX">
          <option value="" disabled>Выберите колонку X</option>
          <option :value="i" v-for="i in list">{{i}}</option>
        </select>
        <select ref="selectY" v-model="columnY">
          <option value="" disabled>Выберите колонку Y</option>
          <option :value="i" v-for="i in list">{{i}}</option>
        </select>
      </div>

      <div class="button">
        <button class="btn" @click="chooseChartHandler">Применить</button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ChooseChart",
    data: () => ({
      selectColumn: [],
      columnX: [],
      columnY: [],
      list: '',
      isLine: false,
      isBar: false,
      isPie: false,
      isStackedBar: false,
    }),
    methods: {
    chooseChartLine() {
        if (this.isLine) {
          this.isPie = false
          this.isBar = false
          this.isStackedBar = false
        }
      },
      chooseChartBar() {
        if (this.isBar) {
          this.isPie = false
          this.isLine = false
          this.isStackedBar = false
        }
      },
      chooseChartPie() {
        if (this.isPie) {
          this.isBar = false
          this.isLine = false
          this.isStackedBar = false
        }
      },
      chooseChartStackedBar() {
        if (this.isStackedBar) {
          this.isBar = false
          this.isLine = false
          this.isPie = false
        }
      },
      async chooseChartHandler() {
        if (this.isBar === false && this.isPie === false && this.isLine === false && this.isStackedBar === false) {
          M.toast({
            html: 'Выберите тип графика',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.selectColumn.length === 0 && (this.columnX.length === 0 || this.columnY === 0)){
          M.toast({
            html: 'Выберите колонку',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.selectColumn.length > 1) {
          M.toast({
            html: 'Выберите только одну колонку',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.selectColumn.length > 1 && this.isPie) {
          M.toast({
            html: 'Выберите только одну колонку',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.columnX.length !== 0 && this.columnY.length !== 0 && this.isStackedBar === false) {
          M.toast({
            html: 'Выберите гистограмму с приращением',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if ((this.columnX.length === 0 || this.columnY.length === 0) && this.isStackedBar) {
          M.toast({
            html: 'Выберите колонки для гистограммы с приращением',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if ((this.columnX.length !== 0 || this.columnY.length !== 0) && this.selectColumn.length !== 0) {
          M.toast({
            html: 'Выберите только колонки для гистограммы или только колонки для диаграмм',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.selectColumn.length !== 0 && (this.columnX.length !== 0 || this.columnY.length !== 0)) {
          M.toast({
            html: 'Выберите только колонки для гистограммы или только колонки для диаграмм',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.columnX === this.columnY) {
          M.toast({
            html: 'Выберите разные колонки для гистограммы с приращением',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        }


        if (this.columnX.length !== 0) {
          this.columnX = this.columnX.split()
        }

        if (this.columnY.length !== 0) {
          this.columnY = this.columnY.split()
        }

        let formData = {
          selectColumn: this.selectColumn,
          columnX: this.columnX,
          columnY: this.columnY,
          isLine: this.isLine,
          isBar: this.isBar,
          isPie: this.isPie,
          isStackedBar: this.isStackedBar
        }
        console.log(formData)
        await this.$store.dispatch('buildChart', formData)
        this.$emit('choose')
      }
    },
    async mounted() {
      await this.$store.dispatch('getListColumnChooseChart')
      this.list = this.$store.state.table.listColumnChooseChart.data
      setTimeout(() => {
        M.FormSelect.init(this.$refs.select)
        M.FormSelect.init(this.$refs.selectX)
        M.FormSelect.init(this.$refs.selectY)
      }, 0)
    }
  }
</script>

<style scoped lang="scss">
  .choose {
    display: flex;
    margin: 10px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    min-height: 200px;

    .chooseChart {
      margin: 10px 0;
      border-right: 1px solid darkgrey;
      padding: 10px;

      div {
        margin: 5px 0;

        span {
          color: black;
        }
      }
    }

    .chooseColumn {
      margin: 10px 0;
      padding: 10px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      .selectStackedBar {
        margin-top: 25px;
        margin-bottom: 10px;
        p{
          margin: 0;
          font-size: 14px;
          color: black;
        }
      }

      .button {
        margin: 5px 0 10px 0;
        display: flex;
        justify-content: center;
      }
    }
  }
</style>