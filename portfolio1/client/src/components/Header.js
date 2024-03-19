import React from 'react';
import '../styles/header.css';

const Header = () => {
  return (
    <header>
      <nav>
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#skills">Skills</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
      <h1>Software Developer Portfolio</h1>
    </header>
  );
};

export default Header;
