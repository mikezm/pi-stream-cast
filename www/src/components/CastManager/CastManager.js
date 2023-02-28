import * as routes from '../../routes';
import React, { useState, useEffect } from "react";
import CastDeviceList from './CastDeviceList';
import CastControls from './CastControls';
import Typography from '@mui/material/Typography';
import Tooltip from '@mui/material/Tooltip';
import Grid from '@mui/material/Grid';
import RefreshIcon from '@mui/icons-material/Refresh';
import IconButton from '@mui/material/IconButton';

function CastManager() {
  const [casts, setCasts] = useState([]);
  const [cast, setCast] = useState({});
  const [listDisabled, setListDisabled] = useState(false);
  const [isRefreshDisabled, setIsRefreshDisabled] = useState(false);

  const handleCastSelect = (value) => {
    setCast({...value, isActive: false});
  };

  const handleCastPlay = (value) => {
    setListDisabled(!listDisabled);
  };

  useEffect(() => {
    const getStatus = async () => {
      const status = await routes.get(routes.STATUS);
      if (status.streamStatus && status.castStatus){
        setCast({...status.castInfo, isActive: true });
        handleList();
        setListDisabled(true);
      } else {
        handleList();
      }
    };

    getStatus();
  }, []);

  const handleList = async () => {
    try {
      const data = await routes.get(routes.LIST_CASTS);
      let singleCasts = [];
      let groupCasts = [];
      data.forEach(element => {
        if (element.type === 'group') {
          groupCasts.push(element);
        } else {
          singleCasts.push(element);
        }
      });
      setCasts([...groupCasts, ...singleCasts]);
    } catch (error) {
      console.error(error);
    }
  };

  const handleRefresh = async () => {
    setIsRefreshDisabled(true);
    await fetch(routes.REFRESH_CASTS, {method: 'GET'});
    console.log("refreshed");
    handleList();
    setIsRefreshDisabled(false);
  };

  const ListHeader = () => {
    return (
      <Grid container spacing={2}>  
        <Grid item xs={9}>
          <Typography sx={{ mt: 4, mb: 2 }} variant="h6" component="span">
            Available Speakers 
          </Typography>
        </Grid>
        <Grid item xs={3}>
          <Tooltip title="Refresh">
            <span>
              <IconButton aria-label="refresh" onClick={handleRefresh} disabled={isRefreshDisabled || listDisabled}>
                <RefreshIcon />
              </IconButton>
            </span>
          </Tooltip>
        </Grid>
      </Grid>
    );
  };
  
  return (
    <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }} alignItems="baseline">
      <Grid item xs={12} md={4}>
        <ListHeader />
        <CastDeviceList casts={casts} onCastSelect={handleCastSelect} disabled={listDisabled}/>
      </Grid>
      <Grid item xs={12} md={8}>
        <CastControls cast={cast} onCastPlay={handleCastPlay}/>
      </Grid>
    </Grid>
  );
}

export default CastManager;