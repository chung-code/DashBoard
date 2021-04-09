import React from 'react';
import { render } from 'react-dom';
import VerticalBar from './VerticalBar.jsx';

const styles = {
  fontFamily: 'sans-serif',
  textAlign: 'center',
};

const App = () => {
  return (
    <div style={styles}>
      <VerticalBar/>
    </div>
  )
}

export default App;