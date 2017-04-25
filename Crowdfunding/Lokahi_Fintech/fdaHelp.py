

import psycopg2


global conn


conn = psycopg2.connect(dbname="users", user="postgres", password="password")

def showAllTables():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT table_name FROM information_schema.tables")
	tables = cur.fetchall()
	tables.sort()
	print( "All Tables" )
	for row in tables:
		print( row )
	print( "------------------------" )



def showAllReports():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT * FROM report")
	reports = cur.fetchall()
	print( "All Reports" )
	for report in reports:
		print( report )
	print( "------------------------" )


#
showAllReports()
#showAllTables()
