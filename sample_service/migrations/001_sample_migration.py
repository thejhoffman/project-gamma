steps = [
    [
        ## creates user table
        ## "up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(20) NOT NULL,
            email VARCHAR(100) NOT NULL;
        );
        """,
        # "down" SQL statement for users table
        """
        DROP TABLE users;
        """
    ],
    [
        ## creates occasion table
        ## "up" SQL statement
        """
        CREATE TABLE occasion (
            id SERIAL PRIMARY KEY NOT NULL,
            "name" VARCHAR(50) NOT NULL,
            date DATE
        );
        """,
        # "down" SQL statement for occasion table
        """
        DROP TABLE occasion;
        """
    ],
    [
        ## creates age table
        ## "up" SQL statement
        """
        CREATE TABLE age_range (
            id SERIAL PRIMARY KEY NOT NULL,
            age integer NOT NULL
        );
        """,
        ## "down" SQL statement for age table
        """
        DROP TABLE age_range;
        """
    ],
    [
        ## creates interests table
        ## "up" SQL statement
        """
        CREATE TABLE interests (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL
        );
        """,
        ## down SQL statement for interests table
        """
        DROP TABLE interests;
        """
    ],
    [
        ## creates gender table
        ## "up" SQL statement
        """
        CREATE TABLE gender (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(20) NOT NULL
        );
        """,
        ## "down" SQL statement for gender table
        """
        DROP TABLE gender;
        """
    ],
    [
        """
        CREATE TABLE person (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(50) NOT NULL,
            age_range_id INTEGER NOT NULL REFERENCES age_range("id") ON DELETE PROTECT,
            gender_id VARCHAR(20) REFERENCES gender("id") ON DELETE PROTECT,
            users_id SERIAL NOT NULL REFERENCES users("id") ON DELETE CASCADE,
            interests_id INTEGER NOT NULL REFERENCES interests("id") ON DELETE PROTECT
        );
        """,
        ## "down" SQL statement for person table
        """
        DROP TABLE person;
        """
    ],
    [
        """
        CREATE TABLE events (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            date DATE NOT NULL,
            person_id INTEGER NOT NULL REFERENCES person("id") ON DELETE PROTECT,
            occasion_id INTEGER REFERENCES occasion("id") ON DELETE PROTECT,
            users_id SERIAL NOT NULL REFERENCES users("id") ON DELETE CASCADE
        );
        """,
        ## "down" SQL statement for events table
        """
        DROP TABLE events;
        """
    ],
]
