import React, { Component } from 'react';
import './index.css';
import '../data/animate.css';
import '../data/commons.css';
import curitiba750 from './curitiba750.png';
import curitiba751 from './curitiba751.png';
import curitiba752 from './curitiba752.png';
import curitiba754 from './curitiba754.png';
import curitiba755 from './curitiba755.png';
import curitiba900 from './curitiba900.png';
import curitiba901 from './curitiba901.png';
import curitiba902 from './curitiba902.png';
import curitiba000 from './curitiba000.png';
import curitiba001 from './curitiba001.png';
import curSprawl14 from './curitiba14.png';
import leftArrow from './leftArrow.png';
import rightArrow from './rightArrow.png';

class BaseSlides extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currFrame: 1,
      maxFrame: this.props.maps.length
    }
  }

  incrementFrame = () => {
    let newCurrFrame = this.state.currFrame + 1;
    this.setState({
      currFrame: newCurrFrame
    })
  }

  decrementFrame = () => {
    let newCurrFrame = this.state.currFrame - 1;
    this.setState({
      currFrame: newCurrFrame
    })
  }

  render() {
    return (
    <div className='BaseSlide'>
      <div className='Left-div'>
        <div className='Slide-year-div'>
          <h className='Slide-year'>{this.props.years[this.state.currFrame - 1]}</h>
        </div>
        <div className='Frame-navigator-div'>
          <img
            src={leftArrow}
            className={this.state.currFrame > 1 ?
                              'Navigator-arrow' :
                              'Navigator-arrow-unclickable'}
            alt='leftArrow'
            onClick={this.state.currFrame > 1 ?
                          this.decrementFrame :
                          () => {} }
          />
          <span
          className='Frame-number'>{
            this.state.currFrame}/{this.state.maxFrame
          }</span>
          <img
            src={rightArrow}
            className={this.state.currFrame < this.state.maxFrame ?
                                                'Navigator-arrow' :
                                                'Navigator-arrow-unclickable'}
            alt='rightArrow'
            onClick={this.state.currFrame < this.state.maxFrame ?
                          this.incrementFrame :
                          () => {} }
          />
        </div>
      </div>
      <div className='Center-div'>
        <img
          className='Map-class'
          style={{
            width: 'auto',
            height: '100%'
          }}
          alt='map'
          src={this.props.maps[this.state.currFrame - 1]}/>
      </div>
      <div className='Right-div'>
        <p className='Blurb-title'>{this.props.titles[this.state.currFrame - 1]}</p>
        <p className='Blurb-text'>{this.props.blurbs[this.state.currFrame - 1]}</p>
      </div>
    </div>
    )
  }
}

class Slides1975 extends Component {
  render() {
    return (
      <BaseSlides years={[1975, 1975, 1975, 1975, 1975, 1978, 1980]}
                  maps={[curitiba750, curitiba751, curitiba752, curitiba751, curitiba754, curitiba755, curitiba751]}
                  titles={['',
                           'Wilhelm\' Master Plan',
                           'The Industrial City',
                           'BRT Corridor',
                           'Vila Pinto',
                           'Plan for Integrated Development',
                           'Integrated Transport Network']}
                  blurbs={['',
                           'By 1975, the Wilhelm Master Plan of 1966 was in the process of steady implementation, replacing the Agache Master Plan of 1944. The Wilhelm Plan split the city up into five radiating axes of urban development. Although the plan introduced vital planning concepts that would help the city thrive economically, it also contained seeds of inequality which would plague the city’s housing sector. Among the newly-created urban planning department’s projects in the 1970s was Rua Quinze do Novembro, the heart of commercial Curitiba and Brazil\'s first pedestrian-only street. The city also adopted a trinary road design, called the Sistema Trinário, to minimize traffic in the city, whose population had now surpassed 600,000. The new system sandwiched a central two-lane street restricted to buses and local car traffic between wide, fast-moving one-way streets. Curitiba also began developing an industrial zone on the city\'s outskirts, which they called Industrial City.',
                           'Although the new plan called for 5 radial axes of development, the 5th axis remained undeveloped through the 70s. Connector 5 was originally meant to be developed for housing for working class residents who labored in the nearby Industrial City; however, it was never developed as intended, because a group of wealthy business people bought up most of the land and allowed property values to rise. Although the city government also purchased some parcels of land along the transit corridor and used them to subsidize housing costs, they were unable to offset the effects of far more powerful private interests.',
                           'Designed in 1972 and built in 1973, the first 20 km opened of the city’s famous bus rapid transit system were up and running by 1975.',
                           'The Capanema Housing Communities, formed in Prado Velho in 1950, are revitalized in the 70s, and the remaining informal housing and huts take on the new name “Vila Pinto.” This unincorporated settlement is one of the oldest and most embedded communities in the city of Curitiba.',
                           'Following the explosion in immigration begins in late 70s and the arrival of more Black and indigenous Northern Brazilians, the peripheries of the city expand with the low income newcomers who could not afford housing in the city’s core. As a result, the poorest citizens were concentrated outside the city, and cut off from the city’s transit oriented development. In order to address these issues, government officials implemented the Plan for Integrated Development in 1978, which emphasized connecting Curitiba with the surrounding 14 municipalities. These trends of immigration would continue: from 1980, the population of Black and mixed race residents in Curitiba would increase by 250% from 1980 to 2010.',
                           '1980']} />
    )
  }
}

class Slides1990 extends Component {
  render() {
    return (
      <BaseSlides years={[1990, 1990, 1996]}
                  maps={[curitiba900, curitiba901, curitiba902]}
                  titles={['',
                           'Formation of gated Edge Cities',
                           'From "Vila Pinto" to "Vila Torres"']}
                  blurbs={['',
                           'By the 1990s, gated edge-cities have emerged in areas like that along Connectora 5 after speculation about land in close proximity to transit-oriented development drove up land value, which developers cashed in on when they began construction of Ecoville, AlphaVilles, Suı´te Vollard. These wealthy communities city’s perimeter are characterized by a “‘localization’ of a global modern design tradition devoid of the original modern social agenda; or worse still, with an ‘inverted’ social agenda” (Irazabal). By 1992, for example, the Ecoville area housed 406 businesses and employed one fifth of the city’s workers, though many of them would live outside of Curitiba’s municipal boundaries, unlike in contrast with the master plan’s vision.',
                           'In 1996, the residents organized a popular referendum and renamed the town: "Vila Torres", thus becoming a community.'
                           ]} />
    )
  }
}

class Slides2000 extends Component {
  render() {
    return (
      <BaseSlides years={[2000, 2003, 2004]}
                  maps={[curitiba000, curitiba001, curitiba001]}
                  titles={['',
                           'BRT Network',
                           '2004 Master Plan']}
                  blurbs={['',
                           'By 2003, the fleet size of Curitiba’s BRT grew to 2,200 buses. The network consisted of 21 terminals (Terminais), where passengers could transfer between routes, and 351 of the distinctive "tube" stations (Estações-Tubo) that provide high-platform boarding.',
                           '']} />
    )
  }
}

class Slides2014 extends Component {
  render() {
    return (
      <BaseSlides years={[2014]}
                  maps={[curSprawl14]}
                  titles={['']}
                  blurbs={['']} />
    )
  }
}
export { Slides1975, Slides1990, Slides2000, Slides2014 }
