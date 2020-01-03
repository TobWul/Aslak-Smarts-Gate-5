import React from 'react';
import LightPanel from './components/light/LightPanel';
import Oven from './components/Oven';
import Temperature from './components/Temperature';
import styles from './App.module.scss';

function App() {
  return (
    <main className={styles.app}>
      <Temperature />
      <Oven />
      <LightPanel />
    </main>
  );
}

export default App;
