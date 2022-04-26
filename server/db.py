import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="engsoc_dinner" )
cursor = connection.cursor()

# cursor.execute("DROP TABLE Nominee;")
# cursor.execute("DROP TABLE Ticket;")
# cursor.execute("DROP TABLE Vote;")

# Query for creating nominee table
NomineeTableSql = """CREATE TABLE Nominee(
ID INT PRIMARY KEY AUTO_INCREMENT,
NAME  VARCHAR(100) NOT NULL,
CATEGORY VARCHAR(100))"""

cursor.execute(NomineeTableSql)

# Query for creating ticket table
TicketTableSql = """CREATE TABLE Ticket(
ID INT PRIMARY KEY AUTO_INCREMENT,
PIN  VARCHAR(10) NOT NULL,
VALUE INT(5),
STATUS VARCHAR(10))"""

cursor.execute(TicketTableSql)

# Query for creating vote table
VoteTableSql = """CREATE TABLE Vote(
ID INT PRIMARY KEY AUTO_INCREMENT,
VCOUNT  INT(5) NOT NULL,
NOMINEE INT REFERENCES Nominee(ID),
TICKET INT REFERENCES Ticket(ID)
)"""

cursor.execute(VoteTableSql)

# some other statements  with the help of cursor
connection.close()