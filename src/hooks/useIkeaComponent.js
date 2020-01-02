import { useState, useEffect } from 'react';
import db from '../db/firebase';

const useIkeaComponent = componentRef => {
  const [on, setOn] = useState(false);

  useEffect(() => {
    componentRef.onSnapshot(doc => setOn(doc.data().on));
  }, []);

  const toggle = () => {
    componentRef.update({ on: !on });
  };

  return [on, toggle];
};

export default useIkeaComponent;
