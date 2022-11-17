steps = [
    [
        # creates user table
        # "up" SQL statement
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            email CITEXT UNIQUE NOT NULL,
            name VARCHAR(100) NOT NULL,
            hashed_password TEXT NOT NULL
        );
        """,
        # "down" SQL statement for accounts table
        """
        DROP TABLE accounts;
        """,
    ],
    [
        # creates occasion table
        # "up" SQL statement
        """
        CREATE TABLE occasion (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            date DATE
        );
        """,
        # "down" SQL statement for occasion table
        """
        DROP TABLE occasion;
        """,
    ],
    [
        # creates age table
        # "up" SQL statement
        """
        CREATE TABLE age_range (
            id SERIAL PRIMARY KEY NOT NULL,
            age integer NOT NULL
        );
        """,
        # "down" SQL statement for age table
        """
        DROP TABLE age_range;
        """,
    ],
    [
        # creates interests table
        # "up" SQL statement
        """
        CREATE TABLE interests (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL
        );
        """,
        # down SQL statement for interests table
        """
        DROP TABLE interests;
        """,
    ],
    [
        # creates gender table
        # "up" SQL statement
        """
        CREATE TABLE gender (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(20) NOT NULL
        );
        """,
        # "down" SQL statement for gender table
        """
        DROP TABLE gender;
        """,
    ],
    [
        # creates relationship table
        # "up" SQL statement
        """
        CREATE TABLE relationships (
            id SERIAL PRIMARY KEY NOT NULL,
            type VARCHAR(50) NOT NULL
        );
        """,
        # 'down' SQL statement for person table
        """
        DROP TABLE relationships;
        """,
    ],
    [
        """
        CREATE TABLE person (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            age_range_id INTEGER NOT NULL REFERENCES age_range("id") ON DELETE RESTRICT,
            gender_id INTEGER REFERENCES gender("id") ON DELETE RESTRICT,
            account_id SERIAL NOT NULL REFERENCES accounts("id") ON DELETE CASCADE,
            interest_id INTEGER NOT NULL REFERENCES interests("id") ON DELETE RESTRICT,
            relationship_id INTEGER NOT NULL REFERENCES relationships("id") ON DELETE RESTRICT
        );
        """,
        # "down" SQL statement for person table
        """
        DROP TABLE person;
        """,
    ],
    [
        """
        CREATE TABLE events (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            date DATE NOT NULL,
            person_id INTEGER NOT NULL REFERENCES person("id") ON DELETE RESTRICT,
            occasion_id INTEGER REFERENCES occasion("id") ON DELETE RESTRICT,
            account_id SERIAL NOT NULL REFERENCES accounts("id") ON DELETE CASCADE
        );
        """,
        # "down" SQL statement for events table
        """
        DROP TABLE events;
        """,
    ],
]
