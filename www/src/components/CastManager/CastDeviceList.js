import React, { useState } from "react";
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import SpeakerIcon from '@mui/icons-material/Speaker';
import SpeakerGroupIcon from '@mui/icons-material/SpeakerGroup';


function CastDeviceList(props) {
  const { casts, onCastSelect, disabled } = props;

  const [selectedIndex, setSelectedIndex] = useState("");

  const handleListItemClick = (event, uuid) => {
    setSelectedIndex(uuid);
    onCastSelect(casts.find(c => c.uuid === uuid));
  };

  return (
    <Box sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
      <nav aria-label="main mailbox folders">
        <List>
          {casts.map((cast) => (
            <ListItemButton 
              key={cast.uuid} 
              selected={selectedIndex === cast.uuid}
              onClick={(event) => handleListItemClick(event, cast.uuid)}
              disabled={disabled}
            >
              <ListItemIcon>
                {cast.type === 'group' ? <SpeakerGroupIcon /> : <SpeakerIcon />}
              </ListItemIcon>
              <ListItemText primary={cast.name} />
            </ListItemButton>
          ))}
        </List>
      </nav>
    </Box>
  );
}

export default CastDeviceList;
