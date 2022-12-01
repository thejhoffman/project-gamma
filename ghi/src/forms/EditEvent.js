import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const baseURL = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST;

const EditEvent = () => {
  const {event_id} = useParams();
  const [event_detail, setEventDetail] = useState({});
  const [formData, setEventFormData] = useState({
    name:'',
    date:'',
    person_id:'',
    occasion_id:'',
  });
  const [name, setName]=useState('');
  const [date, setDate]=useState('');
  const [persons, setPersons] = useState([]);
  const [occasions, setOccasions] = useState([]);

  const fetchData = async (endpoint, setState) => {
    let eventUrl = baseURL + endpoint;
    const eventresponse= await fetch(eventUrl,{credentials:'include'});
    if (eventresponse.ok){
      const fetchedData=await eventresponse.json();
      setState(fetchedData);
    }
  };

  useEffect(()=>{
    fetchData('/api/people',setPersons);
    fetchData('/api/occasions',setOccasions);
  },[]);

  useEffect(() => {
    fetchData(`/api/events/${event_id}`, setEventDetail);
  },[event_id]);

  useEffect(()=>{
    if (Object.keys(event_detail).length>0){
      setEventFormData(prev=>{
        return{
          ...prev,
          name:event_detail.name,
          date:event_detail.date,
          person_id:event_detail.person.id,
          occasion_id:event_detail.occasion.id
        };
      });
    }
  }, [event_detail]);

  const handleEventFormData = event => {
    setEventFormData(prev=>({...prev, [event.target.name]: event.target.value}));
  }

  const handleSubmit = async event => {
    window.location.replace("http://localhost:3000/calendar");
    event.preventDefault();
    const fetchConfig = {
      method: "put", body: JSON.stringify(formData),
      headers: { 'Content-Type': 'application/json' }, credentials: 'include',
    };
    const response = await fetch(baseURL+`/api/events/${event_id}`, fetchConfig);
    if (response.ok) {
      setName(''); setDate(''); setPersons(''); setOccasions('');
    }
  };

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Edit an event!</h1>
          <form onSubmit={handleSubmit} id="edit-event-form">
            <div className="form-floating mb-3">
              <input onChange={handleEventFormData} defaultValue={formData.name} placeholder="Name" required type="text" name="name" id="name" className="form-control" />
              <label htmlFor="name">Name of event</label>
            </div>
            <div className="form-floating mb-3">
              <input onChange={handleEventFormData} defaultValue={formData.date} placeholder="Date" required type="date" name="date" id="date" className="form-control" />
              <label htmlFor="date">Date of event</label>
            </div>
            <div className="form-floating mb-3">
              <select onChange={handleEventFormData} value={formData.person_id} required name="person_id" id="person_id" className="form-select" >
                <option value="person_id">Person</option>
                {persons?.map((events) => {
                  return (
                      <option key={events.id} value={events.id}>{events.name}</option>
                  );
                })}
              </select>
            </div>
            <div className="form-floating mb-3">
              <select onChange={handleEventFormData} value={formData.occasion_id} required name="occasion_id" id="occasion_id" className="form-select" >
                <option value="occasion_id">Occasion</option>
                {occasions?.map((events) => {
                  return (
                    <option key={events.id} value={events.id}>{events.name}</option>
                  );
                })}
              </select>
            </div>
            <button className="btn btn-primary" type="submit">Complete Edit!</button>
          </form>
        </div>
      </div>
    </div>

);
};

export default EditEvent;
