import { useState } from 'react';
import { useEffect } from 'react';
import { Link } from "react-router-dom";
import htmlDecode from '../utils/htmlDecode';

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

const CreateRow = (props) => {
  return (
    <div className="row row-cols-2 row-cols-lg-4">
      <div className='col'>
        <ProductCard key={0} product={props.rowList[0]} />
      </div>
      <div className='col'>
        <ProductCard key={1} product={props.rowList[1]} />
      </div>
      <div className='col'>
        <ProductCard key={2} product={props.rowList[2]} />
      </div>
      <div className='col'>
        <ProductCard key={3} product={props.rowList[3]} />
      </div>
    </div>
  );
};

const ProductCard = (props) => {
  if (props.product !== undefined) {
    return (
      <div className="card mb-3 shadow" >
        <img src={props.product.MainImage.url_170x135} className="card-img-top" alt="product" />
        <div className="card-body">
          <div className="card-title">{htmlDecode(props.product.title)}</div>
          <p className="card-subtitle mb-2 text-muted">${props.product.price} {props.product.currency_code}</p>
          <a href={props.product.url} className="btn btn-primary">View on Etsy</a>
        </div>
      </div >
    );
  }
};

const TableAndCards = (props) => {
  const [events, setEvents] = useState([]);
  const [eventsByPerson, setEventsByPerson] = useState([]);
  const [activeEventID, setActiveEventID] = useState("0");
  const [includeOccasion, setIncludeOccasion] = useState(true);
  const [includeGender, setIncludeGender] = useState(true);
  const [includeRelationship, setIncludeRelationship] = useState(true);
  const [productRows, setProductRows] = useState([]);

  useEffect(() => {
    fetchData('/api/events', setEvents);
  }, []);

  useEffect(() => {
    setEventsByPerson(events.filter(singleEvent => singleEvent.person.id === +props.person_id));
  }, [props.person_id, events]);

  useEffect(() => {
    if (eventsByPerson.length > 0)
      setActiveEventID(eventsByPerson[0].id);
  }, [eventsByPerson]);

  const handleActiveEvent = (e) => {
    setActiveEventID(e.target.value);
  };

  const handleFilterToggle = (e, currentState, toggleState) => {
    toggleState(!currentState);
  };

  useEffect(() => {
    const fetchProducts = async () => {
      const activeEvent = eventsByPerson.filter(event => event.id === +activeEventID)[0];
      const params = {
        limit: 24,
        occasion: activeEvent.occasion.name,
      };
      if (includeOccasion)
        params.taxonomy_id = props.personDetail.interest.id;
      if (includeGender)
        params.gender = props.personDetail.gender.name;
      if (includeRelationship)
        params.relationship = props.personDetail.relationship.type;

      const paramsString = Object.keys(params).map((key) => {
        return [key, params[key]].join("=");
      }).join("&");

      const url = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST + `/api/products?${paramsString}`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        const dataForProductRows = Array.from(Array(Math.ceil(data.products.length / 4)), () => []);
        let [row, count] = [0, 0];
        data.products.forEach((product) => {
          dataForProductRows[row].push(product);
          count++;
          if (count > 3) {
            row++;
            count = 0;
          }
        });
        setProductRows(dataForProductRows);
      }
    };

    if (eventsByPerson.length > 0 && +activeEventID !== 0)
      fetchProducts();
  }, [eventsByPerson, props.personDetail, activeEventID, includeOccasion, includeGender, includeRelationship]);

  if (eventsByPerson.length > 0) {
    return (
      <>
        <hr />
        <div className="row">
          <h3>Upcoming events</h3>
          <div className="offset-1 col-10">
            <table className="table table-hover text-center">
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
                      <td>
                        <button
                          className='btn btn-primary'
                          disabled={event.id === +activeEventID}
                          value={event.id}
                          onClick={handleActiveEvent}
                        >
                          View products
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
            <h3 className='text-center'>Filters</h3>
            <h3 className='text-center'>
              <button
                className={"btn" + (
                  includeOccasion
                    ? " btn-primary"
                    : " btn-outline-secondary"
                )}
                onClick={(e) => handleFilterToggle(e, includeOccasion, setIncludeOccasion)}
                style={{ marginRight: '1em' }}
              >
                {props.personDetail.interest.name}
              </button>
              <button
                className={"btn" + (
                  includeGender
                    ? " btn-primary"
                    : " btn-outline-secondary"
                )}
                onClick={(e) => handleFilterToggle(e, includeGender, setIncludeGender)}
                style={{ marginRight: '1em' }}
              >
                {props.personDetail.gender.name}
              </button>
              <button
                className={"btn" + (
                  includeRelationship
                    ? " btn-primary"
                    : " btn-outline-secondary"
                )}
                onClick={(e) => handleFilterToggle(e, includeRelationship, setIncludeRelationship)}
              >
                {props.personDetail.relationship.type}
              </button>
            </h3>
          </div>
        </div>
        <hr />
        <div className='container-flex'>
          {productRows > 0
            ?
            <h1 className="text-center">No products found</h1>
            :
            productRows.map((rowList, index) => {
              return <CreateRow key={index} rowList={rowList} />;
            })
          }
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
  if (props.people.length > 0) {
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
              {props.people.map(person => {
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
              to={"/delete_person/" + (props.person_id)}
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
        <p> A person must be added to access the dashboard.</p>
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
  const [people, setPeople] = useState([]);
  const [person_id, setPerson] = useState("0");
  const [personDetail, setPersonDetail] = useState({});

  useEffect(() => {
    fetchData('/api/people', setPeople);
  }, []);

  useEffect(() => {
    setPersonDetail(people.filter(person => person.id === +person_id)[0]);
  }, [people, person_id]);

  const handlePersonData = async (e) => {
    setPerson(e.target.value);
  };

  return (
    <div className="container box mt-2 shadow p-4 mt-4">
      <PersonDropdown
        people={people}
        person_id={person_id}
        handlePersonData={handlePersonData}
      />

      {+person_id !== 0 &&
        <TableAndCards
          person_id={person_id}
          personDetail={personDetail}
        />
      }
    </div >
  );
};

export default Dashboard;
