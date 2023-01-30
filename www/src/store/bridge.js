import axios from 'axios';

const { REACT_APP_API_BASE } = process.env;

const instance = axios.create({
    baseURL: REACT_APP_API_BASE
});

export default instance;