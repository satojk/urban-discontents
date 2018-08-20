import { Switch, Route } from 'react-router-dom'
import React, { Component } from 'react';
import Home from './Home/index';
import Curitiba from './Curitiba/index';


class App extends Component {
  render() {
    return (
      <main>
        <Switch>
          <Route exact path='/' component={Home}/>
          <Route path='/curitiba' component={Curitiba}/>
        </Switch>
      </main>
    );
  }
}

export default App;
