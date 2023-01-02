from termcolor import colored


class Commander:
    def __init__(self, db, cursor) -> None:
        self.db = db
        self.cursor = cursor

    def createTable(self):
        status = None
        create_table: str = """CREATE TABLE IF NOT EXISTS Todos (
                Title TEXT,
                Description TEXT,
                Created TIMESTAMP
            );
            """
        try:
            self.cursor.execute(create_table)
            self.db.commit()
            status = colored("Table created successfully !", "green", attrs=["bold"])
        except:
            status = colored("Unable to create Table !", "red", attrs=["bold"])
        return status

    def insertData(self, data):
        status = None
        insert_data = (
            """INSERT INTO Todos (Title, Description, Created) VALUES (?,?,?)"""
        )
        try:
            self.cursor.execute(insert_data, data)
            self.db.commit()
            status = colored("Data inserted successfully !", "green", attrs=["bold"])
        except:
            status = colored("Unable to insert Data !", "red", attrs=["bold"])
        return status

    def readData(self):
        read_data = "SELECT * FROM Todos"
        self.cursor.execute(read_data)
        result = self.cursor.fetchall()

        print("Total rows are: ", len(result))
        print(colored("\nPrinting each row\n", "magenta", attrs=["bold"]))
        for rows in result:
            print("\n")
            print(colored("Title: " + rows[0], "green", attrs=["bold"]))
            print(colored("Description: " + rows[1], "green", attrs=["bold"]))
            print(colored("Created: " + rows[2], "cyan", attrs=["bold"]))
            print("\n")
        json_data = {"Title": rows[0], "Description": rows[1], "Created": rows[2]}
        # return json_data
        return result
