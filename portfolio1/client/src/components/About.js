import React from 'react';
import profile from '../images/profile.jpg';
import '../styles/about.css';

const About = () => {
  return (
    <section id="about">
      <div className="about-content">
        <img src={profile} alt="Profile" />
        <h2>About Me</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl id aliquam tincidunt, nunc nunc tincidunt nunc, id tincidunt nunc nunc id nunc. Nullam auctor, nisl id aliquam tincidunt, nunc nunc tincidunt nunc, id tincidunt nunc nunc id nunc.</p>
      </div>
    </section>
  );
};

export default About;
