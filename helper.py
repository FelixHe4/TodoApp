import sqlite3

DB_PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'
#Function establishes a connection with the database and executes an insert query. 
#It returns the inserted item and its status
def add_to_list(item):
    #adding an item to the db.
    try:
        conn = sqlite3.connect(DB_PATH)
        #Once a connection has been established, we use the cursor object to execute queries
        c = conn.cursor() 
        #Keep the initial status as Not Started
        c.execute('insert into items(item , status) values(?,?)', (item, NOTSTARTED))
        #We commit to save the change
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None