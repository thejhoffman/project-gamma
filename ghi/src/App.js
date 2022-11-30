import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PrivateRoutes from './utils/PrivateRoutes';
import Nav from './nav/Nav';
import './App.css';
import MainPage from './main/MainPage';
import Dashboard from './main/Dashboard';
import Calendar from './main/Calendar';
import Login from './auth/Login';
import Signup from './auth/Signup';
import EventForm from './forms/EventForm';
import PersonForm from './forms/PersonForm';

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, '');
  return (
    <BrowserRouter basename={basename}>
      <Nav />
      <div className="container">
        <Routes>
          {/* Home Route */}
          <Route path="/" element={<MainPage />} />
          {/* Auth Routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />

          {/* Restrict access to below routes to only authenticated users */}
          <Route element={<PrivateRoutes />}>
            {/* Main Routes */}
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/calendar" element={<Calendar />} />
            {/* Form Routes */}
            <Route path="/create_event" element={<EventForm />} />
            <Route path="/create_person" element={<PersonForm />} />
          </Route>

        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
