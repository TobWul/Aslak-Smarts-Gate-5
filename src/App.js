import React from 'react';
import Button from './components/Button/Button';
import LightPanel from './components/lights/LightPanel';
import Outlet from './components/outlets/Outlet';
import styles from './App.module.scss';

function App() {
  return (
    <main className={styles.app}>
      <LightPanel />
      <Outlet />
    </main>
  );
}

export default App;
