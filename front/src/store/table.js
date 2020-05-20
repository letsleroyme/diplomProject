import axios from 'axios'

export default {
  state: {
    file: '',
    list: '',
    listColumnChooseChart: '',
    chartData: ''
  },
  mutations: {
    setFile(state, file) {
      state.file = file
    },
    setList(state, list) {
      state.list = list
    },
    setListColumnChooseChart(state, list) {
      state.listColumnChooseChart = list
    },
    setChartData(state, data) {
      state.chartData = data.data
    }
  },
  actions: {
    async uploadFile({dispatch, commit}, formData) {
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
          commit('setFile', resp)
        })
          .catch(err => {
            reject(err)
            console.log(err)
          })
      })
    },
    async getListColumnChooseChart({commit}) {
      return new Promise((resolve, reject) => {
        axios.get('http://localhost:5000/graphs')
          .then(resp => {
            resolve(resp)
            commit('setListColumnChooseChart', resp)
          })
          .catch(err => {
            reject(err)
            console.log(err)
          })
      })
    },
    async buildChart({dispatch, commit}, formData) {
      return new Promise((resolve, reject) => {
        axios.post( 'http://localhost:5000/graphs',
          formData,
          {
            headers: {
              'Content-Type': "application/json"
            }
          }
        ).then(resp => {
          resolve(resp)
          console.log(resp)
          commit('setChartData', resp)
        })
          .catch(err => {
            reject(err)
            console.log(err)
          })
      })
    }
  }
}