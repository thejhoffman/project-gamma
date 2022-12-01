import { useState } from 'react';
import { useEffect } from 'react';
import { Link } from "react-router-dom";

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

const ProductCard = (props) => {
  return (
    <div className="card mb-4" style={{ width: '18rem' }}>
      <img src="..." className="card-img-top" alt="..." />
      <div className="card-body">
        <h5 className="card-title">Card title</h5>
        <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        <Link to="/" className="btn btn-primary">Go somewhere</Link>
      </div>
    </div >
  );
};

const TableAndCards = (props) => {
  const [eventsByPerson, setEventsByPerson] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchData('/api/events', setEvents);
  }, []);

  useEffect(() => {
    setEventsByPerson(events.filter(singleEvent => singleEvent.person.id.toString() === props.person_id));
  }, [props.person_id, events]);

  if (eventsByPerson.length > 0) {
    return (
      <>
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
                {eventsByPerson.slice(0, 3).map(event => {
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
        <div className="row">
          <div className="col d-flex justify-content-center">
            <ProductCard />
          </div>
          <div className="col d-flex justify-content-center">
            <ProductCard />
          </div>
          <div className="col d-flex justify-content-center">
            <ProductCard />
          </div>
          <div className="col d-flex justify-content-center">
            <ProductCard />
          </div>
        </div>
      </>
    );
  }
  else {
    return (
      <>
        <hr />
        <div className="row text-center">
          <h3>No upcoming events</h3>
          <div className="col d-flex justify-content-center">
            <Link to="/create_event" className="btn btn-primary">
              Create a new event
            </Link>
          </div>
        </div>
      </>
    );
  }
};

const PersonDropdown = (props) => {
  const [people, setPeople] = useState([]);

  useEffect(() => {
    fetchData('/api/people', setPeople);
  }, []);

  if (people.length > 0) {
    return (
      <>
        <div className="row">
          <div className="col">
            <select
              onChange={props.handlePersonData}
              value={props.person_id}
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
            <Link
              to={"/edit_person/" + (props.person_id)}
              className={"btn btn-primary" + ((+props.person_id === 0) ? " disabled" : "")}
              style={{ marginRight: '1em' }}
            >
              Edit
            </Link>
            <Link
              to="/delete_person"
              className={"btn btn-danger" + ((+props.person_id === 0) ? " disabled" : "")}
            >
              Delete
            </Link>
          </div>
        </div>
      </>
    );
  }
  else {
    return (
      <div className="row text-center">
        <h3>No people found</h3>
        <div className="col d-flex justify-content-center">
          <Link to="/create_person" className="btn btn-primary">
            Add a new person
          </Link>
        </div>
      </div>
    );
  }
};


const Dashboard = () => {
  const [person_id, setPerson] = useState("0");

  const handlePersonData = async (e) => {
    setPerson(e.target.value);
  };

  return (
    <div className="container mt-2 shadow p-4 mt-4">
      <PersonDropdown
        person_id={person_id}
        handlePersonData={handlePersonData}
      />

      {+person_id !== 0 &&
        <TableAndCards
          person_id={person_id}
        />
      }
    </div >
  );
};

export default Dashboard;
