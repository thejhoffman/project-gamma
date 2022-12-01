import React, { useEffect, useState } from 'react';
import { useGetTokenQuery } from '../store/tokenApi';
import { Link } from "react-router-dom";

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
  // async function handleUpdate_Event(id) {
  //   const eventsUrl = `http://localhost:8000/api/events/${id}`;
  //   const fetchConfig = {
  //     method: "PUT",
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Authorization': `Bearer ${token.access_token}`,
  //     },
  //   };
  //   const eventResponse = await fetch(eventsUrl, fetchConfig);
  //   if (eventResponse.ok) {
  //     setEvents(events.filter(event => event.id !== id))
  //   }
  //   else {
  //     throw new Error ("Error");
  //   }
  // };

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
        <h1>Calendar</h1>
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
                                  <Link
                                  to={"/EditEvent/" + (event.id)}
                                  className={"btn btn"+((event.id===0))}>
                                  Edit
                                  </Link>
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
