import React, { useEffect } from 'react';
import useIkeaComponent from '../../hooks/useIkeaComponent';
import Button from '../Button/Button';
import db from '../../db/firebase';

const Outlet = () => {
  const [on, toggle] = useIkeaComponent(db.collection('outlets').doc('65539'));

  return (
    <Button on={on} onClick={toggle}>
      Ovn
    </Button>
  );
};

export default Outlet;
