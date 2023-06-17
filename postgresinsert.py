import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(database="Mhofu", user="postgres", password="6809", host="localhost", port="5432")

# Create a cursor object
cur = conn.cursor()

# Execute an INSERT statement
cur.execute("INSERT INTO Mhofu(name, price) VALUES (%s, %s)",  ( SELECT CURRENT_DATE, 0))

# Commit your changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()