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
  export default {
    name: 'tables',
    data:()=>({
      loader: true,
      file: '',
      tables: ''
    }),
    mounted() {
      this.file = this.$store.state.table.file.data
      console.log(typeof this.file)
      setTimeout(() => {
        if (this.file.length !== 0) {
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
        height: 100px;
      }

      .table-body {
        padding: 20px 10px 10px 10px;
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