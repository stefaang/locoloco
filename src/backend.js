import axios from 'axios'

let $axios = axios.create({
  baseURL: 'http://localhost:5000/api',
  // baseURL: '/api',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  console.log(response.data)
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  async fetchResource () {
    return $axios.get('/racer/xxx')
      .then(response => response.data)
  },

  async fetchMarkers () {
    return $axios.get('/marker')
      .then(response => response.data)
  },

  async fetchSecureResource () {
    return $axios.get('/secure-resource/zzz')
      .then(response => response.data)
  }
}
