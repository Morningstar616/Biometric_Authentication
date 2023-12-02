import React from "react";
import './Start.css'

function Start() {
  return (
    <div className="start">
      <h1>Welcome Onboard!</h1>
      <p>Create your account</p>

      <div className="form-container">
        <label htmlFor="firstName">First Name</label>
        <div className="form-group">
          <input type="text" id="firstName" placeholder="Enter First Name" />
        </div>

        <label htmlFor="lastName">Last Name</label>
        <div className="form-group">
          <input type="text" id="lastName" placeholder="Enter Last Name" />
        </div>

        <label htmlFor="dob">Date of Birth</label>
        <div className="form-group">
          <input type="date" id="dob" />
        </div>
      </div>
      <button className="signup-button">Next</button>
    </div>
  );
}

export default Start;