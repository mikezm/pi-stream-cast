import * as routes from '../../routes';
import React, { useState, useEffect } from "react";

function CastManager() {
  const [casts, setCasts] = useState([]);

  useEffect(() => {
    handleList();
  }, []);

  const handleList = async () => {
    try {
      const response = await fetch(routes.LIST_CASTS, {method: 'GET'});
      const data = await response.json();
      setCasts(data);
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  };
  
  return (
    <div className="cast-list">
      {casts.map((cast) => (
        <div key={cast.uuid}>{cast.name}</div>
      ))}
    </div>
  );
}

export default CastManager;