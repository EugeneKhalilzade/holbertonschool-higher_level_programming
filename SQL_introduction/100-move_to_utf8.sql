-- Convert database, table, and column to UTF8 (utf8mb4)
-- Holberton School SQL task

ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

