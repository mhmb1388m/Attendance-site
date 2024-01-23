agents = []
managers=[]
teachers=[]
god_manager = {"name" : "mohammad hosein"}
#god_manager=[name['Mohammad hosein'] , family[ 'mohammad bagheri'] , username['Mhmb1388102'] , password['1388102mhmb']]
teachers_average = []

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
class Manager:
    def __init__(self,name,family,username,password):
        self.name=name
        self.family=family
        self.username=username
        self.password=password
class Teachers:
    def __init__(self , name , family , absens , average , username , password ):
        self . name = name
        self . family = family
        self . absens = absens
        self . average = average
        self . username = username
        self . password = password
def add_student():
    input_name = input()
    input_family=input()
    input_absence=int(input())
    input_average=int(input())
    input_Class=int(input())
    input_National_Code=int(input("input_National_Code:"))
    input_username = input()
    input_password = input()
    student = Student(input_name,input_family, input_absence,input_average,input_Class, input_National_Code,input_username,input_password)
    return student
def add_manager():
    input_name = input()
    input_family = input()
    input_username = input()
    input_password = input()
    manager = Manager(input_name, input_family,input_username, input_password)
    return manager
def add_teacher():
    input_name = input()
    input_family = input()
    input_username = input()
    input_password = input()
    input_absens = int(input())
    input_average = int(input())
    teacher = Teachers(input_name, input_family,input_absens,input_average, input_username, input_password)
    return teacher
def show_info(student):
    print('name='+student.name,'family='+student.family,'absence='+str(student.absence),'average='+str(student.average),'Class='+str(student.Class),'National_Code='+str(student.National_Code))
def login_user():
    username=input()
    password=input()
    for i in range(len(agents)):
        if agents[i].username==username and agents[i].password==password:
            print('login successfuly')
            return i
    print('login unsuccessfuly')
    return 0
def login_manager():
    username=input()
    password=input()
    for i in range(len(managers)):
        if managers[i].username==username and managers[i].password==password:
            print('login_manager successfuly')
            return i
    print('login_manager unsuccessfuly')
    return 0
def remove(username , password):
    username = input()
    password = input()
    for i in range(len(agents)):
        if agents[i].username == username and agents[i].password == password :
            agents . remove(i)
            return 'remove successfuly'
        else:
            return 'remove unsuccessfuly'
def grading_the_teachers():
    family_teacher=input()
    for i in range (len(teachers)):
        if teachers[i].family == family_teacher:
            average=int(input())
            teachers_average . append(average)
def login_god_manager():
    username=input()
    password=input()
    if
def read_txt_file():
    file_name = input()
    file_path = f'C:\\Users\\USER\\Desktop\\{file_name}.txt'
    file = open(file_path, 'r', encoding='utf-8')
    return file

file = read_txt_file()

while True:
    command = file.readline()
    print(command)
    if command=='login':
        login_user=login_user()
        if login_user=='login successfuly':
            t=file.readline()
            if t == 'show':
                show_info(agents[-1])
            if t == 'grading the teachers':
                grading_the_teachers()
            if t == "esc":
                print("bye")
                break
    if command == 'login_manager':
        login__manager=login_manager()
        if login__manager=='login_manager successfuly':
            t=file.readline()
            if t == "add":
                agents.append(add_student())
            if t == 'remove':
                print(remove())
            if t == 'add teacher':
                teachers . append(add_teacher())
            if t == 'add manager':
                managers . append(add_manager())





