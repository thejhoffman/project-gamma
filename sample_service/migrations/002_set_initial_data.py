steps = [
    [
        # data for age_range
        """
        INSERT INTO age_range
            (age)
        VALUES
            ('Children (under 14)'),
            ('Youth (15-24)'),
            ('Adults (25-64)'),
            ('Seniors (over 65)');
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
            (type)
        VALUES
            ('Boyfriend'),
            ('Brother'),
            ('Colleague'),
            ('Daughter'),
            ('Father'),
            ('Friend'),
            ('Girlfriend'),
            ('Husband'),
            ('Mother'),
            ('Relative'),
            ('Sister'),
            ('Son'),
            ('Wife');
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
            (name, date)
        VALUES
            ('Anniversary', NULL),
            ('Baby Shower', NULL),
            ('Baptism', NULL),
            ('Birthday', NULL),
            ('Bridal Shower', NULL),
            ('Christmas', '2022-12-25'),
            ('Engagement', NULL),
            ('Graduation', NULL),
            ('Hanukkah', '2022-12-18'),
            ('Valentines', '2023-02-14'),
            ('Wedding', NULL)
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
            (66, 'Art'),
            (324, 'Books'),
            (930, 'Foodies'),
            (1553, 'Games & Puzzles'),
            (355, 'Movies'),
            (356, 'Music'),
            (115, 'Photography'),
            (1560, 'Sports & Outdoors'),
            (875, 'Tech'),
            (1580, 'Toys'),
            (168, 'Travel'),
            (890, 'Video Games'),
            (316, 'Wellness');
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
            (name)
        VALUES
            ('Male'),
            ('Female'),
            ('Neutral');
        """,
        # delete data from occasions
        """
        DELETE FROM gender
        """,
    ],
]
