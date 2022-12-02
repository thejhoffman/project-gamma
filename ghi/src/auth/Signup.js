import { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useGetTokenQuery, useCreateAccountMutation } from "../store/tokenApi";
import { useEffect } from 'react';

function BootstrapInput(props) {
    const { id, placeholder, labelText, value, onChange, type } = props;

    return (
        <div className="offset-3 col-6">
            <label htmlFor={id} className="form-label">{labelText}</label>
            <input value={value} onChange={onChange} required type={type} className="form-control" id={id} placeholder={placeholder} />
        </div>
    );
}

function SignUp(props) {
    const [email, setEmail] = useState('');
    const [name, setName] = useState('');
    const [password, setPassword] = useState('');
    const [createAccount, result] = useCreateAccountMutation();
    const { data: tokenData } = useGetTokenQuery();
    const navigate = useNavigate();
    const [trigger, setTrigger] = useState(false)

    const handleSubmit = async e => {
        e.preventDefault();
        createAccount({ email, name, password });
    };


    useEffect(() => {
        if (result.isSuccess && tokenData !== null) {
            navigate("/dashboard");
        }
        else if (result.isError) {
            setTrigger(true)
        }
    }, [navigate, result, tokenData]);

    let alertMessage = "alert alert-danger d-none"
    if (trigger) {
        alertMessage = "alert alert-danger"
    }

    return (
        <>
            <div className={alertMessage} role="alert" align="center">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" className="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z" />
                </svg>
                Unable to create an account, please try again
            </div>

            <form>
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
                <button
                    disabled={password.length === 0}
                    onClick={handleSubmit}
                    className="btn btn-primary offset-3 col-6">Submit</button>
            </form>
        </>
    );
}

export default SignUp;
