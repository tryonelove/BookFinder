import Heart from "../../assets/images/heart.svg";
import SmallLogo from "../../assets/images/small-logo.svg";

function Footer() {
  return (
    <footer className="footer">
      <p>
        с{" "}
        <span>
          <img src={Heart} />
        </span>{" "}
        к тому, что делаем
      </p>
      <img src={SmallLogo} alt="small logo" />
    </footer>
  );
}
export default Footer;
