import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Link } from "react-router-dom";

const baseURL = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST;

const DeleteForm = (props) => {
  const { personID } = useParams();
  const [personName, setPersonName] = useState("");
  const [personIsValid, setPersonIsValid] = useState(false);

  useEffect(() => {
    const fetchData = async (endpoint, setState) => {
      let url = baseURL + `/api/people/${personID}`;
      const response = await fetch(url, {
        credentials: 'include'
      });
      if (response.ok) {
        const fetchedData = await response.json();
        setPersonName(fetchedData.name);
        setPersonIsValid(true);
      }
    };

    fetchData();
  }, [personID]);

  const handleDelete = async (e) => {
    e.preventDefault();
    const fetchConfig = {
      method: "DELETE",
      credentials: 'include'
    };

    const response = await fetch(baseURL + `/api/people/${personID}`, fetchConfig);
    if (response.ok) {
      props.setDidDelete(response.ok);
    }
  };

  if (!personIsValid) {
    return (
      <div className="row text-center">
        <h3>Unable to find person</h3>
        <div className="col d-flex justify-content-center">
          <Link to="/dashboard" className="btn btn-primary">
            Return to dashboard
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="row text-center">
      <h4>Are you sure you want to delete this person?</h4>
      <hr />
      <h5>{personName}</h5>
      <div className="col mt-2 d-flex justify-content-center">
        <button
          className="btn btn-danger"
          style={{ marginRight: '1em' }}
          onClick={handleDelete}
        >
          YES
        </button>
        <Link
          className="btn btn-primary"
          to="/dashboard"
        >
          NO
        </Link>
      </div>
    </div>
  );
};

const SuccessMessage = () => {
  return (
    <div className="row text-center">
      <h3>Person successfully deleted</h3>
      <div className="col d-flex justify-content-center">
        <Link to="/dashboard" className="btn btn-primary">
          Return to dashboard
        </Link>
      </div>
    </div>
  );
};

const DeletePerson = () => {
  const [didDelete, setDidDelete] = useState(false);

  return (
    <div className="container mt-2 offset-3 col-6">
      <div className="shadow p-4 mt-4">
        {didDelete
          ? <SuccessMessage />
          : <DeleteForm setDidDelete={setDidDelete} />
        }
      </div>
    </div>
  );
};

export default DeletePerson;
