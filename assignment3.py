#Name :Yash Vishwari
#Enrollment No:0176EC231037
#Batch :6 (MTF) 
#Batch time: 12:10pm - 1:50pm 

import quiz_module
admin ="Admin LNCT"
admin_pswd ="LNCT Bhopal"
admin_contact ="1234567890"
admin_mail ="admin123@gmail.com" 
logged_user = ''
logged = False
names ={admin:admin}
dt ={} # dt = date-time
score ={}
enrollment_no ={}
branches ={}
year ={}
phone_no ={admin:admin_contact}
usernames =[admin]
passwords ={admin:admin_pswd}
mail_id={admin:admin_mail}

def register():
  print("---REGISTRATION---")
  name=  input("Please Enter Your name :")
  mno= input("Please enter your Mobile Number :")
  mail = input("Please Enter your mail-id :")
  enrno =input("Enter Your Enrollment no :")
  branch =input("Enter Your Branch :")
  acad_year =input("Enter Your Academic year :")
  uname = input("Enter a username :")
  usernames.append(uname)
  pswd = input("Enter Your Password :")
  passwords[uname] =pswd
  phone_no[uname] =mno
  names[uname]= name
  enrollment_no[uname] =enrno
  mail_id[uname] =mail
  branches[uname] = branch
  year[uname] =acad_year
  score[uname] =[0,0,0]
  dt[uname] =[0,0,0]
  print("------REGISTRATION SUCCESSFULL------")
  print()


def login():
    global logged_user
    global logged
    print("------Login-----------")
    type = input('''
        Choose Login type:
        1.User
        2.Admin
            select option 1/2: ''')
    
    if(type =='1'):

        user = input("Please enter Username :") 
        if user not in usernames or user ==admin:
            print("Invalid Username !")
            return
        
        pswd = input("Please enter Password :")

        if passwords[user] != pswd:
            print("Invalid Password !")
            return
        logged_user=user
    else:
        user = input("Please enter Admin name :")
        if user != admin:
            print("Invalid name !")
            return
        pswd = input("Please enter Password :")
        if passwords[admin] != pswd:
            print("Invalid Password !")
            return
        logged_user=admin
    
    logged = True

def run_quiz():
    
    if logged ==False:
        login()
    

    if logged_user !=admin:
        quiz_module.user_display(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)

        
    else:
        quiz_module.admin_display(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)



def terminate():
    exit()


def main():
    print("Welcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Quiz
        4. Exit

            select option 1/2/3/4: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    
    elif response == '3':
        run_quiz()

    elif response == '4':
        terminate()

       
    else:
        print("Invalid Choice, Please select correct option")
    
    main()   

        

main()






