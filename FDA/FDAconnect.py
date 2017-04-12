import psycopg2


global conn

conn = psycopg2.connect("URL")



def getReports():
    global conn
    curs = conn.cursor()
    curs.execute("SELECT * FROM  report") ##whatever we call reports
    reports = curs.fetchall()
    reportsList = []
    for report in reportsList:
        if (report[4] == True):   #What ever index public is
            reportsList.append(report)
    return (reportsList)

def getDocs(report):
    global conn
    curs = conn.cursor()
    curs.execute("SELECT * FROM doc") #whatever we call docs
    documents = curs.fetchall()
    docs = []
    for doc in documents:
        if (doc[1] == report[0]):   #if the doc is in report
            docs.append(doc)
    return (documents)


if __name__ == "__main__":
    print("hello")