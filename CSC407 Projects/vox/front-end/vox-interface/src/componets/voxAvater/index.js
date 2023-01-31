import React from "react";
import './style.css'
import './../../styles/gobal.css'

function voxavater() {
    return (
      <div className="vox-avater-container">
       <img src={require('./../../assets/vox-avatar-2.gif')} alt="Animated Gif" />
      </div>
    );
  }
  
  export default voxavater;