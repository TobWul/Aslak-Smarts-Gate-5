import React from "react";
import Button from "./Components/Button/Button";
import styles from "./App.module.scss";

function App() {
  return (
    <main className={styles.app}>
      <Button>Lights</Button>
    </main>
  );
}

export default App;
