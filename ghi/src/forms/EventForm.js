import React, { useEffect, useState } from 'react';

function EventForm() {
  const [name, setName] = useState('');
  const [date, setDate] = useState('');
  const[person_id, setPerson] = useState('');
  const[persons, setPersons] = useState([]);
  const[occasion_id, setOccasion] = useState('');

  useEffect(() => {
      const getEventData = async () => {
          const eventResponse = await fetch(
              "http://localhost:8000/api/people/"
              , {credentials: 'include'});
              const eventData = await eventResponse.json();
              setPersons(eventData.persons);
          };
          getEventData(); }, []);

const handleSubmit = async event => {
  event.preventDefault();
  const data = {name, date, person_id, occasion_id};
  const eventUrl = 'http://localhost:8000/api/events/new/'
  const fetchConfig = {
      method:"post", body:JSON.stringify(data), headers:{'Content-Type':'application/json'},
  };
  const response = await fetch(eventUrl, fetchConfig);
  if(response.ok){setName(''); setDate(''); setPerson(''); setOccasion('');
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

return (
  <div className="row">
    <div className="offset-3 col-6">
      <div className="shadow p-4 mt-4">
        <h1>Add a new event</h1>
        <form onSubmit={handleSubmit} id="create-event-form">
          <div className="form-floating mb-3">
            <input onChange={handleNameChange} value={name} placeholder="Name" required type="text" name="name" id="name" className="form-control" />
            <label htmlFor="name">Name</label>
          </div>
          <div className="form-floating mb-3">
            <input onChange={handleDateChange} value={date} placeholder="Date" required type="text" name="date" id="date" className="form-control" />
            <label htmlFor="date">Date</label>
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
            <input onChange={handleOccasionChange} value={occasion_id} placeholder="occasion_id" required type="text" name="occasion_id" id="occasion_id" className="form-control" />
            <label htmlFor="occasion_id">Occasion</label>
          </div>
          <div className="form-floating mb-3">
            </div>
          <button className="btn btn-primary">Add</button>
        </form>
      </div>
    </div>
  </div>
);
}

export default EventForm;
