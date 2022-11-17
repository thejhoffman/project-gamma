# People API
---
### Get list of all people
* Endpoint path: `/api/people/`
* Endpoint method: `GET`
* Query parameters: `None`
* Headers:
  * Authorization: User token
* Request shape (JSON): `None`
* Response: Returns list of all people associated with current logged in user.
* Response shape (JSON):
```json
{
  "people" [
    {
      "id": int,
      "name": "string"
    }
    ...
  ]
}
```
---
### Create a new person
* Endpoint path: `/api/people/`
* Endpoint method: `POST`
* Query parameters: `None`
* Headers:
  * Authorization: User token
* Request shape (JSON):
```json
{
  "name": "string",
  "gender": "string",
  "age_range": "string",
  "relationship:": "string",
  "likes": "string"
}
```
* Response: Return details of new person with id that is associated with current logged in user.
* Response shape (JSON):
```json
{
  "id": int,
  "name": "string",
  "gender": "string",
  "age_range": "string",
  "relationship:": "string",
  "likes": "string"
}
```
---
### Get the details of a person
* Endpoint path: `/api/people/{id}/`
* Endpoint method: `GET`
* Query parameters:
  * `id`: Used to query for a specific person
* Headers:
  * Authorization: User token
* Request shape (JSON): `None`
* Response: Return the details of a person that is associated with current logged in user and based off of the id provided
* Response shape (JSON):
```json
{
  "id": int,
  "name": "string",
  "gender": "string",
  "age_range": "string",
  "relationship:": "string",
  "likes": "string"
}
```
---
### Update a person
* Endpoint path: `/api/people/{id}/`
* Endpoint method: `PUT`
* Query parameters:
  * `id`: Used to query for a specific person
* Headers:
  * Authorization: User token
* Request shape (JSON):
```json
{
  "name": "string",
  "gender": "string",
  "age_range": "string",
  "relationship:": "string",
  "likes": "string"
}
```
* Response: Return the details of the updated person that is associated with current logged in user and based off of the id provided
* Response shape (JSON):
```json
{
  "id": int,
  "name": "string",
  "gender": "string",
  "age_range": "string",
  "relationship:": "string",
  "likes": "string"
}
```
---
### Delete a person
* Endpoint path: `/api/people/{id}/`
* Endpoint method: `DELETE`
* Query parameters:
  * `id`: Used to query for a specific person
* Headers:
  * Authorization: User token
* Request shape (JSON): `None`
* Response: Returns a boolean, true if successfully deleted.
* Response shape (JSON):
```json
{
  boolean
}
```
---
### «Human-readable of the endpoint»
* Endpoint path: «path to use»
* Endpoint method: «HTTP method»
* Query parameters:
  * «name»: «purpose»
* Headers:
  * Authorization: Bearer token
* Request shape (JSON):
```json
«JSON-looking thing that has the
keys and types in it»
```
* Response: «Human-readable description of response»
* Response shape (JSON):
```json
«JSON-looking thing that has the
keys and types in it»
```


# Event API
---
### Get a list of events

* Endpoint path: `/api/events`
* Endpoint method: GET

* Headers:
    *Authorization: Bearer token

* Response: A list of Events

* Response shape (JSON):
    ```json
        "events": [
            {
                "date": "string",
                "event_name": "string",
                "people": "string",
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
        "events": [
            {
                "date": "string",
                "event_name": "string",
                "people": "string",
            }
        ]
    ```

* Response: Update an event

* Response shape (JSON):
    ```json
        "events": [
            {
                "date": "string",
                "event_name": "string",
                "people": "string"
            }
        ]
    ```

### Delete an event

* Endpoint path: `/api/events/{id}/`
* Endpoint method: DELETE

* Headers:
    * Authorization: Bearer token

* Response: Delete an event

* Response shape (JSON):
    ```json
        "events": [
            {
                "date": "string",
                "event_name": "string",
                "people": "string",
            }
        ]
}
    ```
