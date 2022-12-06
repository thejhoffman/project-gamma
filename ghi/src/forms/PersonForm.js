import { useState } from 'react';
import { useEffect } from 'react';
import { useGetTokenQuery } from '../store/tokenApi';
import { useNavigate } from 'react-router-dom';

const baseURL = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST;

function PersonForm() {
  const { data: token, isLoading: tokenLoading } = useGetTokenQuery();
  const [genders, setGenders] = useState([]);
  const [ages, setAges] = useState([]);
  const [relationships, setRelationships] = useState([]);
  const [interests, setInterests] = useState([]);
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: '',
    gender_id: '',
    age_range_id: '',
    relationship_id: '',
    interest_id: '',
  });

  const resetForm = () => {
    setFormData({ ...formData, name: '', gender_id: '', age_range_id: '', relationship_id: '', interest_id: '' });
  };

  useEffect(() => {
    async function getData(url, setFunction) {
      url = baseURL + `/${url}`;
      const response = await fetch(url, { credentials: 'include' });
      if (response.ok) {
        const data = await response.json();
        setFunction(data);
      }
    }

    getData(`gender`, setGenders);
    getData(`api/age_range`, setAges);
    getData(`api/relationships`, setRelationships);
    getData(`api/interests`, setInterests);
  }, []);

  const handleSubmit = e => {
    e.preventDefault();
    navigate('/dashboard');

    const data = { ...formData };
    const requestOptions = {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token.access_token}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    };
    fetch(baseURL + `/api/people`, requestOptions).then(response => response.json());
    resetForm();
  };

  return (
    <div className="container offset-3 col-6">
      <div className="shadow p-4 mt-4">
        <h1>Add a new person</h1>
        {tokenLoading ? "please wait" :
          <form>
            <div className="container">
              <div className="mb-3">
                <label htmlFor="name" className="form-label">Name</label>
                <input value={formData.name} onChange={(e) => setFormData({ ...formData, name: e.target.value })} required type="text" className="form-control" id="name"></input>
              </div>
              <div className="mb-3">
                <label htmlFor="gender" className="form-label">Gender</label>
                <select onChange={(e) => setFormData({ ...formData, gender_id: e.target.value })} value={formData.gender_id} id="gender" className="form-select" aria-label="Gender">
                  <option value="">Select gender</option>
                  {genders.map(gender => <option key={gender.id} value={gender.id}>{gender.name}</option>)}
                </select>
              </div>
              <div className="mb-3">
                <label htmlFor="age" className="form-label">Age</label>
                <select onChange={(e) => setFormData({ ...formData, age_range_id: e.target.value })} value={formData.age_range_id} id="age" className="form-select" aria-label="Age" required>
                  <option value="">Select age</option>
                  {ages.map(age => <option key={age.id} value={age.id}>{age.age}</option>)}
                </select>
              </div>
              <div className="mb-3">
                <label htmlFor="relationship" className="form-label">Relationship</label>
                <select onChange={(e) => setFormData({ ...formData, relationship_id: e.target.value })} value={formData.relationship_id} id="relationship" className="form-select" aria-label="Relationship" required>
                  <option value="">Select relationship</option>
                  {relationships.map(relationship => <option key={relationship.id} value={relationship.id}>{relationship.type}</option>)}
                </select>
              </div>
              <div className="mb-3">
                <label htmlFor="interest" className="form-label">Interest</label>
                <select onChange={(e) => setFormData({ ...formData, interest_id: e.target.value })} value={formData.interest_id} id="interest" className="form-select" aria-label="Interest" required>
                  <option value="">Select an interest</option>
                  {interests.map(interest => <option key={interest.id} value={interest.id}>{interest.name}</option>)}
                </select>
              </div>
              <button disabled={Object.values(formData).includes('')} onClick={handleSubmit} type="submit" className="btn btn-primary">Submit</button>
            </div>
          </form>
        }
      </div>
    </div>
  );
}

export default PersonForm;
