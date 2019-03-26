from mysql import connector

class Connection:

    def __init__(self):
        self.con = connector.connect(user="root",password="root",host="127.0.0.1",database='planner')
        self.cur = self.con.cursor(buffered=True)

    def __enter__(self):
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.con
    
    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def execute(self,sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()


    def retrive(self,sql):
        self.execute(sql)
        self.commit()
        return self.fetchall()
    
    def insert(self,sql):
        self.execute(sql)
        self.commit()
        return self.cursor
