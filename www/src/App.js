import './App.css';
import React, { useState } from 'react';
import play from './img/play.svg';
import stop from './img/stop.svg';

function App() {
  const baseUri = process.env.PI_STREAM_CAST_ENV === 'prod' ? 'http://localhost' : 'http://localhost:5000';
  const [isPlaying, setIsPlaying] = useState(false);
  
  const handlePlay = async () => {
    setIsPlaying(true);
    //try {
    //  const response = await fetch(`${baseUri}/api/audio`, {
    //    method: 'GET'
    //  });
    //  const data = await response.json();
    //  console.log(data);
    //} catch (error) {
    //  console.error(error);
    //}

    try {
      const response = await fetch(`${baseUri}/start-cast`, {
        method: 'GET'
      });
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }

  };

  const handleStop = async () => {
    setIsPlaying(false);
    try {
      const response = await fetch(`${baseUri}/stop-cast`, {
        method: 'GET'
      });
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h3>
          Pi Stream Cast
        </h3>
      </header>
      <div class="play-btn " style={{display: "flex"}}>
        <button class="ctrl-btn"
          onClick={handlePlay} 
          disabled={isPlaying} 
          style={{
            backgrougColor: "#000",
            height: "150px",
            width: "150px",
            radius: "50%",
            float: "left",
            inline: "true"
          }}>
          <img src={play} class="play-btn__svg" alt="Play" />
        </button>
        <button class="ctrl-btn"
          onClick={handleStop} 
          disabled={!isPlaying}
          style={{
            backgrougColor: "#000",
            height: "150px",
            width: "150px",
            radius: "50%",
            float: "right",
            inline: "true"
          }}
        >
          <img src={stop} class="play-btn__svg" alt="Stop" />
        </button>
      </div>
    </div>
  );
}

export default App;
