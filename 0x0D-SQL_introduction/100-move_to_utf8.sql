-- This script converts hbtn_0c_0 database to UTF8
-- convert database hbtn_0c_0, table first_table, field name 
ALTER DATABASE 
    hbtn_0c_0 
    CHARACTER SET = utf8mb4 
    COLLATE = utf8mb4_unicode_ci;
ALTER TABLE 
    hbtn_0c_0.first_table 
    CONVERT TO CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;
ALTER TABLE 
    hbtn_0c_0.first_table 
    MODIFY `name` 
    VARCHAR(256) 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;
