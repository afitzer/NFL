import sqlite3

# This function gets the table head and returns a list of all the fields in the table head row.
def get_table_head_fields_as_list(table_obj):
    result = []
    table_head = table_obj.find('thead')
    table_head_fields = table_head.find_all('th')
    for field_obj in table_head_fields:
        result.append(field_obj.getText().strip())
    return result

# This function gets the table body and return a list of rows with data fields.
def get_table_body_as_lists(table_obj):
    result = []
    table_body = table_obj.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        curr_row = []
        row_fields = row.find_all('td')
        for field_obj in row_fields:
            curr_row.append(field_obj.getText().strip())
        result.append(curr_row)
    return result

# This functions creates the table for the Offensive Teams Passing data.
def create_offensive_teams_passing():
    conn = sqlite3.connect('nfl.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS offensive_passing (
    "Team"	TEXT NOT NULL UNIQUE,
	"Att"	INTEGER NOT NULL,
	"Cmp"	INTEGER NOT NULL,
	"Cmp %"	REAL NOT NULL,
	"Yds/Att"	REAL NOT NULL,
	"Pass Yds"	INTEGER NOT NULL,
	"TD"	INTEGER NOT NULL,
	"INT"	INTEGER NOT NULL,
	"Rate"	REAL NOT NULL,
	"1st"	INTEGER NOT NULL,
	"1st%"	INTEGER NOT NULL,
	"20+"	INTEGER NOT NULL,
	"40+"	INTEGER NOT NULL,
	"Lng"	TEXT NOT NULL,
	"Sck"	INTEGER NOT NULL,
	"SckY"	INTEGER NOT NULL,
	"Date"	TEXT NOT NULL,
	PRIMARY KEY("Team")
);
""")
    conn.commit()
    conn.close()

# This function creates the table for the Offensive Teams Receiving data.
def create_offensive_teams_receiving():
    conn = sqlite3.connect('nfl.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS offensive_receiving (
    "Team"	TEXT NOT NULL UNIQUE,
	"Rec"	INTEGER NOT NULL,
	"Yds"	INTEGER NOT NULL,
	"Yds/Rec"	REAL NOT NULL,
	"TD"	INTEGER NOT NULL,
	"20+"	INTEGER NOT NULL,
	"40+"	INTEGER NOT NULL,
	"Lng"	TEXT NOT NULL,
	"Rec 1st"	INTEGER NOT NULL,
	"Rec 1st%"	REAL NOT NULL,
	"Rec FUM"	INTEGER NOT NULL,
	"Date"	TEXT NOT NULL,
	PRIMARY KEY("Team")
);
""")
    conn.commit()
    conn.close()

# This function creates the table for the Offensive Teams Rushing data.
def create_offensive_teams_rushing():
    conn = sqlite3.connect('nfl.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS offensive_rushing (
    "Team"	TEXT NOT NULL UNIQUE,
	"Att"	INTEGER NOT NULL,
	"Rushs Yds"	INTEGER NOT NULL,
	"YPC"	REAL NOT NULL,
	"TD"	INTEGER NOT NULL,
	"20+"	INTEGER NOT NULL,
	"40+"	INTEGER NOT NULL,
	"Lng"	TEXT NOT NULL,
	"Rec 1st"	INTEGER NOT NULL,
	"Rec 1st%"	REAL NOT NULL,
	"Rec FUM"	INTEGER NOT NULL,
	"Date"	TEXT NOT NULL,
	PRIMARY KEY("Team")
);
""")
    conn.commit()
    conn.close()

# This function creates the table for the Offensive Teams Scoring data.
def create_offensive_teams_scoring():
    conn = sqlite3.connect('nfl.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS offensive_scoring (
    "Team"	TEXT NOT NULL UNIQUE,
	"Rush TD"	INTEGER NOT NULL,
	"Rec TD"	INTEGER NOT NULL,
	"Tot TD"	INTEGER NOT NULL,
	"2-PT"	INTEGER NOT NULL,
	"Date"	TEXT NOT NULL,
	PRIMARY KEY("Team")
);
""")
    conn.commit()
    conn.close()