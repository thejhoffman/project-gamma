# People API
## Accounts
---
### Get token
* Endpoint path: `/token`
* Endpoint method: `GET`
* Response: Account information, token
* Response shape (JSON):
    ```json
    {
      "access_token": "string",
      "token_type": "string",
      "account": {
        "id": 0,
        "email": "string",
        "name": "string"
      }
    }
    ```
### Login
* Endpoint path: `/token`
* Endpoint method: `POST`
* Request shape (form):
  * username: string
  * password: string
* Response: token
* Response shape (JSON):
    ```json
    {
      "access_token": "string",
      "token_type": "string"
    }
### Logout
* Endpoint path: `/token`
* Endpoint method: `DELETE`
* Headers:
  * Authorization: Bearer token
* Response: true
* Response shape (JSON):
    ```json
    true
    ```
### Create account
* Endpoint path: `/api/accounts`
* Endpoint method: `POST`
* Request shape (form):
  * email: string,
  * password: string,
  * name: string
* Response: account information, token
* Response shape (JSON):
    ```json
    {
      "access_token": "string",
      "token_type": "string",
      "account": {
        "id": 0,
        "email": "string",
        "name": "string"
      }
    }

## People
---
### Get list of all people
* Endpoint path: `/api/people`
* Endpoint method: `GET`
* Query parameters: `None`
* Headers:
  * Authorization: Bearer token
* Request shape (JSON): `None`
* Response: Returns list of all people associated with current logged in user.
* Response shape (JSON):
```json
[
  {
    "id": 0,
    "name": "string",
    "age_range": {
      "id": 0,
      "age": "string"
    },
    "gender": {
      "id": 0,
      "name": "string"
    },
    "interest": {
      "id": 0,
      "name": "string"
    },
    "relationship": {
      "id": 0,
      "type": "string"
    }
  }
]
```
### Create a new person
* Endpoint path: `/api/people`
* Endpoint method: `POST`
* Query parameters: `None`
* Headers:
  * Authorization: Bearer token
* Request shape (JSON):
```json
{
  "name": "string",
  "age_range_id": 0,
  "gender_id": 0,
  "interest_id": 0,
  "relationship_id": 0
}
```
* Response: Return details of new person with id that is associated with current logged in user.
* Response shape (JSON):
```json
{
  "id": 0,
  "name": "string",
  "age_range": {
    "id": 0,
    "age": "string"
  },
  "gender": {
    "id": 0,
    "name": "string"
  },
  "interest": {
    "id": 0,
    "name": "string"
  },
  "relationship": {
    "id": 0,
    "type": "string"
  }
}
```
### Get the details of a person
* Endpoint path: `/api/people/{id}`
* Endpoint method: `GET`
* Query parameters:
  * `id`: Used to query for a specific person
* Headers:
  * Authorization: Bearer token
* Request shape (JSON): `None`
* Response: Return the details of a person that is associated with current logged in user and based off of the id provided
* Response shape (JSON):
```json
{
  "id": 0,
  "name": "string",
  "age_range": {
    "id": 0,
    "age": "string"
  },
  "gender": {
    "id": 0,
    "name": "string"
  },
  "interest": {
    "id": 0,
    "name": "string"
  },
  "relationship": {
    "id": 0,
    "type": "string"
  }
}
No links
422
Validation Er
```
### Update a person
* Endpoint path: `/api/people/{id}`
* Endpoint method: `PUT`
* Query parameters:
  * `id`: Used to query for a specific person
* Headers:
  * Authorization: Bearer token
* Request shape (JSON):
```json
{
  "name": "string",
  "age_range_id": 0,
  "gender_id": 0,
  "interest_id": 0,
  "relationship_id": 0
}
```
* Response: Return the details of the updated person that is associated with current logged in user and based off of the id provided
* Response shape (JSON):
```json
{
  "id": 0,
  "name": "string",
  "age_range": {
    "id": 0,
    "age": "string"
  },
  "gender": {
    "id": 0,
    "name": "string"
  },
  "interest": {
    "id": 0,
    "name": "string"
  },
  "relationship": {
    "id": 0,
    "type": "string"
  }
}
```
### Delete a person
* Endpoint path: `/api/people/{id}`
* Endpoint method: `DELETE`
* Query parameters:
  * `id`: Used to query for a specific person
* Headers:
  * Authorization: Bearer token
* Request shape (JSON): `None`
* Response: Returns a boolean, true if successfully deleted.
* Response shape (JSON):
```json
true
```

## Events
---
### Get a list of events
* Endpoint path: `/api/events`
* Endpoint method: GET
* Headers:
    *Authorization: Bearer token
* Response: A list of Events
* Response shape (JSON):
```json
[
  {
    "id": 0,
    "name": "string",
    "date": "2022-12-12",
    "person": {
      "id": 0,
      "name": "string"
    },
    "occasion": {
      "id": 0,
      "name": "string"
    }
  }
]
```
### Update an event
* Endpoint path: `/api/events/{id}/`
* Endpoint method: PUT
* Headers:
    * Authorization: Bearer token
* Request shape (JSON):
```json
{
  "name": "string",
  "date": "2022-12-12",
  "person_id": 0,
  "occasion_id": 0
}
```
* Response: Update an event
* Response shape (JSON):
```json
{
  "id": 0,
  "name": "string",
  "date": "2022-12-12",
  "person": {
    "id": 0,
    "name": "string"
  },
  "occasion": {
    "id": 0,
    "name": "string"
  }
}
```
### Delete an event
* Endpoint path: `/api/events/{id}/`
* Endpoint method: DELETE
* Headers:
    * Authorization: Bearer token
* Response: Delete an event
* Response shape (JSON):
```json
true
```
