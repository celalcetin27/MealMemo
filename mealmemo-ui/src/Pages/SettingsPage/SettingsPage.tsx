import { Navbar } from "../../Components/Navbar/Navbar";
import settingsFood from "./settingsFood.png";
import "./SettingsPage.scss";

export const SettingsPage = () => {
  return (
    <>
      <Navbar />
      <div className="SettingsWrapper">
        <div className="SettingsProfileWrapper">
          <div className="SettingsProfileHeader">PROFILE</div>
          <div>
            <div className="SettingsProfileItemHeader">NAME</div>
            <div className="SettingsProfileItemValue">* USER NAME</div>
          </div>
          <div>
            <div className="SettingsProfileItemHeader">SURNAME</div>
            <div className="SettingsProfileItemValue">* USER SURNAME</div>
          </div>
          <div>
            <div className="SettingsProfileItemHeader">E-MAIL</div>
            <div className="SettingsProfileItemValue">* USER EMAIL</div>
          </div>
          <div>
            <div className="SettingsProfileItemHeader">PASSWORD</div>
            <div className="SettingsProfileItemValue">* USER PASSWORD</div>
          </div>
        </div>
        <img src={settingsFood} alt="food" />
        <div className="SettingsFormWrapper">
          <div className="SettingsFormHeader">WANT TO CHANGE PASSWORD</div>
          <div>
            <div className="SettingsFormItemHeader">CURRENT PASSWORD</div>
            <input />
          </div>
          <div>
            <div className="SettingsFormItemHeader">NEW PASSWORD</div>
            <input />
          </div>
          <div>
            <div className="SettingsFormItemHeader">CONFIRM NEW PASSWORD</div>
            <input />
          </div>
          <button>
            <span className="text">CHANGE</span>
          </button>
        </div>
        <div className="leftOrange" />
      </div>
    </>
  );
};
