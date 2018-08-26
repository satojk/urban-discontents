import React, { Component } from 'react';
import ProjectHeader from '../data/project-header.js'
import '../data/commons.css';
import '../data/animate.css';
import './index.css';
import Slider, { Range } from 'rc-slider';
import 'rc-slider/assets/index.css';
import { Slides1975,
         Slides1990,
         Slides2000,
         Slides2014
} from './slides'

const SlideDeckController = (props) => {
  const year = props.year;
  switch(year) {
    case 1975:
      return <Slides1975 />

    case 1990:
      return <Slides1990 />

    case 2000:
      return <Slides2000 />

    default:
      return <Slides2014 />
  }
}

class Curitiba extends Component {
  constructor() {
    super();
    this.state = {
      year: 1975
    }
  }

  changeYear = (newYear) => {
    this.setState({
      year: newYear
    })
  }

  render() {
    return (
      <div className="Curitiba">
        <ProjectHeader />
        <div className='Intro-div'>
          <div className='Curitiba-title-div'>
            <span className='Curitiba-title'>Curitiba</span>
          </div>
          <div className='Curitiba-text-div'>
            <span className='Curitiba-text'>Famous as one of the world’s most sustainable and equitable cities, Curitiba possesses a mythology of successful, equitable transportation planning. But outside of Curitiba’s famously well-planned urban infrastructure, vulnerability exists on the fringes of the city’s formal institutions and processes, in the domain of the informal, improvised, and impoverished. What happens between and outside the Curitiba’s renowned corridors of concentrated transit, resources, and institutional attention on a series of arteries extending from its urban core?</span>
          </div>
        </div>
        <Slider
          min={1975}
          max={2014}
          marks={{
            1975: '1975',
            1990: '1990',
            2000: '2000',
            2014: '2014'
          }}
          step={null}
          style={{width: '25%'}}
          onChange={this.changeYear}
          className='Slider'
        />
        <div className='Slide-div'>
          <SlideDeckController year={this.state.year}/>
        </div>
      </div>
    )
  }
}

export default Curitiba;
