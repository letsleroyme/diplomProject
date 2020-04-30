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
        </form>
      </div>
      <div class="col l1 ">
        <div class="upload-btn">
          <button class="btn" @click="submitFile">Загрузить</button>
<!--          <div>{{info}}</div>-->
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
    info: null
  }),
  methods: {
    handleUploadFile() {
      this.file = this.$refs.file.files[0]
    },
    async submitFile() {
      let formData = new FormData()
      formData.append('file', this.file)
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

    .upload-btn {
      padding-top: 15px;

      button {
        height: 45px;
      }
    }
  }
</style>