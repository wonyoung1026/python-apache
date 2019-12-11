# 1
mysql -u $(username) -p

# 2
CREATE DATABASE CisoDashboard;

# 3
USE CisoDashboard;

# 4
# Create table usinig the SQL query below before running the app

CREATE TABLE IF NOT EXISTS Computers (
    computer_name VARCHAR(255) PRIMARY KEY,
    os_type VARCHAR(255),
    os_version VARCHAR(255),
    build_number VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE NOW(),
    UNIQUE(computer_name)
);


# 5
# Run below code to check the table
DESCRIBE Computers;

