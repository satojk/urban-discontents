import React, { Component } from 'react';
import './index.css';
import '../data/animate.css';
import '../data/commons.css';
import InViewMonitor from 'react-inview-monitor';

class BaseSlides extends Component {
  render() {
    return (
    <div className='BaseSlide'>
      <InViewMonitor
        classNameNotInView='vis-hidden'
        classNameInView='animated fadeInUp'
        childPropsInView={{animate: true}}
      >
      <p className='Slide-year'>{this.props.year}</p>
      </InViewMonitor>
      <InViewMonitor
        classNameNotInView='vis-hidden'
        classNameInView='animated fadeInUp'
        childPropsInView={{animate: true}}
      >
      <p className='Main-text'>{this.props.text}</p>
      </InViewMonitor>
    </div>
    )
  }
}

class Slides1975 extends Component {
  render() {
    return (
      <BaseSlides year={1975}
                  text={'This is the first recorded year'} />
    )
  }
}

class Slides1990 extends Component {
  render() {
    return (
      <BaseSlides year={1990}
                  text={'Second year'} />
    )
  }
}

class Slides2000 extends Component {
  render() {
    return (
      <BaseSlides year={2000}
                  text={'2000!!'} />
    )
  }
}

class Slides2014 extends Component {
  render() {
    return (
      <BaseSlides year={2014}
                  text={'Alright, end of the line'} />
    )
  }
}
export { Slides1975, Slides1990, Slides2000, Slides2014 }
