import React, { useState } from 'react';
import './components.css';

const SignUp = () => {
  const handleSignUpClick = async () => {
    await sendSlackNotification();
  };

  const sendSlackNotification = async () => {
    const request = new Request(`api/sign-up/`, {
      method: 'GET',
    });
    try {
      const response = await fetch(request);
      if (!response.ok) {
        throw new Error('Failed to send Slack notification');
      }
    } catch (error) {
      console.log(error.message);
    }
  };

  return (
    <div className="service-container">
      <div className="service">
        <h2 className="service-title">My Cool Service</h2>
        <p className="service-description">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        </p>
        <button className="sign-up-button" onClick={handleSignUpClick}>
          Sign Up
        </button>
      </div>
    </div>
  );
};

export default SignUp;
