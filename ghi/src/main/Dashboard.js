import { useState } from 'react';
import { useEffect } from 'react';

const Dashboard = () => {
  const [person_id, setPerson] = useState("0");
  const [events_by_person, setEventsByPerson] = useState([]);
  const [people, setPeople] = useState([]);
  const [events, setEvents] = useState([]);

  const handlePersonData = async (e) => {
    setPerson(e.target.value);
  };

  const handleEditPerson = async (e) => {
    e.preventDefault();
  };

  const handleDeletePerson = async (e) => {
    e.preventDefault();
  };

  useEffect(() => {
    const fetchData = async (endpoint, setState) => {
      let url = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST + endpoint;
      const response = await fetch(url, {
        credentials: 'include'
      });
      if (response.ok) {
        const fetchedData = await response.json();
        setState(fetchedData);
      }
    };
    fetchData('/api/people', setPeople);
    fetchData('/api/events', setEvents);
  }, []);

  useEffect(() => {
    setEventsByPerson(events.filter(singleEvent => singleEvent.person.id.toString() === person_id));
  }, [person_id, events]);


  return (
    <div className="container mt-2 shadow p-4 mt-4">
      <div className="row">
        <div className="col">
          <select
            onChange={handlePersonData}
            value={person_id}
            className="form-select"
            required
            id="person_id"
            name="person_id"
          >
            <option value="0">Choose a person</option>
            {people.map(person => {
              return (
                <option key={person.id} value={person.id}>
                  {`${person.name}`}
                </option>
              );
            })}
          </select>
        </div>

        <div className="col-auto">
          <button
            className="btn btn-primary"
            onClick={handleEditPerson}
            style={{ marginRight: '1em' }}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={handleDeletePerson}
          >
            Delete
          </button>
        </div>
      </div>

      <hr />

      <div className="row">
        <h3>Upcoming events</h3>
        <div className="offset-1 col-10">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Event</th>
                <th>Date</th>
                <th>Occasion</th>
              </tr>
            </thead>
            <tbody>
              {events_by_person?.map(event => {
                return (
                  <tr key={event.id}>
                    <td>{event.name}</td>
                    <td>{event.date}</td>
                    <td>{event.occasion.name}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      <hr />

      {/* TODO: Add Cards */}

    </div>
  );
};

export default Dashboard;
