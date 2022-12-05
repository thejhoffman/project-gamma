import React, { useEffect, useState } from 'react';
import { useGetTokenQuery } from '../store/tokenApi';
import { Link } from "react-router-dom";

const baseURL = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST;

function Calendar() {
  const [events, setEvents] = useState([]);
  useEffect(() => {
    const getEventData = async () => {
      const eventResponse = await fetch(
        baseURL + "/api/events/",
        { credentials: 'include' });
      const eventData = await eventResponse.json();
      setEvents(eventData);
    };
    getEventData();
  }, []);

  const { data: token } = useGetTokenQuery();
  async function handleDelete(id) {
    const eventsUrl = baseURL + `/api/events/${id}`;
    const fetchConfig = {
      method: "delete",
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.access_token}`,
      },
    };
    const eventResponse = await fetch(eventsUrl, fetchConfig);
    if (eventResponse.ok) {
      setEvents(events.filter(event => event.id !== id));
    }
    else {
      throw new Error("Error");
    }
  };

  return (
    <div className="container mt-2 shadow p-4 mt-4">
      <div className="row text-center">
        <h1>Calendar</h1>
        <p> A list of your upcoming events.</p>
        <div className="col d-flex justify-content-center">
          <Link to="/create_event" className="btn btn-primary">Add event</Link>
        </div><table className="table table-striped">
          <thead>
            <tr>
              <th>Event</th>
              <th>Date</th>
              <th>Person</th>
              <th>Occasion</th>
            </tr>
          </thead>
          <tbody>
            {events?.map(event => {
              return (
                <tr key={event.id}>
                  <td>{event.name}</td>
                  <td>{event.date}</td>
                  <td>{event.person.name}</td>
                  <td>{event.occasion.name}</td>
                  <td><Link to={"/edit_event/" + (event.id)} className="btn btn-success">Edit</Link></td>
                  <td><button className="btn btn-danger" onClick={() => handleDelete(event.id)}>Delete</button></td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Calendar;
