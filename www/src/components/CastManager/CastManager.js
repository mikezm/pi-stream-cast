import * as routes from '../../routes';
import React, { useState, useEffect } from "react";

function CastManager() {
  const [casts, setCasts] = useState([]);
  const [groups, setCastGroups] = useState([]);

  useEffect(() => {
    handleList();
  }, []);

  const handleList = async () => {
    try {
      const response = await fetch(routes.LIST_CASTS, {method: 'GET'});
      const data = await response.json();
      let singleCasts = [];
      let groupCasts = [];
      data.forEach(element => {
        if (element.type === 'group') {
          groupCasts.push(element);
        } else {
          singleCasts.push(element);
        }
      });
      setCasts(singleCasts);
      setCastGroups(groupCasts);
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  };
  
  return (
    <div className='row'>
      <div className='col'>
        <div className="cast-list">
          {casts.map((cast) => (
            <div key={cast.uuid}>{cast.name}</div>
          ))}
        </div>
      </div>
      <div className='col'>
        <div className="cast-list-group">
          {groups.map((cast) => (
            <div key={cast.uuid}>{cast.name}</div>
          ))}
        </div>
      </div>
    </div>
    
  );
}

export default CastManager;