import React, {Component, useState, useEffect} from 'react'
import { render } from 'react-dom';
import VerticalBar from './VerticalBar.jsx';
// import useFetch from './useFetch.js';

const styles = {
  fontFamily: 'sans-serif',
  textAlign: 'center',
};

const App = () => {

  const [todos, setTodos] = useState([]);

  const fetchInitialData = async() => {
    const response = await fetch('http://localhost:5000/dash'); //미리 만들어놓은 api 서버
    const initialData = await response.json();
    setTodos(initialData);
  }

  useEffect( () => {
    fetchInitialData(); 
  }, [])
  
  useEffect( () => {
    console.log("새로운내용", todos);
  }, [])

  return (
    <div style={styles}>
      <VerticalBar todos={todos} />
    </div>
  )
}

export default App;