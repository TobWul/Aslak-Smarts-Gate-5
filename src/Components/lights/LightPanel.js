import React, { useEffect, useState } from 'react';
import db from '../../db/firebase';
import { getLights } from '../../db/controlLights';
import Light from './Light';

const LightPanel = () => {
  const [lights, setLights] = useState([]);
  useEffect(() => {
    getLights
      .then(lights => setLights(lights))
      .catch(error => console.error(error));
  });

  return lights.map(light => <Light light={light} key={light.id} />);
};

export default LightPanel;
