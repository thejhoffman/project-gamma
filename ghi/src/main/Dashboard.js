import { useState } from 'react';
import { useEffect } from 'react';

const Dashboard = () => {
  const [person_id, setPerson] = useState();
  const [people, setPeople] = useState([]);

  const handlePersonData = async (e) => {
    setPerson(prev => (e.target.value));
  };

  const handleEditPerson = async (e) => {
    e.preventDefault();
  };

  const handleDeletePerson = async (e) => {
    e.preventDefault();
  };

  useEffect(() => {
    const fetchData = async () => {
      const url = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST + '/api/people';
      const response = await fetch(url, {
        credentials: 'include'
      });
      if (response.ok) {
        const fetchedData = await response.json();
        setPeople(fetchedData);
      }
    };
    fetchData();
  }, []);


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
      </div>

      <hr />


    </div>
  );
};

export default Dashboard;
