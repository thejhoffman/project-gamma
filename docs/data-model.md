# Data models

## Largesseance monolith

---

### Occasion
| name | type   | unique | optional |
| ---- | ------ | ------ | -------- |
| id   | serial | yes    | no       |
| name | string | yes    | no       |
| date | date   | no     | yes      |

### Interest
| name | type   | unique | optional |
| ---- | ------ | ------ | -------- |
| id   | int    | yes    | no       |
| name | string | yes    | no       |

### Gender
| name | type   | unique | optional |
| ---- | ------ | ------ | -------- |
| id   | serial | yes    | no       |
| name | string | yes    | no       |

### Relationship
| name | type   | unique | optional |
| ---- | ------ | ------ | -------- |
| id   | serial | yes    | no       |
| type | string | yes    | no       |

### Age Range
| name | type   | unique | optional |
| ---- | ------ | ------ | -------- |
| id   | serial | yes    | no       |
| age  | string | yes    | no       |

### Person
| name            | type                             | unique | optional |
| --------------- | -------------------------------  | ------ | -------- |
| id              | serial                           | yes    | no       |
| name            | string                           | no     | no       |
| age_range_id    | reference to Age Range entity    | no     | no       |
| gender_id       | reference to Gender entity       | no     | no       |
| account_id      | reference to Account entity      | no     | no       |
| interest_id     | reference to Interest entity     | no     | no       |
| relationship_id | reference to Relationship entity | no     | no       |

### Event
| name        | type                         | unique | optional |
| ----------- | ---------------------------- | ------ | -------- |
| id          | serial                       | yes    | no       |
| name        | string                       | no     | no       |
| date        | date                         | no     | no       |
| person_id   | reference to Person entity   | no     | no       |
| occasion_id | reference to Occasion entity | no     | yes      |
| account_id  | reference to Account entity  | no     | no       |
