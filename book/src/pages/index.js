import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">
          Bridging Digital Intelligence and the Physical World through Embodied AI Systems
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/module1/module1/overview">
            Start Learning Physical AI & Humanoid Robotics
          </Link>
        </div>
      </div>
    </header>
  );
}

// Styled Textbook Overview
function TextbookOverview() {
  return (
    <section className={styles.textbookOverview}>
      <div className="container">
        <h2>About This Textbook</h2>
        <p>
          This textbook provides a comprehensive introduction to Physical AI and Humanoid Robotics.
          Explore embodied intelligence, AI systems in physical environments, and hands-on modules.
        </p>
        <div className={styles.features}>
          <div className={styles.featureCard}>
            <h3>Hands-On Labs</h3>
            <p>Experiment with real AI-driven robots and learn by doing.</p>
          </div>
          <div className={styles.featureCard}>
            <h3>Core AI Concepts</h3>
            <p>Understand ROS2, sensors, actuators, and intelligent agents.</p>
          </div>
          <div className={styles.featureCard}>
            <h3>Project-Based Learning</h3>
            <p>Build full projects to apply theory into practice.</p>
          </div>
          <div className={styles.featureCard}>
            <h3>AI Simulation Tools</h3>
            <p>Practice robotics in virtual environments before moving to real-world robots.</p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Physical AI & Humanoid Robotics: AI Systems in the Physical World, Embodied Intelligence">
      <HomepageHeader />
      <TextbookOverview />
      
    </Layout>
  );
}
