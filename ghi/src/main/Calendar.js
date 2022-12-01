import React, { useEffect, useState } from 'react';
import { useGetTokenQuery } from '../store/tokenApi';

function Calendar() {
  const [events, setEvents] = useState([]);
  useEffect(() => {
    const getEventData = async () => {
      const eventResponse = await fetch(
        "http://localhost:8000/api/events/",
        {credentials:'include'});
        const eventData = await eventResponse.json();
        setEvents(eventData);
      };
      getEventData(); }, []);

  const {data:token} = useGetTokenQuery();
  async function handleDelete(id) {
    const eventsUrl = `http://localhost:8000/api/events/${id}`;
    const fetchConfig = {
      method: "delete",
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.access_token}`,
      },
    };
    const eventResponse = await fetch(eventsUrl, fetchConfig);
    if (eventResponse.ok) {
      setEvents(events.filter(event => event.id !== id))
    }
    else {
      throw new Error ("Error");
    }
  };

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
        <h1>Calendar</h1>
        <td><button className="btn btn-success"><a href = {"/create_event/"} class="text-decoration-none"><font color="white">Add event</font></a></button></td>
              <table className="table table-striped">
                  <thead>
                  <tr>
                      <th>Event</th>
                      <th>Date</th>
                      <th>Person</th>
                      <th>Occasion</th>
                  </tr>
                  </thead>
                  <tbody>
                      {events?.map(event=> {
                          return(
                              <tr key={event.id}>
                                  <td>{event.name}</td>
                                  <td>{event.date}</td>
                                  <td>{event.person.name}</td>
                                  <td>{event.occasion.name}</td>
                                  <td><button className="btn btn-primary"><a href = {"/edit_event/"+(event.id)} class="text-decoration-none"><font color="white">Edit</font></a></button></td>
                                  <td><button className="btn btn-danger" onClick={() => handleDelete(event.id)}>Delete</button></td>
                              </tr>
                          );
                      })}
                  </tbody>
              </table>
              </div>
          </div>
      </div>
      );
                  }

export default Calendar;
