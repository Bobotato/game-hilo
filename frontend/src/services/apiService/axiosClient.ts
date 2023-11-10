import axios from 'axios'

const apiBaseURL = import.meta.env.VITE_APIBASEURL

export const apiClient = axios.create({
  withCredentials: true,
  baseURL: apiBaseURL,
  headers: {
    Accept: 'application/json',
    'content-type': 'application/json',
    timeout: 1000,
  },
})
