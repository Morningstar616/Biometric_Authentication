import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import './App.css';
import Login from './Login';
import Start from './Start';

function LandingPageContent() {
  return (
    <div className="landing-content">
      <h1>Secure Farming, Smart Living.</h1>
      <p>Empower your farm with our state-of-the-art Biometric Security Application. Experience seamless integration, real-time monitoring, and robust protection for a smarter and more secure agricultural future.</p>
      <div className="padlock-container">
        <Padlock />
      </div>
    </div>
  );
}

function Padlock() {
  return (
    <div className="padlock">
      <div className="shackle"></div>
      <div className="body">
        <div className="upper"></div>
        <div className="lower"></div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="landing-page">
        <Routes>
          <Route
            path="/"
            element={
              <>
                <LandingPageContent />
                <div className="action-buttons">
                  <NavLink to="/Start" className="get-started-button">
                    Get Started
                  </NavLink>
                  <NavLink to="/Login" className="login-button">
                    Login
                  </NavLink>
                </div>
              </>
            }
          />
          <Route path="/Start" element={<Start />} />
          <Route path="/Login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
