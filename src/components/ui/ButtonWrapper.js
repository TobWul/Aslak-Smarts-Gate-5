import React from 'react';
import PropTypes from 'prop-types';
import styles from './ButtonWrapper.module.scss';

const ButtonWrapper = ({ children }) => {
  return <div className={styles.buttonwrapper}>{children}</div>;
};

ButtonWrapper.propTypes = {
  children: PropTypes.any.isRequired
};

export default ButtonWrapper;
