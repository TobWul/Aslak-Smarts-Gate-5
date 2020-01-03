import React from 'react';
import useIkeaComponent from '../hooks/useIkeaComponent';
import Button from './ui/Button';
import db from '../db/firebase';
import Icon from './ui/Icon';
import ButtonWrapper from './ui/ButtonWrapper';

const Oven = () => {
  const [on, toggle] = useIkeaComponent(db.collection('outlets').doc('65539'));

  return (
    <ButtonWrapper>
      <Button on={on} onClick={toggle}>
        <Icon symbol="oven" on={on} />
      </Button>
    </ButtonWrapper>
  );
};

export default Oven;
