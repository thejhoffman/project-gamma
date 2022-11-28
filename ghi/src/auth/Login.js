import { useState } from 'react';

function BootstrapInput(props) {
    const { id, placeholder, labelText, value, onChange, type } = props;

    return (
        <div className="mb-3">
            <label htmlFor={id} className="form-label">{labelText}</label>
            <input value={value} onChange={onChange} required type={type} className="form-control" id={id} placeholder={placeholder} />
        </div>
    );
}

function Login(props) {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    return (

        <form>
            <BootstrapInput
                id="email"
                placeholder="you@example.com"
                labelText="Login with email address"
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
            <button className="btn btn-primary">Submit</button>
        </form>
    );
}

export default Login;
