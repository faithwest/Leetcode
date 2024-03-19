import React from 'react';
import project1Image from '../images/project1.jpg';
import project2Image from '../images/project2.jpg';
import project3Image from '../images/project3.jpg';
import '../styles/projects.css';

const Projects = () => {
  return (
    <section id="projects">
      <h2>Projects</h2>
      <div className="project">
        <img src={project1Image} alt="Project 1" />
        <h3>Project 1</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl id aliquam tincidunt, nunc nunc tincidunt nunc, id tincidunt nunc nunc id nunc.</p>
      </div>
      <div className="project">
        <img src={project2Image} alt="Project 2" />
        <h3>Project 2</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl id aliquam tincidunt, nunc nunc tincidunt nunc, id tincidunt nunc nunc id nunc.</p>
      </div>
      <div className="project">
        <img src={project3Image} alt="Project 3" />
        <h3>Project 3</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam auctor, nisl id aliquam tincidunt, nunc nunc tincidunt nunc, id tincidunt nunc nunc id nunc.</p>
      </div>
    </section>
  );
};

export default Projects;
