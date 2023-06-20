"""
This module connects to the mhofu database and inserts data into the mhofu table.
"""

import psycopg2

# Establish a connection to the database
conn=psycopg2.connect(database="mhofu",
                      user="postgres",
                     password="Eureka22",
                     host="localhost",
                     port="5432")

# Create a cursor object
cur = conn.cursor()

# Execute an INSERT statement
cur.execute("INSERT INTO mhofu(name, price) VALUES (CURRENT_DATE, %s)",
            (0,))

# Commit your changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

#adding newlinecharacter 
print()