steps = [
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
            (1, 'Boyfriend'),
            (2, 'Brother'),
            (3, 'Colleague'),
            (4, 'Daughter'),
            (5, 'Father'),
            (6, 'Friend'),
            (7, 'Girlfriend'),
            (8, 'Husband'),
            (9, 'Mother'),
            (10, 'Relative'),
            (11, 'Sister'),
            (12, 'Son'),
            (13, 'Wife');
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
            (1, 'Anniversary', NULL),
            (2, 'Baby Shower', NULL),
            (3, 'Baptism', NULL),
            (4, 'Birthday', NULL),
            (5, 'Bridal Shower', NULL),
            (6, 'Christmas', '2022-12-25'),
            (7, 'Engagement', NULL),
            (8, 'Graduation', NULL),
            (9, 'Hanukkah', '2022-12-18'),
            (10, 'Valentines', '2023-02-14'),
            (11, 'Wedding', NULL)
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
