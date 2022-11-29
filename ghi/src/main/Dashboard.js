import { useState } from 'react';
import { useEffect } from 'react';

const Dashboard = () => {
  const [formData, setFormData] = useState({
    person_id: ""
  });
  const [people, setPeople] = useState([]);

  const handleFormData = async (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
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
    <div className=" container mt-2">
      <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Select a person</h1>
            <form>
              <div className="mb-3">
                <select
                  onChange={handleFormData}
                  value={formData.person_id}
                  className="form-select"
                  required
                  id="person_id"
                  name="person_id"
                >
                  <option value="">Choose a person</option>
                  {people.map(person => {
                    return (
                      <option key={person.id} value={person.id}>
                        {`${person.name}`}
                      </option>
                    );
                  })}
                </select>
              </div>
              <button className="btn btn-primary">Add</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
