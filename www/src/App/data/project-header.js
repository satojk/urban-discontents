import React, { Component } from 'react';
import logo from './logo_urb.jpg';
import nsf_logo from './nsf_logo.jpg';
import cesta_logo from './cesta_logo.jpg';
import './animate.css';
import './commons.css';

class ProjectHeader extends Component {
  render() {
    return (
      <div className='Home-header-div'>
        <header className='Home-header'>
          <a href='/'><img src={logo} alt='logo' className='Project-logo'/></a>
          <div className='Smaller-logo-div'>
            <a href='https://www.nsf.gov/'><img src={nsf_logo} className='Smaller-logo' alt='nsf_logo'/></a>
            <a href='https://cesta.stanford.edu'><img src={cesta_logo} className='Smaller-logo' alt='cesta_logo'/></a>
          </div>
          <a href='/' className='Header-link'>ABOUT</a>
          <a href='/' className='Header-link'>GEOGRAPHIES OF VULNERABILITY</a>
          <a href='/' className='Header-link'>CITIES</a>
        </header>
      </div>
    )
  }
}

export default ProjectHeader;
