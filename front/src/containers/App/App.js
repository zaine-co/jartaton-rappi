import React, { Component } from 'react';
import './App.css';
import Header from '../../components/Ui/Header/Header';
import AppBody from '../../components/Ui/AppBody/AppBody';
import Jartaton from '../../components/Jartaton/Jartaton';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Jartaton />
      </div>
    );
  }
}

export default App;
