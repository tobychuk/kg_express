CREATE DATABASE test_db;
CREATE USER test_user  WITH PASSWORD 'admin';
ALTER ROLE test_user SET client_encoding TO 'utf-8';
ALTER ROLE test_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE test_user SET timezone TO 'Asia/Bishkek';
GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;

/Users/Asus/OneDrive/"Рабочий стол"/it.run lessens/shop/express_kg/sql_db/create_db.sql

