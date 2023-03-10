import * as routes from '../../routes';
import React, { useState } from "react";
import play from '../../img/play.svg'
import stop from '../../img/stop.svg';

function MediaControls() {
  const [isPlaying, setIsPlaying] = useState(false);
  
  const handlePlay = async (id) => {
    setIsPlaying(true);
    try {
      const response = await fetch(`${routes.START_CAST}/${id}`, {method: 'GET'});
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleStop = async () => {
    setIsPlaying(false);
    try {
      const response = await fetch(routes.STOP_CAST, {method: 'GET'});
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="play-btn " style={{display: "flex"}}>
        <button className="ctrl-btn"
          onClick={handlePlay} 
          disabled={isPlaying} 
          style={{
            backgroundColor: "#000",
            height: "150px",
            width: "150px",
            radius: "50%",
            float: "left",
            inline: "true"
          }}>
          <img src={play} className="play-btn__svg" alt="Play" />
        </button>
        <button className="ctrl-btn"
          onClick={handleStop} 
          disabled={!isPlaying}
          style={{
            backgroundColor: "#000",
            height: "150px",
            width: "150px",
            radius: "50%",
            float: "right",
            inline: "true"
          }}
        >
          <img src={stop} className="play-btn__svg" alt="Stop" />
        </button>
      </div>
  );
}

export default MediaControls;
