from connection_code import *
class Emp():
    
    def __init__(self):
        try:
            x = int(raw_input("< 1 > Register \n< 2 > Update \n< 3 > Delete \n< 4 > View Registered Details"))
            
            if x == 1 :
                self.user()
            elif x == 2:
                self.update()
            elif x == 3:
                self.delete()
            elif x == 4:
                self.changes()
            else:
                print('Sorry, we are unable to understand ')
                self.__init__()
        except ValueError:
            print("OOPS Error\nPlease select correct value")
            self.__init__()

            
    def user(self):
        self.name = raw_input("Enter name: ")
        self.age = raw_input("Enter age: ")
        cursor.execute("INSERT INTO students(name, age) VALUES (%s, %s)" , (self.name,self.age))
        print('Successfully registered')
        x = int(raw_input("Press 1 to home\nPress any other number to exit\n"))
        if x == 1:
            self.__init__()
        else:
            exit
        
    def delete(self):
        self.name = raw_input("Enter name: ")
        sql = "DELETE FROM students WHERE name = %s"
        adr = (self.name, )
        cursor.execute(sql, adr)
        x = int(raw_input("Press 1 to check details < deleted or not >\nPress any other number to exit\n"))
        if x == 1:
            self.changes()
        else:
            exit

    def update(self):
        self.name = raw_input("Enter name to update age: ")
        self.age = raw_input("Enter age: ")
        sql = "UPDATE students SET age = %s WHERE name = %s"
        adr = (self.age,self.name, )
        cursor.execute(sql, adr)
        x = int(raw_input("Press 1 to check details < updated or not >\nPress any other number to exit\n"))
        if x == 1:
            self.changes()
        else:
            exit 

    def changes(self):
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row in result:
            print(row)
        x = int(raw_input("Press 1 to home\nPress any other number to exit\n"))
        if x == 1:
            self.__init__()
        else:
            exit

emp = Emp()  
db.commit()