import React from 'react';
import PropTypes from 'prop-types';
import icons from './iconLib';

const Icon = ({ symbol, size, on }) => {
  const iconSrc = icons[symbol][on ? 'on' : 'off'];
  return (
    <img
      src={iconSrc}
      alt={`${symbol}-icon`}
      style={{ width: size, height: size }}
    />
  );
};

Icon.propTypes = {
  size: PropTypes.number,
  symbol: PropTypes.string.isRequired,
  on: PropTypes.bool
};

Icon.defaultProps = {
  size: 40,
  on: false
};

export default Icon;
