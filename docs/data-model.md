# Data models

## Largesseance monolith

---

### Person
| name            | type                            | unique | optional |
| --------------- | ------------------------------- | ------ | -------- |
| name            | string                          | no     | no       |
| age_range_id    | reference to Age Range entity   | no     | no       |
| gender_id       | reference to Gender entity      | no     | no       |
| account_id      | reference to Account entity     | no     | no       |
| interest_id     | reference to Interest entity    | no     | no       |
| relationship_id | integer                         | no     | no       |


### Event
| name | type | unique | optional |
|------
| name
| date
| person_id
| occasion_id
| account_id
