import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [stats, setCurrentStats] = useState([])

  useEffect(() => {
    fetch('/tracker').then(res => res.json()).then(data => {
      setCurrentStats(data.tracker)
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        
        {stats[1][0]}: {stats[1][1]}
      </header>
    </div>
  );
}

export default App;
