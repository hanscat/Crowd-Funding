#Jake Mathews (jwm5vv) Lab4 for CS 3240 S17


import psycopg2

PG_USER = "postgres"
PG_USER_PASS = "1isNOTprime!"
PG_DATABASE = "course1"
PG_HOST_INFO = "" # use "" for OS X or Windows

# Connect to an existing database
conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
print("** Connected to database.")

# Open a cursor to perform database operations
cur = conn.cursor()

def instructor_numbers(dept_id):
    cur.execute("SELECT instructor,seatstaken FROM coursedata WHERE deptid=%s", (dept_id))
instructor_numbers('APMA')

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM coursedata;")
print("** Output from SQL SELECT: ", cur.fetchone())

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
print("** Closed connection and database.  Bye!.")