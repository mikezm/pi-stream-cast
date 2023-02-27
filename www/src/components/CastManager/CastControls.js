
import * as routes from '../../routes';
import React, { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Tooltip from '@mui/material/Tooltip';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import StopIcon from '@mui/icons-material/Stop';
import VolumeUpIcon from '@mui/icons-material/VolumeUp';
import VolumeDownIcon from '@mui/icons-material/VolumeDown';
import VolumeMuteIcon from '@mui/icons-material/VolumeMute';
import VolumeOffIcon from '@mui/icons-material/VolumeOff';

function CastControls(props) {
  const { cast, onCastPlay } = props;
  const [isPlaying, setIsPlaying] = useState(false);
  const [isPlayDisabled, setIsPlayDisabled] = useState(true);
  const [isMuted, setIsMuted] = useState(false);
  const [isVolumeDisabled, setIsVolumeDisabled] = useState(false);

  useEffect(() => {
    setIsPlayDisabled(!(props.cast.uuid));
  }, [props.cast]);

  const delay = async () => {
    return new Promise(resolve => setTimeout(resolve, 1000));
  };
  
  const handlePlay = async (id) => {
    onCastPlay(!isPlaying);
    setIsPlayDisabled(true);
    const uri = isPlaying ? routes.STOP_CAST : `${routes.START_CAST}/${id}`;
    //const data = await routes.get(uri);
    await delay();
    setIsPlayDisabled(false);
    setIsPlaying(!isPlaying);
    
  };

  const handleMute = async () => { 
    setIsVolumeDisabled(true);
    const uri = isMuted ? routes.VOLUME_UNMUTE : routes.VOLUME_MUTE;
    //const data = await routes.get(uri);
    await delay();
    setIsVolumeDisabled(false);
    setIsMuted(!isMuted);
  };
  

  const handleVolumeUp = async () => {
    setIsVolumeDisabled(true); 
    //const data = await routes.get(routes.VOLUME_UP);
    await delay();
    setIsVolumeDisabled(false);
  };

  const handleVolumeDown = async () => {
    setIsVolumeDisabled(true); 
    //const data = await routes.get(routes.VOLUME_DOWN);
    await delay();
    setIsVolumeDisabled(false); 
  };
  //useEffect(() => {
  //  handleMute();
  //}, []);
  //useEffect(() => {
  //  handleVolumeUp();
  //}, []);
  //useEffect(() => {
  //  handleVolumeDown();
  //}, []);
  

  return (
    <Card sx={{ display: 'flex' }}>
      <Box sx={{ display: 'flex', flexDirection: 'column' }}>
        <CardContent sx={{ flex: '1 0 auto' }}>
          <Typography component="div" variant="h5">
            {cast.name}
          </Typography>
          <Typography variant="subtitle1" color="text.secondary" component="div">
            {cast.ip}
          </Typography>
        </CardContent>
        <Box sx={{ display: 'flex', alignItems: 'center', pl: 1, pb: 1 }}>
          {isPlaying ? 
            <Tooltip title="Stop">
              <span>
                <IconButton aria-label="stop" onClick={handlePlay} disabled={isPlayDisabled}>
                  <StopIcon sx={{ height: 38, width: 38 }} />
                </IconButton>
              </span>
            </Tooltip>
            :
            <Tooltip title="Play">
              <span>
                <IconButton aria-label="play" onClick={handlePlay} disabled={isPlayDisabled}>
                  <PlayArrowIcon sx={{ height: 38, width: 38 }} />
                </IconButton>
              </span>
            </Tooltip>
          }
          {isMuted ?
            <Tooltip title="Unmute">
              <span>
                <IconButton aria-label="unmute" onClick={handleMute} disabled={!isPlaying || isVolumeDisabled || isPlayDisabled}>
                  <VolumeOffIcon />
                </IconButton>
              </span>
            </Tooltip>
          :
            <Tooltip title="Mute">
              <span>
                <IconButton aria-label="mute" onClick={handleMute} disabled={!isPlaying || isVolumeDisabled || isPlayDisabled}>
                  <VolumeMuteIcon />
                </IconButton>
              </span>
            </Tooltip>
          }
          <Tooltip title="Volume Down">
            <span>
              <IconButton aria-label="volume down" onClick={handleVolumeDown} disabled={!isPlaying || isVolumeDisabled || isMuted || isPlayDisabled}>
                <VolumeDownIcon />
              </IconButton>
            </span>
          </Tooltip>
          <Tooltip title="Volume Up">
            <span>
              <IconButton aria-label="volume up" onClick={handleVolumeUp} disabled={!isPlaying || isVolumeDisabled || isMuted || isPlayDisabled}>
                <VolumeUpIcon />
              </IconButton>
            </span>
          </Tooltip>
        </Box>
      </Box>
    </Card>
  );

}

export default CastControls;