import { BrowserRouter, Routes, Route } from 'react-router-dom';
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
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          {/* Main Routes */}
          <Route path="/" element={<MainPage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/calendar" element={<Calendar />} />
          {/* Auth Routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          {/* Form Routes */}
          <Route path="/create_event" element={<EventForm />} />
          <Route path="/create_person" element={<PersonForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
