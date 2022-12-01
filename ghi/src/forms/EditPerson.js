import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";

const baseURL = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST;

const FormSelect = (props) => {
  return (
    <div className="mb-3">
      <label
        className="form-label"
        htmlFor={props.field}
      >
        {props.label}
      </label>
      <select
        className="form-select"
        onChange={props.handleData}
        name={props.field}
        value={props.value}
        id={props.field}
      >
        <option value="">{props.selectLabel}</option>
        {props.list.map(item => {
          return (
            <option
              key={item.id}
              value={item.id}
            >
              {item[Object.keys(item)[1]]}
            </option>
          );
        })}
      </select>
    </div>
  );
};

const EditForm = (props) => {
  const { personID } = useParams();
  const [personDetail, setPersonDetail] = useState({});
  const [formData, setFormData] = useState({
    name: '',
    gender_id: 0,
    age_range_id: 0,
    relationship_id: 0,
    interest_id: 0,
  });
  const [genders, setGenders] = useState([]);
  const [ages, setAges] = useState([]);
  const [relationships, setRelationships] = useState([]);
  const [interests, setInterests] = useState([]);

  const fetchData = async (endpoint, setState) => {
    let url = baseURL + endpoint;
    const response = await fetch(url, {
      credentials: 'include'
    });
    if (response.ok) {
      const fetchedData = await response.json();
      setState(fetchedData);
    }
  };

  useEffect(() => {
    fetchData('/gender', setGenders);
    fetchData('/api/age_range', setAges);
    fetchData('/api/relationships', setRelationships);
    fetchData('/api/interests', setInterests);
  }, []);

  useEffect(() => {
    fetchData(`/api/people/${personID}`, setPersonDetail);
  }, [personID]);

  useEffect(() => {
    if (Object.keys(personDetail).length > 0) {
      setFormData(prev => {
        return {
          ...prev,
          name: personDetail.name,
          age_range_id: personDetail.age_range.id,
          gender_id: personDetail.gender.id,
          interest_id: personDetail.interest.id,
          relationship_id: personDetail.relationship.id
        };
      });
    }
  }, [personDetail]);

  const handleFormData = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const fetchConfig = {
      method: "PUT",
      headers: {
        "Content-type": "application/json"
      },
      body: JSON.stringify(formData),
      credentials: 'include'
    };

    const response = await fetch(baseURL + `/api/people/${personID}`, fetchConfig);
    if (response.ok) {
      props.setDidUpdate(response.ok);
    }
  };

  return (
    <>
      <h2>Edit person</h2>

      <form onSubmit={handleSubmit}>
        <div className="container">
          <div className="form-floating mb-3">
            <input
              className="form-control"
              onChange={handleFormData}
              name="name"
              value={formData.name}
              id="name"
              type="text"
              required
            />
            <label htmlFor="name" className="form-label">Name</label>
          </div>

          <FormSelect
            field="gender_id"
            label="Gender"
            handleData={handleFormData}
            value={formData.gender_id}
            list={genders}
            selectLabel="Select a gender"
          />
          <FormSelect
            field="age_range_id"
            label="Age"
            handleData={handleFormData}
            value={formData.age_range_id}
            list={ages}
            selectLabel="Select age"
          />
          <FormSelect
            field="relationship_id"
            label="Relationship"
            handleData={handleFormData}
            value={formData.relationship_id}
            list={relationships}
            selectLabel="Select relationship"
          />
          <FormSelect
            field="interest_id"
            label="Interest"
            handleData={handleFormData}
            value={formData.interest_id}
            list={interests}
            selectLabel="Select an interest"
          />

          <button
            className="btn btn-primary"
            type="submit"
          >
            Submit
          </button>

        </div>
      </form >
    </>
  );
};

const SuccessMessage = () => {
  return (
    <div className="row text-center">
      <h3>Person successfully updated</h3>
      <div className="col d-flex justify-content-center">
        <Link to="/dashboard" className="btn btn-primary">
          Return to dashboard
        </Link>
      </div>
    </div>
  );
};

const EditPerson = () => {
  const [didUpdate, setDidUpdate] = useState(false);
  return (
    <div className="container mt-2 offset-3 col-6">
      <div className="shadow p-4 mt-4">
        {didUpdate
          ? <SuccessMessage />
          : <EditForm setDidUpdate={setDidUpdate} />
        }
      </div>
    </div>
  );
};

export default EditPerson;
