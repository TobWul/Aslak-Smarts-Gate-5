import React from 'react';
import Button from '../ui/Button';
import db from '../../db/firebase';
import useIkeaComponent from '../../hooks/useIkeaComponent';
import Icon from '../ui/Icon';
import Dimmer from './Dimmer';
import ButtonWrapper from '../ui/ButtonWrapper';

const Light = ({ light }) => {
  const lightRef = db.collection('lights').doc(light.id);
  const [on, toggle] = useIkeaComponent(lightRef);

  return (
    <ButtonWrapper>
      <Button on={on} onClick={toggle}>
        <Icon symbol="light" on={on} />
      </Button>
      <Dimmer min={10} max={100} step={10} lightInstanceId={`${light.id}`} />
    </ButtonWrapper>
  );
};

export default Light;
