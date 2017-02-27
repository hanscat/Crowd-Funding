#Jake Mathews (jwm5vv) Lab4 for CS 3240 S17

import csv
import psycopg2

PG_USER = "postgres"
PG_USER_PASS = "1isNOTprime!"
PG_DATABASE = "course1"
PG_HOST_INFO = "" # use "" for OS X or Windows

# Connect to an existing database
conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
print("** Connected to database.")
print("Will Cricchi was here muahaha")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table, but first removes it if it's there already
cur.execute("DROP TABLE IF EXISTS coursedata;")
cur.execute("CREATE TABLE coursedata (deptID text, courseNum int, semester int, meetingType text, seatsTaken int, seatsOffered int, instructor text);")
print("** Created table.")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO coursedata (deptid, coursenum, semester, meetingtype, seatstaken, seatsoffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)
load_course_database(PG_DATABASE, 'seas-courses-5years.csv')
print("** Exectuted SQL INSERT into database.")

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM coursedata;")
print("** Output from SQL SELECT: ", cur.fetchone())

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
print("** Closed connection and database.  Bye!.")