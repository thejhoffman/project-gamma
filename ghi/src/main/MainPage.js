import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useGetTokenQuery } from "../store/tokenApi";
import htmlDecode from '../utils/htmlDecode';

const baseURL = process.env.REACT_APP_SAMPLE_SERVICE_API_HOST;

function ProductColumn(props) {
  return (
    <>
      {props.list.map(product => {
        if (product === undefined) {
          return null;
        }

        return (
          <div className="col mb-4" id="mainpage-card" key={product.MainImage.listing_id}>
            <div className="card h-100 mb-3 shadow">
              <a href={product.url} className="mainpage-link">
                <div className="mainpage-hover">
                  <div className="mainpage-hover-content"><i className="fas fa-cart-shopping fa-3x"></i></div>
                </div>
                <img src={product.MainImage.url_170x135} className="card-img-top" alt="..." />
              </a>
              <div className="card-body">
                <div className="card-title">{htmlDecode(product.title)}</div>
                <p className="card-subtitle mb-2 text-muted">${product.price} {product.currency_code}</p>
              </div>
            </div>
          </div>
        );
      })}
    </>
  );
}


function MainPage() {

  const [productColumns, setProductColumns] = useState([[], []]);
  const [occasions, setOccasions] = useState([]);
  const [occasion, setOccasion] = useState('');
  const [price, setPrice] = useState('');
  const [offset, setOffset] = useState(4);
  const navigate = useNavigate();
  const { data: token } = useGetTokenQuery();

  async function getCards(keywords) {
    const url = baseURL + `/api/products?${keywords}`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      const requests = [];
      for (let product of data.products) {
        requests.push(product);
      }
      const productColumns = [[], []];

      let i = 0;
      for (const request of requests) {
        productColumns[i].push(request);
        i = i + 1;
        if (i > 1) {
          i = 0;
        }
      }
      setProductColumns(productColumns);
    }
  }

  useEffect(() => {
    getCards('');
  }, []);

  useEffect(() => {
    async function getOccasions() {
      const url = baseURL + `/api/occasions`;
      const response = await fetch(url);
      if (response.ok) {
        const data = await response.json();
        setOccasions(data);
      }
    }
    getOccasions();
  }, []);

  function objToQueryString(obj) {
    const keyValuePairs = [];
    for (const key in obj) {
      keyValuePairs.push(encodeURIComponent(key) + '=' + encodeURIComponent(obj[key]));
    }
    return keyValuePairs.join('&');
  }

  useEffect(() => {
    const obj = {};
    if (price !== '') {
      obj["max_price"] = price;
    }
    if (occasion !== '') {
      obj["occasion"] = occasion;
    }
    const data = objToQueryString(obj);
    getCards(data);
  }, [occasion, price]);

  function randomize() {
    const data = objToQueryString({ offset: offset });
    getCards(data);
    setOffset(offset + 4);
  }

  function signUp() {
    navigate("/signup");
  }

  var signUpButton = "btn btn-primary";
  if (token !== null) {
    signUpButton = "btn btn-primary d-none";
  }



  return (
    <div className="container mt-2" id="mainpage">
      <div className="row justify-content-center">
        <div className="col-lg-6 carousel box shadow-lg p-3 mb-5">
          <div className="carousel slide carousel-fade" data-bs-ride="carousel" id="carousel">
            <h2>Gift shopping made easier</h2>
            <p>
              Never lose track of a special occasion again
              <br />Receive personalized gift suggestions
            </p>
            <div className="carousel-inner">
              <div className="carousel-item active" data-bs-interval="3000">
                <img src="https://images.unsplash.com/photo-1513885535751-8b9238bd345a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" className="d-block w-100" alt="colorfully wrapped gifts with ribbons"></img>
              </div>
              <div className="carousel-item" data-bs-interval="3000">
                <img src="https://images.unsplash.com/photo-1608755728617-aefab37d2edd?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" className="d-block w-100" alt="multiple wrapped gifts with string ribbons"></img>
              </div>
              <div className="carousel-item" data-bs-interval="3000">
                <img src="https://images.unsplash.com/photo-1607469256872-48074e807b0a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" className="d-block w-100" alt="wrapped gifts with red ribbons and green ribbons"></img>
              </div>
            </div>
            <button className="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
              <span className="carousel-control-prev-icon" aria-hidden="true"></span>
              <span className="visually-hidden">Previous</span>
            </button>
            <button className="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
              <span className="carousel-control-next-icon" aria-hidden="true"></span>
              <span className="visually-hidden">Next</span>
            </button>
            <br />
            <button onClick={signUp} type="submit" className={signUpButton}>Sign Up</button>
          </div>
        </div>
      </div>

      <div className="row justify-content-center">
        <div className="col cards fluid box shadow-lg p-3 mb-5">
          <div className="row row-cols-1 row-cols-sm-3 pb-3">
            <div className="col-md-4 d-flex justify-content-center">
              <select onChange={e => setOccasion(e.target.value)} value={occasion} id="occasion" className="form-select btn-outline-danger shrink-when-sm" aria-label="Occasion">
                <option value="">Occasion</option>
                {occasions.map(occasion => <option key={occasion.id} value={occasion.name}>{occasion.name}</option>)}
              </select>
            </div>
            <div className="col-md-4 d-flex justify-content-center">
              <select onChange={e => setPrice(e.target.value)} value={price} id="price" className="form-select btn-outline-danger shrink-when-sm" aria-label="Price">
                <option value="">Max Price</option>
                <option value="20">$20</option>
                <option value="50">$50</option>
                <option value="100">$100</option>
                <option value="150">$150</option>
              </select>
            </div>
            <div className="col-md-4 d-flex justify-content-center">
              <button onClick={randomize} type="submit" className="btn btn-outline-danger shrink-when-sm">Randomize</button>
            </div>
          </div>

          <div className="row row-cols-2 row-cols-lg-4 cards">
            {productColumns.map((productList, index) => {
              return (
                <ProductColumn key={index} list={productList} />
              );
            })}
          </div>
        </div>
      </div>

    </div>
  );
}

export default MainPage;
