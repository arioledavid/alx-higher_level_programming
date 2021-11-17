-- This script lists the records with a score >= 10 in the second_table table
-- from the hbtn_0c_0 database
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
