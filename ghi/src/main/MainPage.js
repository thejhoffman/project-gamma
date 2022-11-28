function MainPage() {
    return (
        <div className="container-fluid">
            <div className="row align-items-center mainpage">
                <div className="col-sm-6 carousel">
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
                        <button type="button" className="btn btn-primary">Sign Up</button>
                    </div>
                </div>
                <div className="col-sm-6 cards">
                    <div className="row row-cols-1 row-cols-md-2 g-4">
                        <div className="col">
                            <div className="card h-100">
                                <img src="https://pyxis.nymag.com/v1/imgs/b9e/026/397e494a126a1c8605954f937388534898.2x.rsquare.w600.jpg" className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <h6 className="card-title">Nespresso Vertuo Next Coffee and Espresso Maker by De'Longhi</h6>
                                    <p className="card-subtitle mb-2 text-muted">$125</p>
                                    <p className="card-text"><small>Upgrade anyones at-home coffee game with this classic Nespresso machine to make the best at home lattes and help them save to buy a house or whatever the finance bros are saying now.</small></p>
                                </div>
                            </div>
                        </div>
                        <div className="col">
                            <div className="card h-100">
                                <img src="https://pyxis.nymag.com/v1/imgs/c06/07a/95d12f7a1ae3168fb98015a13e8b9a3cec.2x.rsquare.w600.jpg" className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <h6 className="card-title">iHealth COVID-19 Antigen Rapid Test</h6>
                                    <p className="card-subtitle mb-2 text-muted">$12</p>
                                    <p className="card-text"><small>To make sure you’re in the clear before gathering with friends and family. Safety first!</small></p>
                                </div>
                            </div>
                        </div>
                        <div className="col">
                            <div className="card h-100">
                                <img src="https://pyxis.nymag.com/v1/imgs/2d5/230/27613b4fe1ca297a22281c89e139d8882f-secondary-a.2x.rsquare.w600.jpg" className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <h6 className="card-title">Daily Ritual Women’s Relaxed-Fit Mock-Neck Short Puffer Jacket</h6>
                                    <p className="card-subtitle mb-2 text-muted">$40</p>
                                    <p className="card-text"><small>Are you from New York even if you still haven’t worn your puffer jacket this season? This one is available in an array of colors, patterns, and sizes so you can work on your winter ‘fits.</small></p>
                                </div>
                            </div>
                        </div>
                        <div className="col">
                            <div className="card h-100">
                                <img src="https://pyxis.nymag.com/v1/imgs/afb/961/2350d5bb4f395dd089725f87724dca0ef2.2x.rsquare.w600.jpg" className="card-img-top" alt="..." />
                                <div className="card-body">
                                    <h6 className="card-title">Ray-Ban Hexagonal Flat Sunglasses</h6>
                                    <p className="card-subtitle mb-2 text-muted">$163</p>
                                    <p className="card-text"><small>Some classic sunnies on sale are always a great gift idea.</small></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )
}

export default MainPage;
