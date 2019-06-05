import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
  state = {
    processed_image: null
  }

  async componentDidMount() {
    const processed_image = await axios.get('http://album-generator-server.surge.sh/generate');
    this.setState({ processed_image: processed_image.data });
  }

  render() {
    const { processed_image } = this.state;

    return (
      <div className="App">
        <header className="App-header">
          {processed_image && <img src={`data:image/jpeg;base64,${processed_image}`} alt="album art" />}
        </header>
      </div>
    );
  }
}

export default App;

