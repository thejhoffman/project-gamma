import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Link } from "react-router-dom";

const baseURL = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST;

function EventForm() {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [date, setDate] = useState('');
  const [person_id, setPerson] = useState('');
  const [persons, setPersons] = useState([]);
  const [occasion_id, setOccasion] = useState('');
  const [occasions, setOccasions] = useState([]);

  useEffect(() => {
    const getEventData = async () => {
      const eventResponse = await fetch(
        baseURL + "/api/people/",
        { credentials: 'include' });
      const eventData = await eventResponse.json();
      setPersons(eventData);
    };
    getEventData();
  }, []);

  useEffect(() => {
    const getData = async () => {
      const eventResponse = await fetch(
        baseURL + "/api/occasions/",
        { credentials: 'include' });
      const eventData = await eventResponse.json();
      setOccasions(eventData);
    };
    getData();
  }, []);


  const handleSubmit = async event => {
    event.preventDefault();
    const data = { name, date, person_id, occasion_id };
    const eventUrl = baseURL + '/api/events/';
    const fetchConfig = {
      method: "post", body: JSON.stringify(data),
      headers: { 'Content-Type': 'application/json' }, credentials: 'include',
    };
    const response = await fetch(eventUrl, fetchConfig);
    if (response.ok) {
      navigate("/calendar");
    }
  };
  const handleNameChange = event => {
    setName(event.target.value);
  };
  const handleDateChange = event => {
    setDate(event.target.value);
  };
  const handlePersonChange = event => {
    setPerson(event.target.value);
  };
  const handleOccasionChange = event => {
    setOccasion(event.target.value);
  };

  if (persons.length > 0) {
    return (
      <div className="container offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Add a new event</h1>
          <form onSubmit={handleSubmit} id="create-event-form">
            <div className="mb-3">
            <label className="form-label" htmlFor="name">Name of event</label>
              <input onChange={handleNameChange} value={name} placeholder="Name" required type="text" name="name" id="name" className="form-control" />
            </div>
            <div className="mb-3">
            <label className="form-label" htmlFor="date">Date</label>
              <input onChange={handleDateChange} value={date} placeholder="Date" required type="date" name="date" id="date" className="form-control" />
            </div>
            <div className="mb-3">
              <label className="form-label" htmlFor="person_id">Person</label>
              <select onChange={handlePersonChange} value={person_id} required name="person_id" id="person_id" className="form-select" >
                <option value="person_id">Select person</option>
                {persons?.map((events) => {
                  return (
                    <option key={events.id} value={events.id}>{events.name}</option>
                  );
                })}
              </select>
            </div>
            <div className="mb-3">
              <label className="form-label" htmlFor="occasion_id">Occasion</label>
              <select onChange={handleOccasionChange} value={occasion_id} required name="occasion_id" id="occasion_id" className="form-select" >
                <option value="occasion_id">Select occasion</option>
                {occasions?.map((events) => {
                  return (
                    <option key={events.id} value={events.id}>{events.name}</option>
                  );
                })}
              </select>
            </div>
            <button className="btn btn-primary">Add</button>
          </form>
        </div>
      </div>
    );
  }
  else {
    return (
      <div className="container offset-3 col-6">
        <div className="shadow p-4 mt-4 text-center">
          <h3>No people found</h3>
          <p> A person must be added to create an event.</p>
          <div className="col d-flex justify-content-center">
            <Link to ="/create_person" className="btn btn-primary">
              Create a new person
            </Link>
          </div>
        </div>
      </div >
    );
  }
}

export default EventForm;
