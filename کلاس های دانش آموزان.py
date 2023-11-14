import keyboard
agents = []
class Student:
    def __init__(self,name,family,absence,average,Class,National_Code,username,password):
        self.name=name
        self.family = family
        self.absence = absence
        self.average = average
        self.Class = Class
        self.National_Code = National_Code
        self.username = username
        self.password = password
def on_key_press():
    input_name = input()
    input_family=input()
    input_absence=int(input())
    input_average=int(input())
    input_Class=int(input())
    input_National_Code=int(input())
    input_username = input()
    input_password = input()
    student = Student(input_name,input_family, input_absence,input_average,input_Class, input_National_Code,input_username,input_password)
    return student
def show_info(student):
    print('name='+student.name,'family='+student.family,'absence='+str(student.absence),'average='+str(student.average),'Class='+str(student.Class),'National_Code='+str(student.National_Code))
def login():
    username=input()
    password=input()
    for i in agents:
        if i.username==username and i.password==password:
            print('login successfuly')
            return i
    print('login unsuccessfuly')
    return 0
while True:
    command = input()
    if command=='show':
        show_info(agents[-1])
    if command == "add":
        agents.append(on_key_press())
        #print(agents[0])
    if command == "esc":
        print("bye")
        break
    if command=='login':
        login_user=login()


