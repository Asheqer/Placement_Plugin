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

QUERIES_INPUT = f"""
You have access to a MySQL Database that contains all the latest industrial palcement
Generate an array of search queries that are relevant to this question.
Use a variation of related keywords for the queries, trying to be as general as possible.
Include as many queries as you can think of, including and excluding terms.
For example, include queries like ['keyword_1 keyword_2', 'keyword_1', 'keyword_2'].
Be creative. The more queries you include, the more likely you are to find relevant results
User question: {input}

Format: {{"queries": ["query_1", "query_2", "query_3"]}}
"""