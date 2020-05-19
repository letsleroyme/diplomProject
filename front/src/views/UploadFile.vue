<template>
  <div class="container">
    <div class="row upload-file">
      <div class="col l8 offset-l1">
        <form action="#">
          <div class="file-field input-field">
            <div class="btn">
              <span>File</span>
              <input type="file" ref="file" @change="handleUploadFile">
            </div>
            <div class="file-path-wrapper">
              <input class="file-path validate" type="text">
            </div>
          </div>
          <div class="check">
            <label>
              <input type="checkbox" @click="checked"/>
              <span>Первая строка является заголовком</span>
            </label>
          </div>
        </form>
      </div>
      <div class="col l1 ">
        <div class="upload-btn">
          <button class="btn" @click="submitFile">Загрузить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'uploadFile',
  data:()=>({
    file: '',
    check: false
  }),
  methods: {
    handleUploadFile() {
      this.file = this.$refs.file.files[0]
    },
    checked() {
      this.check = !this.check
    },
    async submitFile() {
      if (this.file === '' || this.file === undefined) {
        M.toast({
          html: 'Загрузите файл',
          displayLength: 2000,
          classes: 'red accent-4'
        })
        return
      }
      let csv = this.file.name.split('.')[1]
      if (csv !== 'csv') {
        M.toast({
          html: 'Формат файла должен быть ".csv"',
          displayLength: 2000,
          classes: 'red accent-4'
        })
        return
      }
      let formData = new FormData()
      formData.append('file', this.file)
      formData.append('check', this.check)
      await this.$store.dispatch('uploadFile', formData)
      await this.$router.push('/tables')
    }
  }
}
</script>

<style lang="scss" scoped>
  .upload-file {
    height: 250px;
    margin-top: 100px;
    padding-top: 70px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);

    .check {
      padding-left: 2px;
      span {
        color: #575757;
      }
    }

    .upload-btn {
      padding-top: 15px;

      button {
        height: 45px;
      }
    }
  }
</style>