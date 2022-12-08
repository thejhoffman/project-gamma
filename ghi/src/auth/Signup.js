import { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useGetTokenQuery, useCreateAccountMutation } from "../store/tokenApi";
import { useEffect } from 'react';
import ErrorMessage from '../utils/ErrorMessage';


function BootstrapInput(props) {
  const { id, placeholder, labelText, value, onChange, type } = props;

  return (
    <div className="mb-3">
      <label htmlFor={id} className="form-label">{labelText}</label>
      <input value={value} onChange={onChange} required type={type} className="form-control" id={id} placeholder={placeholder} />
    </div>
  );
}

function SignUp(props) {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [passwordCheck, setPasswordCheck] = useState('');
  const [createAccount, result] = useCreateAccountMutation();
  const { data: tokenData } = useGetTokenQuery();
  const navigate = useNavigate();
  const [alert, setAlert] = useState({
    isShown: false,
    message: ""
  });

  const handleSubmit = async e => {
    e.preventDefault();
    if (password === passwordCheck)
      createAccount({ email, name, password });
    else
      setAlert({ isShown: true, message: "Passwords do not match. Please try again" });
  };

  useEffect(() => {
    if (result.isSuccess && tokenData !== null) {
      navigate("/dashboard");
    }
    else if (result.error) {
      setAlert({ isShown: true, message: result.error.data.detail });
    }
    else if (result.isError) {
      setAlert({ isShown: true, message: "Unable to create account. Please try again" });
    }
  }, [navigate, result, tokenData]);

  return (
    <div className="container mt-2">
      <div className='offset-3 col-6'>
        <div className="box shadow p-4 mt-4">
          <h1>Signup</h1>
          <form onSubmit={handleSubmit}>
            <BootstrapInput
              id="email"
              placeholder="you@example.com"
              labelText="Your email address"
              value={email}
              onChange={e => setEmail(e.target.value)}
              type="email" />
            <BootstrapInput
              id="name"
              placeholder="Your name"
              labelText="Your Name"
              value={name}
              onChange={e => setName(e.target.value)}
              type="text" />
            <BootstrapInput
              id="password"
              placeholder="Create Password"
              labelText="Password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              type="password" />
            <BootstrapInput
              id="passwordCheck"
              placeholder="Retype Password"
              labelText="Confirm Password"
              value={passwordCheck}
              onChange={e => setPasswordCheck(e.target.value)}
              type="password" />
            <ErrorMessage isShown={alert.isShown} message={alert.message} />
            <button
              disabled={password.length === 0}
              className="btn btn-primary offset-3 col-6">Submit</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SignUp;
