import * as routes from '../../routes';
import React, { useState, useEffect } from "react";
import CastDeviceList from './CastDeviceList';
import CastControls from './CastControls';
import Grid from '@mui/material/Grid';

function CastManager() {
  const [casts, setCasts] = useState([]);
  const [cast, setCast] = useState({});
  const [listDisabled, setListDisabled] = useState(false);

  const handleCastSelect = (value) => {
    setCast(value);
  };

  const handleCastPlay = (value) => {
    setListDisabled(!listDisabled);
  };

  useEffect(() => {
    handleList();
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
  
  return (
    <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }} alignItems="baseline">
      <Grid item xs={12} md={4}>
        <CastDeviceList casts={casts} onCastSelect={handleCastSelect} disabled={listDisabled}/>
      </Grid>
      <Grid item xs={12} md={8}>
        <CastControls cast={cast} onCastPlay={handleCastPlay}/>
      </Grid>
    </Grid>
  );
}

export default CastManager;