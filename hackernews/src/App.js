import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

function add(x,y) {
  return x+y;
}
function add1(x) {
  return x+1;
}
let key=3;
console.log([1,2,3].map(function(x,index){
  return add(x,index);
}));

class App extends Component {
  render() {
    const helloWorld = 'Welcome to the Road to learn React';
    var name = {
      'first': "Bobby",
      'last': "Fischer"
    };
    return (
      <div className="App">
        <h2>{helloWorld}</h2>
        <h3>{name.first + " " + name.last}</h3> 
      </div>
    );
  }
}

export default App;
