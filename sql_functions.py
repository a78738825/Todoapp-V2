from termcolor import colored



def createTable(db, cursor):
    """Function for creating a Table with name Todos if it doesn'tm exists
    
    Keyword arguments:
     db : Takes sqllite connecting variable for commiting changes i.e. db = sqllite3.connect(....)
     cursor : For executing sqllite commands, takes argument as variable of db.cursor()
    Return: None
    """
    create_table: str = """CREATE TABLE IF NOT EXISTS Todos (
            Title TEXT,
            Description TEXT,
            Created TIMESTAMP
        );
        """
    cursor.execute(create_table)
    db.commit()


def insertData(db, cursor, data):
    insert_data = """INSERT INTO Todos (Title, Description, Created) VALUES (?,?,?)"""
    cursor.execute(insert_data, data)
    db.commit()


def readData(cursor):
    read_data = "SELECT * FROM Todos"
    cursor.execute(read_data)
    result = cursor.fetchall()

    print("Total rows are: ", len(result))
    print(colored("\nPrinting each row\n", "magenta", attrs=["bold"]))
    for rows in result:
        print(colored("Title: " + rows[0], "green", attrs=["bold"]))
        print(colored("Description: " + rows[1], "green", attrs=["bold"]))
        print(colored("Created: " + rows[2], "cyan", attrs=["bold"]))
        print("\n")

