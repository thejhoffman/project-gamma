steps = [
    [
        # data for person
        """
        INSERT INTO person
        VALUES
            (1, 'Theresa'),
            (2, 'Hello Kitty');
        """,
        """
        DELETE FROM person
        """,
    ],
    [
        # data for age_range
        """
        INSERT INTO age_range
        VALUES
            (1, 'Children (under 14)'),
            (2, 'Youth (15-24)'),
            (3, 'Adults (25-64)'),
            (4, 'Seniors (over 65)');
        """,
        # delete data from age_range
        """
        DELETE FROM age_range
        """,
    ],
    [
        # data for relationships
        """
        INSERT INTO relationships
        VALUES
            (1, 'Spouse'),
            (2, 'Mother'),
            (3, 'Father'),
            (4, 'Colleague');
        """,
        # delete data from relationships
        """
        DELETE FROM relationships
        """,
    ],
    [
        # data for occasions
        """
        INSERT INTO occasion
        VALUES
            (1, 'Christmas', '2022-12-25'),
            (2, 'Valentines', '2023-02-14'),
            (3, 'Hanukkah', '2022-12-18');
        """,
        # delete data from occasions
        """
        DELETE FROM occasion
        """,
    ],
    [
        # data for interests
        """
        INSERT INTO interests
        VALUES
            (1, 'Movies'),
            (2, 'Sports');
        """,
        # delete data from interests
        """
        DELETE FROM interests
        """,
    ],
    [
        # data for gender
        """
        INSERT INTO gender
        VALUES
            (1, 'Male'),
            (2, 'Female'),
            (3, 'Neutral');
        """,
        # delete data from occasions
        """
        DELETE FROM gender
        """,
    ],
]
