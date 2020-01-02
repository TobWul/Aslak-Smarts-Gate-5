import React, { useState } from "react";
import PropTypes from "prop-types";
import styles from "./Button.module.scss";
import { cn } from "../../lib/helpers";

const Button = ({ children, onClick }) => {
  const [on, setOn] = useState(false);

  const click = () => {
    onClick && onClick();
    setOn(!on);
  };

  return (
    <button onClick={click} className={cn(styles.button, on ? styles.on : "")}>
      <div className={styles.inner}>{children}</div>
    </button>
  );
};

Button.propTypes = {
  children: PropTypes.any.isRequired,
  onClick: PropTypes.func
};

export default Button;
