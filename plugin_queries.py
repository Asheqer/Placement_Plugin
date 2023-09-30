create_placement_table_query = """
CREATE TABLE placements_db (
    placement_id INT,
    title VARCHAR(100)
    company VARCHAR(100)
    deadline DATE
    duration VARCHAR(100)
    location VARCHAR(100)
)
"""
insert_single = """
    INSERT INTO Placements (title,company,deadline,duration,location)
    VALUES
        ("kig","cog",20230410,"10+ months","london")
"""
insert_placement_records_query = """
    INSERT INTO Placements
    (title,company,deadline,duration,location)
    VALUES ( %s, %s, %s, %s, %s)
"""

check_duplicates_query = """
    SELECT COUNT(*) FROM placements WHERE title = %s
"""

select_placements_query = "SELECT * FROM placements LIMIT 5"