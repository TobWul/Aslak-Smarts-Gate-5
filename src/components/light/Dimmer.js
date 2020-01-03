import React from 'react';
import PropTypes from 'prop-types';

const Dimmer = props => {
  return (
    <div>
      <input
        type="range"
        min="1"
        max="100"
        value="50"
        class="slider"
        id="myRange"
      />
    </div>
  );
};

Dimmer.propTypes = {};

export default Dimmer;
