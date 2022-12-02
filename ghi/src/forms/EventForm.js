import React, { useEffect, useState } from 'react';

function EventForm() {
  const [name, setName] = useState('');
  const [date, setDate] = useState('');
  const [person_id, setPerson] = useState('');
  const [persons, setPersons] = useState([]);
  const [occasion_id, setOccasion] = useState('');
  const [occasions, setOccasions] = useState([]);

  useEffect(() => {
    const getEventData = async () => {
      const eventResponse = await fetch(
        "http://localhost:8000/api/people/",
        { credentials: 'include' });
      const eventData = await eventResponse.json();
      setPersons(eventData);
    };
    getEventData();
  }, []);

  useEffect(() => {
    const getData = async () => {
      const eventResponse = await fetch(
        "http://localhost:8000/api/occasions/",
        { credentials: 'include' });
      const eventData = await eventResponse.json();
      setOccasions(eventData);
    };
    getData();
  }, []);


  const handleSubmit = async event => {
    window.location.replace("http://localhost:3000/calendar");
    event.preventDefault();
    const data = { name, date, person_id, occasion_id };
    const eventUrl = 'http://localhost:8000/api/events/'
    const fetchConfig = {
      method: "post", body: JSON.stringify(data),
      headers: { 'Content-Type': 'application/json' }, credentials: 'include',
    };
    const response = await fetch(eventUrl, fetchConfig);
    if (response.ok) {
      setName(''); setDate(''); setPerson(''); setOccasion('');
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

  if (persons.length>0) {
  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Add a new event!</h1>
          <form onSubmit={handleSubmit} id="create-event-form">
            <div className="form-floating mb-3">
              <input onChange={handleNameChange} value={name} placeholder="Name" required type="text" name="name" id="name" className="form-control" />
              <label htmlFor="name">Name of event</label>
            </div>
            <div className="form-floating mb-3">
              <input onChange={handleDateChange} value={date} placeholder="Date" required type="date" name="date" id="date" className="form-control" />
              <label htmlFor="date">Date of event</label>
            </div>
            <div className="form-floating mb-3">
              <select onChange={handlePersonChange} value={person_id} required name="person_id" id="person_id" className="form-select" >
                <option value="person_id">Person</option>
                {persons?.map((events) => {
                  return (
                      <option key={events.id} value={events.id}>{events.name}</option>
                  );
                })}
              </select>
            </div>
            <div className="form-floating mb-3">
              <select onChange={handleOccasionChange} value={occasion_id} required name="occasion_id" id="occasion_id" className="form-select" >
                <option value="occasion_id">Occasion</option>
                {occasions?.map((events) => {
                  return (
                    <option key={events.id} value={events.id}>{events.name}</option>
                  );
                })}
              </select>
            </div>
            <button className="btn btn-primary">Add!</button>
          </form>
        </div>
      </div>
    </div>

);
}
  else {
    return (
      <div className="row text-center">
        <div className="container mt-2 shadow p-4 mt-4">
        <h3>No people found</h3>
        <div className="col d-flex justify-content-center">
          <td><button className="btn btn-primary"><a href = {"/create_person/"} class="text-decoration-none"><font color="white">Add a new person</font></a></button></td>
          </div>
        </div>
      </div>
    );
  }}

export default EventForm;
