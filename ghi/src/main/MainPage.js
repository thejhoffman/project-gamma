import { useEffect, useState } from "react";

function ProductColumn(props) {
    return (
        <>
            {props.list.map(product => {
                return (
                    <div className="col mb-4" id="mainpage-card">
                        <div className="card h-100" key={product.url} onClick={() => { window.open(`${product.url}`) }}>
                            <img src={product.MainImage.url_170x135} className="card-img-top" alt="..." />
                            <div className="card-body h-100">
                                <div className="card-title">{product.title}</div>
                                <p className="card-subtitle mb-2 text-muted">${product.price}</p>
                                {/* <p className="card-text"><small></small></p> */}
                            </div>
                        </div>
                    </div>
                )
            })}
        </>
    )
}


function MainPage() {

    const [productColumns, setProductColumns] = useState([[], []]);
    const [occasions, setOccasions] = useState([]);
    const [occasion, setOccasion] = useState('');
    const [price, setPrice] = useState('');

    useEffect(() => {
        async function getCards() {
            const url = `http://localhost:8000/api/products`;
            const response = await fetch(url, { credentials: 'include' });
            if (response.ok) {
                const data = await response.json();
                const requests = [];
                for (let product of data.products) {
                    requests.push(product);
                }
                const productColumns = [[], []];

                let i = 0;
                for (const request of requests) {
                    productColumns[i].push(request)
                    i = i + 1;
                    if (i > 1) {
                        i = 0;
                    }
                }
                setProductColumns(productColumns)
            }
        }
        getCards();
    }, [])

    useEffect(() => {
        async function getOccasions() {
            const url = `http://localhost:8000/api/occasions`;
            const response = await fetch(url);
            if (response.ok) {
                const data = await response.json();
                setOccasions(data)
            }
        }
        getOccasions();
    }, [])

    return (
        <div className="container-fluid" id="mainpage">
            <div className="row align-items-center mainpage">
                <div className="col-lg-6 carousel">
                    <div className="carousel slide carousel-fade" data-bs-ride="carousel" id="carousel">
                        <h2>Gift shopping made easier</h2>
                        <p>
                            Never lose track of a special occasion again
                            <br />Receive personalized gift suggestions
                        </p>
                        <div className="carousel-inner">
                            <div className="carousel-item active" data-bs-interval="3000">
                                <img src="https://images.unsplash.com/photo-1513885535751-8b9238bd345a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" className="d-block w-100" alt="..."></img>
                            </div>
                            <div className="carousel-item" data-bs-interval="3000">
                                <img src="https://images.unsplash.com/photo-1608755728617-aefab37d2edd?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" className="d-block w-100" alt="..."></img>
                            </div>
                            <div className="carousel-item" data-bs-interval="3000">
                                <img src="https://images.unsplash.com/photo-1607469256872-48074e807b0a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" className="d-block w-100" alt="..."></img>
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
                        <button type="submit" className="btn btn-primary">Sign Up</button>
                    </div>
                </div>
                <div className="col-lg-6 cards">
                    <div className="row pb-3">
                        <div className="col-md-4 d-flex justify-content-center">
                            <select onChange={e => setOccasion(e.target.value)} value={occasion} id="occasion" className="form-select btn-outline-danger" aria-label="Occasion">
                                <option>Occasion</option>
                                {occasions.map(occasion => <option key={occasion.id} value={occasion.name}>{occasion.name}</option>)}
                            </select>
                        </div>
                        <div className="col-md-4 d-flex justify-content-center">
                            <select onChange={e => setPrice(e.target.value)} value={price} id="price" className="form-select btn-outline-danger" aria-label="Price">
                                <option>Max Price</option>
                                <option value="25">$25</option>
                                <option value="50">$50</option>
                                <option value="75">$75</option>
                                <option value="100">$100</option>
                            </select>
                        </div>
                        <div className="col-md-4 d-flex justify-content-end">
                            <button type="submit" className="btn btn-outline-danger">Randomize</button>
                        </div>
                    </div>

                    <div className="row row-cols-1 row-cols-md-2 cards">
                        {productColumns.map((productList, index) => {
                            return (
                                <ProductColumn key={index} list={productList} />
                            )
                        })}
                    </div>
                </div>
            </div>
        </div>
    )
}

export default MainPage;
