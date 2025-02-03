student_list = []
class Student:
 
    #Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_student_name(self):
        return self.name
    def get_student_id(self):
        return self.id

        
def add_student():
    #try catch for name as str and id as int 
    #fix the length of id and check 
    while(True):
        name = input("Enter the name of the student: ")  
        if(name == "-1"):
            return    
        id = input("Enter the id of the student: ")
        student_list.append([name,id])    

def update_student(): 
    name = input("Enter the name of the student: ")
    id = input("Enter the ID of the student: ")
    if len(student_list) != 0 and [name,id] in student_list:
        remove_index = student_list.index([name,id])
        print(f"The index removed: {remove_index}")
        student_list.pop(remove_index)

        add_student()
    else:
        print("The list is empty or the name or ID of the student does not exist.")


def get_student_list():
    print(f"Here is the student list: ")
    print(student_list)

add_student()
get_student_list()
update_student()                              
get_student_list()

# lists = [["A",1],["B",2]]
# print(["A",1] in lists)