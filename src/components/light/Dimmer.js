import React, { useState, useRef } from 'react';
import PropTypes from 'prop-types';
import styles from './Dimmer.module.scss';
import { debounce } from '../../lib/helpers';
import db from '../../db/firebase';
import Indicator from '../ui/Indicator';

const Dimmer = ({ min, max, step, lightInstanceId }) => {
  const [value, setValue] = useState(min);
  const lights = [];
  const delayedQuery = useRef(
    debounce(brightness => {
      db.collection('lights')
        .doc(lightInstanceId)
        .update({ brightness: brightness });
    }, 300)
  ).current;

  const changeHandler = e => {
    setValue(e.target.value);
    delayedQuery((e.target.value / max) * 100);
  };

  const createLights = () => {
    for (let i = 0; i < max / step; i++) {
      lights.push(<div className={styles.light}></div>);
    }
  };

  createLights();

  return (
    <div className={styles.dimmerContainer}>
      <div className={styles.lights}>
        {[...Array(max / step)].map((light, index) => (
          <Indicator on={index < value / step} key={index} />
        ))}
      </div>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        className={styles.dimmer}
        onChange={changeHandler}
      />
    </div>
  );
};

Dimmer.propTypes = {
  min: PropTypes.number.isRequired,
  max: PropTypes.number.isRequired,
  step: PropTypes.number.isRequired,
  lightInstanceId: PropTypes.string.isRequired
};

export default Dimmer;