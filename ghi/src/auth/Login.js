import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useLoginAccountMutation } from "../store/tokenApi";
import ErrorMessage from '../utils/ErrorMessage';

function BootstrapInput(props) {
  const { id, placeholder, labelText, value, onChange, type } = props;

  return (
    <div className="mb-3">
      <label htmlFor={id} className="form-label">{labelText}</label>
      <input value={value} onChange={onChange} required type={type} className="form-control" id={id} placeholder={placeholder} />
    </div>
  );
};

function Login(props) {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loginAccount, result] = useLoginAccountMutation();
  const [alert, setAlert] = useState({
    isShown: false,
    message: ""
  });

  const handleLogin = async (e) => {
    e.preventDefault();
    const details = {
      'username': email,
      'password': password
    };
    const formBody = Object.keys(details).map(
      key => encodeURIComponent(key) + '=' + encodeURIComponent(details[key])
    ).join('&');
    loginAccount(formBody);
  };

  useEffect(() => {
    if (result.isSuccess) {
      navigate("/");
    }
    else if (result.error) {
      setAlert({ isShown: true, message: result.error.data.detail });
    }
  }, [navigate, result]);

  return (
    <div className="container mt-2">
      <div className='offset-3 col-6'>
        <div className="box shadow p-4 mt-4">
          <h1>Login</h1>
          <form onSubmit={handleLogin}>
            <BootstrapInput
              id="email"
              placeholder="you@example.com"
              labelText="Email Login"
              value={email}
              onChange={e => setEmail(e.target.value)}
              type="email" />
            <BootstrapInput
              id="password"
              placeholder="Password"
              labelText="Password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              type="password" />
            <ErrorMessage isShown={alert.isShown} message={alert.message} />
            <div className="form-floating mb-3">
              <button
                disabled={password.length === 0}
                className="btn btn-primary offset-3 col-6">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
