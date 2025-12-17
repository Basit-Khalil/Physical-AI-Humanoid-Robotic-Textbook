import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Module 1: The Robotic Nervous System (ROS 2)',
      link: { type: 'doc', id: 'module1/module1-overview' }
,
      items: [
        {
          type: 'category',
          label: 'Week 1: Introduction to Physical AI and Embodied Intelligence',
          items: ['module1/week1/module1-week1-chapter1', 'module1/week1/module1-week1-chapter2', 'module1/week1/module1-week1-new-concept'],
        },
        {
          type: 'category',
          label: 'Week 2: ROS 2 Fundamentals',
          items: ['module1/week2/module1-week2-chapter3', 'module1/week2/module1-week2-chapter4'],
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 2: The Digital Twin (Gazebo & Unity)',
      link: {type: 'doc', id: 'module2/module2-overview'},
      items: [
        {
          type: 'category',
          label: 'Week 3: Physics Simulation Fundamentals',
          items: ['module2/week3/module2-week3-chapter5', 'module2/week3/module2-week3-chapter6'],
        },
        {
          type: 'category',
          label: 'Week 4: Advanced Simulation and Sensor Integration',
          items: ['module2/week4/module2-week4-chapter7', 'module2/week4/module2-week4-chapter8'],
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac)',
      link: {type: 'doc', id: 'module3/module3-overview'},
      items: [
        {
          type: 'category',
          label: 'Week 5: NVIDIA Isaac and Hardware Acceleration',
          items: ['module3/week5/module3-week5-chapter9', 'module3/week5/module3-week5-chapter10'],
        },
        {
          type: 'category',
          label: 'Week 6: Advanced Locomotion and Control',
          items: ['module3/week6/module3-week6-chapter11', 'module3/week6/module3-week6-chapter12'],
        },
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      link: {type: 'doc', id: 'module4/module4-overview'},
      items: [
        {
          type: 'category',
          label: 'Week 7: Voice and Cognitive Interfaces',
          items: ['module4/week7/module4-week7-chapter13', 'module4/week7/module4-week7-chapter14'],
        },
        {
          type: 'category',
          label: 'Week 8: Capstone Project - Autonomous Humanoid Tasks',
          items: ['module4/week8/module4-week8-chapter15', 'module4/week8/module4-week8-chapter16'],
        },
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
