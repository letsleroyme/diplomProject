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
    </div>
    <div class="input-field col l6 chooseColumn">
      <select ref="select" v-model="selectColumn" multiple>
        <option value="" disabled>Выберите колонку</option>
        <option :value="i" v-for="i in list">{{i}}</option>
      </select>

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
      list: '',
      isLine: false,
      isBar: false,
      isPie: false
    }),
    methods: {
    chooseChartLine() {
        if (this.isBar && this.isLine || this.isPie && this.isLine ) {
          this.isPie = false
          this.isBar = false
        }
      },
      chooseChartBar() {
        if (this.isBar && this.isPie || this.isBar && this.isLine) {
          this.isPie = false
          this.isLine = false

        }
      },
      chooseChartPie() {
        if (this.isBar && this.isPie || this.isLine && this.isPie) {
          this.isBar = false
          this.isLine = false

        }
      },
      async chooseChartHandler() {
        if (this.isBar === false && this.isPie === false && this.isLine === false) {
          M.toast({
            html: 'Выберите тип графика',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.selectColumn.length === 0){
          M.toast({
            html: 'Выберите колонку',
            displayLength: 2000,
            classes: 'red accent-4'
          })
          return
        } else if (this.selectColumn.length > 2) {
          M.toast({
            html: 'Выберите не больше двух колонок',
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
        }

        let formData = {
          selectColumn: this.selectColumn,
          isLine: this.isLine,
          isBar: this.isBar,
          isPie: this.isPie
        }
        await this.$store.dispatch('buildChart', formData)
        this.$emit('choose')
      }
    },
    async mounted() {
      await this.$store.dispatch('getListColumnChooseChart')
      this.list = this.$store.state.table.listColumnChooseChart.data
      setTimeout(() => {
        M.FormSelect.init(this.$refs.select)
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

      .button {
        margin: 5px 0 10px 0;
        display: flex;
        justify-content: center;
      }
    }
  }
</style>