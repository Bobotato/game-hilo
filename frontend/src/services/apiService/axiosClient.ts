import axios from 'axios'

const apiBaseURL = import.meta.env.VITE_APIBASEURL

export const apiClient = axios.create({
  baseURL: apiBaseURL,
  withCredentials: true,
  headers: {
    Accept: 'application/json',
    'content-type': 'application/json',
    timeout: 1000
  },
})
