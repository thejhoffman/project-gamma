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

    const handleSubmit = e => {
        e.preventDefault();
        createAccount({ email, name, password });
    };

    useEffect(() => {
        if (result.isSuccess && tokenData !== null) {
            navigate("/dashboard");
        }
    }, [navigate, result.isSuccess, tokenData]);

    return (

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
    );
}

export default SignUp;
