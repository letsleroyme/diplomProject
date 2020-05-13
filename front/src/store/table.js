import axios from 'axios'

export default {
  state: {
    file: '',
    list: ''
  },
  mutations: {
    setFile(state, file) {
      // console.log('mutation')
      state.file = file
      // console.log(state.file)
    },
    setList(state, list) {
      state.list = list
      // console.log(state.list)
    }
  },
  actions: {
    async uploadFile({dispatch, commit}, formData) {
      // console.log(checkData)
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
    },
    async getList({commit}) {
      return new Promise((resolve, reject) => {
        axios.get('http://localhost:5000/table')
          .then(resp => {
            resolve(resp)
            commit('setList', resp)
        })
          .catch(err => {
            reject(err)
            console.log(err)
          })
      })
    },
    async changeFile({dispatch, commit}, formData) {
      // console.log(formData)
      // console.log('succes')
      return new Promise((resolve, reject) => {
        axios.post( 'http://localhost:5000/table',
          formData,
          {
            headers: {
              'Content-Type': "application/json"
            }
          }
        ).then(resp => {
          resolve(resp)
          console.log(resp)
        })
          .catch(err => {
            reject(err)
            console.log(err)
          })
      })
    },
  }
}