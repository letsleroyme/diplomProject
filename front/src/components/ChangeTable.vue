<template>
  <div class="table-action">
    <div class="input-field col l4 action-1">
      <h4>Числовые столбцы</h4>
      <select ref="select" v-model="numberColumns" multiple>
        <option value="" disabled>Выберите колонку</option>
        <option :value="i" v-for="i in list">{{i}}</option>
      </select>
      <div class="check">
        <div class="check-1" @change="action1check1">
          <label>
            <input type="checkbox" v-model="action1_check1"/>
            <span>Заменить NaN на среднее по столбцу</span>
          </label>
        </div>
        <div class="check-2" @change="action1check2">
          <label>
            <input type="checkbox" v-model="action1_check2"/>
            <span>Удалить строки с NaN</span>
          </label>
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
        <div class="check-1" @change="action2check1">
          <label>
            <input type="checkbox" v-model="action2_check1"/>
            <span>Заменить NaN значением, которое встречается в большинстве</span>
          </label>
        </div>
        <div class="check-2" @change="action2check2">
          <label>
            <input type="checkbox" v-model="action2_check2"/>
            <span>Удалить строки с NaN</span>
          </label>
        </div>
        <div class="check-3" @change="action2check3">
          <label>
            <input type="checkbox" v-model="action2_check3"/>
            <span>Привести текстовые категории в числовые</span>
          </label>
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
        <div class="check-1" @change="action3check1">
          <label>
            <input type="checkbox" v-model="action3_check1"/>
            <span>Привести заглавные буквы к маленьким</span>
          </label>
        </div>
        <div class="check-2" @change="action3check2">
          <label>
            <input type="checkbox" v-model="action3_check2"/>
            <span>Убрать знаки препинания</span>
          </label>
        </div>
        <div class="check-3" @change="action3check3">
          <label>
            <input type="checkbox" v-model="action3_check3"/>
            <span>Удалить строки с NaN</span>
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ChangeTable",
    data: () => ({
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
      action1check1() {
        if (this.action1_check1) {
          this.action1_check2 = false
        }
      },
      action1check2() {
        if (this.action1_check2) {
          this.action1_check1 = false
        }
      },
      action2check1() {
        if (this.action2_check1) {
          this.action2_check2 = false
          this.action2_check3 = false
        }
      },
      action2check2() {
        if (this.action2_check2) {
          this.action2_check1 = false
          this.action2_check3 = false
        }
      },
      action2check3() {
        if (this.action2_check3) {
          this.action2_check1 = false
          this.action2_check2 = false
        }
      },
      action3check1() {
        if (this.action3_check1) {
          this.action3_check2 = false
          this.action3_check3 = false
        }
      },
      action3check2() {
        if (this.action3_check2) {
          this.action3_check1 = false
          this.action3_check3 = false
        }
      },
      action3check3() {
        if (this.action3_check3) {
          this.action3_check1 = false
          this.action3_check2 = false
        }
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
        console.log(formData)
        await this.$store.dispatch('changeFile', formData)
        this.$emit('changetable')
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
      },
    },
    async mounted() {
      await this.$store.dispatch('getList')
      this.list = this.$store.state.table.list.data
      setTimeout(() => {
        M.FormSelect.init(this.$refs.select)
        M.FormSelect.init(this.$refs.select2)
        M.FormSelect.init(this.$refs.select3)
      }, 1)
    }
  }
</script>

<style scoped lang="scss">
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

      div {
        margin: 5px 0;

        span {
          color: black;
        }
      }

    }
    .action-2 {
      margin: 10px 0;
      padding: 10px;
      border-right: 1px solid grey;
      border-left: 1px solid grey;

      div {
        margin: 5px 0;

        span {
          color: black;
        }
      }
      .button {
        margin: 15px 0 5px 0;
        display: flex;
        justify-content: center;
      }


    }
    .action-3 {
      margin: 10px 0;
      padding: 10px;

      div {
        margin: 5px 0;

        span {
          color: black;
        }
      }
    }
  }
</style>