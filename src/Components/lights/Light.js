import React, { useEffect, useState } from 'react';
import Button from '../Button/Button';
import db from '../../db/firebase';
import { toggleLight } from '../../db/controlLights';
import useIkeaComponent from '../../hooks/useIkeaComponent';

const Light = ({ light }) => {
  const lightRef = db.collection('lights').doc(light.id);
  const [on, toggle] = useIkeaComponent(lightRef);

  return (
    <Button on={on} onClick={toggle}>
      {light.id}
    </Button>
  );
};

export default Light;
