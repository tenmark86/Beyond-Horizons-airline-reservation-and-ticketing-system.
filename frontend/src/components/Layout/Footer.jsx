import React from "react";
import "./footer.css";
import footer from "../../images/Footer.png";
import fb from "../../images/facebook.png";
import twitter from "../../images/twitter.png";
import linkedIn from "../../images/linkedin.png";

const Footer = () => {
  return (
    <div className="footer-box">
      <div className="footer-dev">
        <div className="image-container">
          <img src={footer} alt="footer" />
          <span className="contact">Contact</span>
          <span className="aboutus">About Us</span>
          <div className="icon">
            <a href="https://x.com/Mark_mutuota">
              <img className="X" alt="Vector" loading="lazy" src={twitter} />
            </a>
            <a href="https://www.linkedin.com/school/university-of-moratuwa/">
              <img className="linked-in" alt="Vector" loading="lazy" src={linkedIn} />
            </a>
            <a href="https://www.facebook.com/">
              <img className="fb" alt="Vector" loading="lazy" src={fb} />
            </a>
          </div>
          <a className="uom" href="https://uom.lk/">
            <span>Beyond Horizons Airlines 2024</span>
          </a>
        </div>
      </div>
    </div>
  );
};

export default Footer;