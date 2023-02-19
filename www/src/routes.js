const baseUri = process.env.PI_STREAM_CAST_ENV === 'prod' ? 'http://127.0.0.1' : 'http://127.0.0.1:5000';

export const AUDIO_STREAM = `${baseUri}/audio-stream`;
export const LIST_CASTS = `${baseUri}/list-casts`;
export const REFRESH_CASTS = `${baseUri}/refresh-casts`;
export const START_CAST = `${baseUri}/start-cast`;
export const STOP_CAST = `${baseUri}/stop-cast`;
export const STOP_STEAM = `${baseUri}/stop-stream`;
export const GET_VOLUME = `${baseUri}/get-volume`;
export const SET_VOLUME = `${baseUri}/set-volume`;
export const VOLUME_UP = `${baseUri}/volume-up`;
export const VOLUME_DOWN = `${baseUri}/volume-down`;
export const VOLUME_MUTE = `${baseUri}/volume-mute`;
export const VOLUME_UNMUTE = `${baseUri}/volume-unmute`;