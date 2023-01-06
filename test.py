import psycopg2

## Connect to the DB

connection = psycopg2.connect(
        host = "127.0.0.1",
                port = "5432",
        database = "postgres",
        user="postgres",
        password="SAHU2003"
)

connection.autocommit = True # "autcommit" set to True, so you don't have to commit your queries.
cursor = connection.cursor()

# Create Database Query
# Suppose we are asking user to choose, name of the database,


#Execute Query
cursor.execute("SHOW Contact")
for i in cursor:
    print(i)