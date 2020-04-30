import axios from 'axios'

export default {
  state: {
    file: ''
  },
  mutations: {
    setFile(state, file) {
      // console.log('mutation')
      state.file = file
      // console.log(state.file)
    }
  },
  actions: {
    async uploadFile({dispatch, commit}, formData) {
      // console.log(formData)
      // console.log('succes')
      return new Promise((resolve, reject) => {
        axios.post( 'http://localhost:5000/',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        ).then(resp => {
          resolve(resp)
          commit('setFile', resp)
          })
          .catch(err => {
            reject(err)
            console.log(err)
          })
      })
    }
  }
}