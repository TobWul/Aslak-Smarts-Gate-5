import React, { useEffect, useState } from 'react';
import db from '../db/firebase';

const Temperature = () => {
  const [temperature, setTemperature] = useState(20);

  useEffect(() => {
    db.collection('settings')
      .doc('currentTemp')
      .onSnapshot(doc =>
        setTemperature(Math.round(doc.data().currentTemp * 10) / 10)
      );
  }, []);

  return <h1>{temperature}°C</h1>;
};

export default Temperature;
