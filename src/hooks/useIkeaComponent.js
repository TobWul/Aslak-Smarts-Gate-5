import { useState, useEffect } from 'react';

const useIkeaComponent = componentRef => {
  const [on, setOn] = useState(false);
  const [brightness, setBrightness] = useState(0);

  useEffect(() => {
    componentRef.onSnapshot(doc => {
      setOn(doc.data().on);
      setBrightness(parseFloat(doc.data().brightness));
    });
  }, []);

  const toggle = () => {
    componentRef.update({ on: !on });
  };

  return { on, toggle, brightness, setBrightness };
};

export default useIkeaComponent;
