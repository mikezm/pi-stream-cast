import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import AudioPlayer from './components/AudioPlayer/AudioPlayer';
import reportWebVitals from './reportWebVitals';

//import { configureStore } from '@reduxjs/toolkit'
//import { Provider } from 'react-redux';
//import reducers from "./store/reducers/index";
//export const store = configureStore({
//  reducer: {
//    todos: todosReducer,
//    filters: filtersReducer
//  }
//})

const root = ReactDOM.createRoot(document.getElementById('root'));
//root.render(
//  <React.StrictMode>
//    <Provider store={store}>
//      <App />
//    </Provider>
//  </React.StrictMode>
//);

root.render(
  <React.StrictMode>
    <AudioPlayer />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
