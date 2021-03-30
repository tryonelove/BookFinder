import React from "react";

import GeneralHeader from "./GeneralHeader";
import Footer from "./Footer";

import BigLogo from "../../assets/images/big-logo.svg";
import Pushkin from "../../assets/images/pushkin.jpg";
import Catalog from "../../assets/images/catalog.jpg";
import MyLibrary from "../../assets/images/my-library.jpg";

import "../../styles/main.css";

function Main() {
  return (
    <>
      <GeneralHeader />
      <main>
        <section className="big_logo_wrapper">
          <img src={BigLogo} alt="big logo border" />
          <a href="#navigation">
            <span></span>
          </a>
        </section>
        <section id="navigation" className="alternative_navigation_wrapper">
          <p>
            {" "}
            <span className="logo">Буконика</span>- наука о поглощении книг
          </p>
          <div className="links_wrapper">
            <div className="left_side_link">
              <img src={Pushkin} alt="pushkin" />
              <img className="link" src={Catalog} alt="catalog" />
            </div>
            <div className="right_side_link">
              <img className="link" src={MyLibrary} alt="my library" />
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}

export default Main;
