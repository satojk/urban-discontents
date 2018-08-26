import React, { Component } from 'react';
import './index.css';
import '../data/commons.css';
import '../data/animate.css';
import ProjectHeader from '../data/project-header.js';
import WorldMap from './map';
import Reveal from 'react-reveal/Reveal';

class Home extends Component {
  constructor() {
    super();
    this.state = {
      cities: ['curitiba', 'phoenix'],
      nameShowing: ['Name-hidden', 'Name-hidden']
    }
  }

  showName = (cityName) => {
    let ix = this.state.cities.indexOf(cityName);
    let newNameShowing = this.state.nameShowing;
    newNameShowing[ix] = 'Name-visible';
    this.setState({
      nameShowing: newNameShowing
    });
  }

  hideName = (cityName) => {
    let ix = this.state.cities.indexOf(cityName);
    let newNameShowing = this.state.nameShowing;
    newNameShowing[ix] = 'Name-hidden';
    this.setState({
      nameShowing: newNameShowing
    });
  }


  render() {
    return (
      <div className="Home">
        <ProjectHeader />
        <Reveal effect="fadeIn" duration={3000}>
        <p className="Text-regular" align="justify">
        Urban population growth has exploded since the mid-20th century, and projections suggest that this growth will only accelerate.  By the year 2030, 60 percent of the world's population will live in cities. Wrapped up in this story of worldwide urbanization is the often ignored, but nevertheless tantamount process of urban vulnerability and displacement. Global Urbanization and its Discontents is concerned with uncovering how, as cities expand and develop, vulnerable communities are left behind, outside, or between the cracks.
        </p>
        </Reveal>
        <Reveal effect="fadeIn" duration={3000}>
        <p className="Text-regular" align="justify">
        The elements and conditions that determine the city’s geography of vulnerability may be formal or informal, institutional or grassroots, regional or local. This is why this project aims to take an interdisciplinary, historical, and comparative approach to global urbanization.
        </p>
        </Reveal>
        <Reveal effect="fadeIn" duration={3000}>
        <p className="Text-regular" align="justify">
         This website visualizes this research of trends in urban growth in 30 cities across history and the world in order to tell a more complete story of the city, and the inequality and marginality therein, in the 20th and 21st centuries.
        </p>
        </Reveal>
        <Reveal effect="fadeIn" duration={3000}>
        <p className="Text-quote" align="center" style={{fontStyle: "italic"}}>
        “Rather than affirming the current condition of cities as the expression of transhistorical laws of social organization, bureaucratic rationality or economic efficiency, critical urban theory emphasizes the politically and ideologically mediated, socially contested and therefore malleable character of urban space—that is, its continual (re)construction as a site, medium and outcome of historically specific relations of social power.”
        </p>
        </Reveal>

        <Reveal effect="fadeIn" duration={3000}>
        <p className="Map-header" align="center">
          Explore urbanization in the cities below
        </p>
        </Reveal>
        <div style={{position: "relative", height: "40%", width: "100%"}}>
          <WorldMap />
          <div style={{width: "20%", height: "30%", position: "absolute",
          top: "59.2%", left: "31.5%", zIndex: "1"}}>
            <Reveal effect="fadeIn" duration={7000}>
              <a href="curitiba" className="Dot" onMouseEnter={() => {this.showName('curitiba')}}
              onMouseLeave={() => {this.hideName('curitiba')}}>.</a>
            </Reveal>
            <p className={this.state.nameShowing[0]}>Curitiba</p>
          </div>
          <div style={{width: "20%", height: "30%", position: "absolute",
          top: "21.5%", left: "16.5%", zIndex: "1", float: "left"}}>
            <Reveal effect="fadeIn" duration={7000}>
              <a href="phoenix" className="Dot" onMouseEnter={() => {this.showName('phoenix')}}
              onMouseLeave={() => {this.hideName('phoenix')}}>.</a>
            </Reveal>
            <p className={this.state.nameShowing[1]}>Phoenix</p>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
