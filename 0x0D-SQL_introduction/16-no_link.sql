-- This script lists all records of the table second_table 
-- off the database hbtn_0c_0
SELECT `score`, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
