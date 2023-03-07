const baseUri = process.env.NODE_ENV === 'production' ? 
  'http://192.168.50.242/api'
  : 
  'http://192.168.50.242:5000/api';

export const STATUS = `${baseUri}/status`;
export const LIST_CASTS = `${baseUri}/list-casts`;
export const REFRESH_CASTS = `${baseUri}/refresh-casts`;
export const START_CAST = `${baseUri}/start-cast`;
export const STOP_CAST = `${baseUri}/stop-cast`;
export const STOP_STREAM = `${baseUri}/stop-stream`;
export const GET_VOLUME = `${baseUri}/get-volume`;
export const SET_VOLUME = `${baseUri}/set-volume`;
export const VOLUME_UP = `${baseUri}/volume-up`;
export const VOLUME_DOWN = `${baseUri}/volume-down`;
export const VOLUME_MUTE = `${baseUri}/volume-mute`;
export const VOLUME_UNMUTE = `${baseUri}/volume-unmute`;
export const get = async (uri) => {
  try {
    const response = await fetch(uri, {method: 'GET'});
    const data = await response.json();
    console.log(uri, data);
    return data;
  } catch (error) {
    console.error(uri, error);
  }
};