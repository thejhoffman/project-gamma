import { NavLink, useNavigate } from "react-router-dom";
import logo from './logo.png';
import { useGetTokenQuery, useLogoutAccountMutation } from "../store/tokenApi";
import { useEffect } from "react";

const DropDown = (props) => {
  if (props.tokenData !== null) {
    return (
      <div className={props.margin}>
        <ul className="navbar-nav">
          <li className="nav-item">
            <NavLink className="nav-link" to="/dashboard">Dashboard</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/calendar">Calendar</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/create_person">New person</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/create_event">New event</NavLink>
          </li>
        </ul>
      </div>
    );
  }
  return null;
};

const AuthButtons = (props) => {
  const navigate = useNavigate();
  const [logoutAccount, result] = useLogoutAccountMutation();

  const handleLogout = async (e) => {
    e.preventDefault();
    logoutAccount();
  };

  useEffect(() => {
    if (result.isSuccess) {
      navigate("/");
      result.isSuccess = false;
    }
  }, [navigate, result.isSuccess, result]);

  if (props.tokenData !== null) {
    return (
      <div>
        <button className="btn btn-outline-danger" onClick={handleLogout}>
          Logout
        </button>
      </div>
    );
  }
  return (
    <div>
      <NavLink className="btn btn-primary" style={{ marginRight: '1em' }} to="/signup" > Signup</NavLink>
      <NavLink className="btn btn-outline-primary" to="/login">Login</NavLink>
    </div>
  );
};

const Nav = () => {
  const { data: tokenData } = useGetTokenQuery();
  return (
    <nav className="navbar navbar-expand-lg" style={{ backgroundColor: "#e3f2fd" }}>

      <div className="container-fluid">
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
          <svg viewBox="0 0 100 80" width="30" height="30">
            <g color="DodgerBlue" >
              <rect width="100" height="20" rx="10" fill="currentcolor"></rect>
              <rect y="30" width="100" height="20" rx="10" fill="currentcolor"></rect>
              <rect y="60" width="100" height="20" rx="10" fill="currentcolor"></rect>
            </g>
          </svg>
        </button>
        <NavLink className="navbar-brand mb-0 h1" to="/">
          <img src={logo} style={{ marginRight: '1rem' }} width="40" height="40" alt="logo" />
          Largesseance
        </NavLink>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <DropDown tokenData={tokenData} />
        </div>

        <AuthButtons tokenData={tokenData} />
      </div>

      <div className="collapse" id="navbarToggleExternalContent">
        <DropDown tokenData={tokenData} margin="m-4" />
      </div>
    </nav>
  );
};

export default Nav;
