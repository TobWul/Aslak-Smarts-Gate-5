import React from 'react';
import styles from './Indicator.module.scss';
import { cn } from '../../lib/helpers';

const Indicator = ({ on }) => {
  return <div className={cn(styles.light, on ? styles.on : '')} />;
};

export default Indicator;
