

import psycopg2


global conn


conn = psycopg2.connect(dbname="users", user="postgres", password="password")


def dropandMake():
	global conn
	cur = conn.cursor()
	cur.execute("DROP DATABASE users")
	cur.execute("CREATE DATABASE users WITH OWNER postgres")

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

def showAllFiles():
	global conn
	cur = conn.cursor()
	cur.execute("SELECT * FROM file")
	reports = cur.fetchall()
	print( "All Files" )
	for report in reports:
		print( report )
	print( "------------------------" )


#
dropandMake()
showAllTables()

showAllReports()
showAllFiles()
