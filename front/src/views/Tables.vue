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
            <button class="btn">Кнопка 1</button>
            <button class="btn">Кнопка 2</button>
            <button class="btn">Кнопка 3</button>
            <button class="btn">Кнопка 4</button>
          </div>

          <div  class="table-body">
            <table border="1">
              <caption>Таблица размеров обуви</caption>
              <tr>
                <th>Россия</th>
                <th>Великобритания</th>
                <th>Европа</th>
                <th>Длина ступни, см</th>
              </tr>
              <tr><td>34,5</td><td>3,5</td><td>36</td><td>23</td></tr>
              <tr><td>35,5</td><td>4</td><td>36⅔</td><td>23–23,5</td></tr>
              <tr><td>36</td><td>4,5</td><td>37⅓</td><td>23,5</td></tr>
              <tr><td>36,5</td><td>5</td><td>38</td><td>24</td></tr>
              <tr><td>37</td><td>5,5</td><td>38⅔</td><td>24,5</td></tr>
              <tr><td>38</td><td>6</td><td>39⅓</td><td>25</td></tr>
            </table>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
  export default {
    name: 'tables',
    data:()=>({
      loader: true,
      file: ''
    }),
    mounted() {
      this.file = this.$store.state.table.file.data
      setTimeout(() => {
        if (this.file !== '') {
          this.loader = false
        }
      }, 1000)
    }
  }
</script>

<style lang="scss" scoped>
  .tables{
    height: 600px;
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
        justify-content: space-around;
      }

      .table-body {
        padding: 20px;

        table {
          height: 300px;
        }
      }
    }
  }
</style>