import { useState } from 'react';
import { useEffect } from 'react';

function PersonForm() {

    const [name, setName] = useState('');
    const [gender, setGender] = useState('');
    const [age, setAge] = useState('');
    const [relationship, setRelationship] = useState('');
    const [interest, setInterest] = useState('');
    const [genders, setGenders] = useState([]);
    const [ages, setAges] = useState([]);
    const [relationships, setRelationships] = useState([]);
    const [interests, setInterests] = useState([]);

    async function getData(url, setFunction) {
        url = `http://localhost:8000/${url}`;
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            setFunction(data);
        }
    }

    useEffect(() => {
        getData(`gender`, setGenders);
    }, []);

    useEffect(() => {
        getData(`api/age_range`, setAges);
    }, []);

    useEffect(() => {
        getData(`api/relationships`, setRelationships);
    }, []);

    useEffect(() => {
        getData(`api/interests`, setInterests);
    }, []);

    return (
        <div className="container">
            <div className="mb-3">
                <label htmlFor="name" className="form-label">Name</label>
                <input value={name} onChange={e => setName(e.target.value)} required type="text" className="form-control" id="name"></input>
            </div>
            <div className="mb-3">
                <label htmlFor="gender" className="form-label">Gender</label>
                <select onChange={e => setGender(e.target.value)} value={gender} id="gender" className="form-select" aria-label="Gender">
                    <option value="">Select gender</option>
                    {genders.map(gender => <option key={gender.id} value={gender.id}>{gender.name}</option>)}
                </select>
            </div>
            <div className="mb-3">
                <label htmlFor="age" className="form-label">Age</label>
                <select onChange={e => setAge(e.target.value)} value={age} id="age" className="form-select" aria-label="Age" required>
                    <option value="">Select age</option>
                    {ages.map(age => <option key={age.id} value={age.id}>{age.age}</option>)}
                </select>
            </div>
            <div className="mb-3">
                <label htmlFor="relationship" className="form-label">Relationship</label>
                <select onChange={e => setRelationship(e.target.value)} value={relationship} id="relationship" className="form-select" aria-label="Relationship" required>
                    <option value="">Select relationship</option>
                    {relationships.map(relationship => <option key={relationship.id} value={relationship.id}>{relationship.type}</option>)}
                </select>
            </div>
            <div className="mb-3">
                <label htmlFor="interest" className="form-label">Interest</label>
                <select onChange={e => setInterest(e.target.value)} value={interest} id="interest" className="form-select" aria-label="Interest" required>
                    <option value="">Select an interest</option>
                    {interests.map(interest => <option key={interest.id} value={interest.id}>{interest.name}</option>)}
                </select>
            </div>
            {/* <div className="mb-3">
                Select an interest
                <div className="form-check">
                    <input className="form-check-input" type="checkbox" id="interestOptionOne"></input>
                    <label htmlFor="interestOptionTwo" className="form-check-label">Interest 1</label>
                </div>
                <div className="form-check">
                    <input className="form-check-input" type="checkbox" id="interestOptionTwo"></input>
                    <label htmlFor="interestOptionTwo" className="form-check-label">Interest 2</label>
                </div>
            </div> */}
        </div>
    );
}

export default PersonForm;
