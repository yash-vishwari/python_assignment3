import random
import datetime
dsa_qans=["B","C","D","C","B"]
dbms_qans=["B","C","D","C","B"]
python_qans=["C","C","B","B","B"]
def admin_display(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
    response = input('''
        Choose option:
        1.Scores
        2.logout
        3.Update profile
        4.Profile
            select option 1/2/3/4: ''')
    

    if response == '1':
        users_scores(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)

    elif response == '2':
        logout(logged,logged_user)
        return
    elif response == '3':
        update_adminprofile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)
    elif response == '4':
        admin_profile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)
    else:
         print("Invalid Choice Please choose a valid option")

    admin_display(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)
    
def  user_display(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
    
    response = input('''
        Choose option:
        1.Attempt quiz
        2.Score
        3.logout
        4.Update profile
        5.Profile
            select option 1/2/3/4/5: ''')
    
    if response == '1':
        category = input('''
        Please Choose a Category:
        1. DSA
        2. DBMS
        3. Python
       
            select option 1/2/3: ''')
        
        if category != '1' and category!= '2' and category != '3':
            print("Invalid Choice Please choose a valid option")

        else:    
            attempt_quiz(category,admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)

    elif response == '2':
        user_score(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)

    elif response == '3':
        logout(logged,logged_user)
        return

    elif response == '4':
        update_userprofile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)

    elif response == '5':
        user_profile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)
    else:
         print("Invalid Choice Please choose a valid option")
         
    user_display(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)

def user_profile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
 
    if logged == False:
        print("Please Login First")
        return
    print("--------User Profile--------")
    print(f"Name :{names[logged_user]}")
    print(f"Enrollment no :{enrollment_no[logged_user]} \t Branch :{branches[logged_user]} \t Year:{year[logged_user]}")
    print(f"Mobile Number :{phone_no[logged_user]} \t Mail-id :{mail_id[logged_user]}")
    

def admin_profile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
    
    if logged == False:
        print("Please Login First")
        return
    print("--------Admin Profile--------")
    print(f"Name :{names[logged_user]}")
    print(f"Mobile Number :{phone_no[logged_user]} \t Mail-id :{mail_id[logged_user]}")    
   
    
def update_userprofile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
    
    if logged == False:
        print("Please Login First")
        return
    response = input('''
        What do you want to update:
        1. Name
        2. Phone Number
        3. Mail id
        4. Branch
        5. Year             
        6.Exit
            select option 1/2/3/4/5: ''')
    
    if response == '1':
        names[logged_user] =input("Enter updated name :")

    elif response == '2':
         phone_no[logged_user] =input("Enter updated phone number :")

    elif response == '3':
         mail_id[logged_user] =input("Enter updated mail id:")

    elif response == '4':
         branches[logged_user] =input("Enter Branch :")

    elif response == '5':
        year[logged_user] =input("Enter Academic year :") 

    elif response == '6':
        return
       
    else:
        print("Invalid Choice, Please select correct option")    
    update_userprofile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)


def update_adminprofile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
    
    if logged == False:
        print("Please Login First")
        return
    response = input('''
        What do you want to update:
        1. Name
        2. Phone Number
        3. Mail id
        4.Exit
            select option 1/2/3: ''')
    
    if response == '1':
       names[logged_user] =input("Enter updated name :")
    elif response == '2':
        phone_no[logged_user] =input("Enter updated phone number :")
    elif response == '3':
        mail_id[logged_user] =input("Enter updated mail id:")
    elif response == '4':
        return
    else:
        print("Invalid Choice, Please select correct option")
    update_adminprofile(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)            
    

def logout(logged,logged_user):
    
    if  logged== False:
        print("Please Login First")
        return
    logged = False
    logged_user =''
    print("-----Logout Successfull-----")
    return

def attempt_quiz(category,admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):

    if category =='1':
        dsa_quiz(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)
    elif category =='2':
        dbms_quiz(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)
    else:
        python_quiz(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt)


def dsa_quiz(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
  
   dsa_score =0 
   file =open("dsa.txt", "r") 
   content = file.read().strip().split("\n\n")
   indexed_content = list(enumerate(content)) 
   random.shuffle(indexed_content)

   for i,ques in indexed_content:
       print(f"\n{ques}")
       user_ans = input("Enter your answer A/B/C/D :").upper()
       if user_ans == dsa_qans[i]:
           dsa_score +=1
             
   score[logged_user][0] =dsa_score
   dt_details =datetime.datetime.now()
   dt_details = dt_details.strftime("%d-%m-%Y ,%H:%M:%S")
   dt[logged_user][0] =dt_details
   

def dbms_quiz(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
   
   dbms_score =0 
   file =open("dbms.txt", "r") 
   content = file.read().strip().split("\n\n")
   indexed_content = list(enumerate(content)) 
   random.shuffle(indexed_content)

   for i,ques in indexed_content:
       print(f"\n{ques}")
       user_ans = input("Enter your answer A/B/C/D :").upper()
       if user_ans == dbms_qans[i]:
           dbms_score +=1
      
   score[logged_user][1] =dbms_score
   dt_details =datetime.datetime.now()
   dt_details = dt_details.strftime("%d-%m-%Y ,%H:%M:%S")
   dt[logged_user][1] =dt_details
   

def python_quiz(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
   
   python_score =0 
   file =open("python.txt", "r") 
   content = file.read().strip().split("\n\n")
   indexed_content = list(enumerate(content)) 
   random.shuffle(indexed_content)

   for i,ques in indexed_content:
       print(f"\n{ques}")
       user_ans = input("Enter your answer A/B/C/D :").upper()
       if user_ans == python_qans[i]:
           python_score +=1
       
   score[logged_user][2] =python_score 
   dt_details =datetime.datetime.now()
   dt_details = dt_details.strftime("%d-%m-%Y ,%H:%M:%S")
   dt[logged_user][2] =dt_details
   


def user_score(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
    
    print(f"\nEnrollment no: {enrollment_no[logged_user]}")
    print("Category :DSA",end= "")
    if dt[logged_user][0] ==0:
        print(", Not Attempted yet")
    else:
        print(f", Score :{score[logged_user][0]} /5 {dt[logged_user][0]}")    


    print("Category :DBMS",end= "")
    if dt[logged_user][1] ==0:
        print(", Not Attempted yet")
    else:
        print(f", Score :{score[logged_user][1]} /5 {dt[logged_user][1]}")   

    print("Category :Python",end= "")
    if dt[logged_user][2] ==0:
        print(", Not Attempted yet")
    else:
        print(f", Score :{score[logged_user][2]} /5 {dt[logged_user][2]}")           
     


def users_scores(admin,logged,logged_user,names,enrollment_no,branches,year,phone_no,usernames,passwords,mail_id,score,dt):
     
      for uname in usernames:
          if uname == admin:
            continue
          
          else:

            print(f"\nEnrollment no: {enrollment_no[uname]}")
            print("Category :DSA",end= "")
            if dt[uname][0] ==0:
                print(", Not Attempted yet")
            else:
                print(f", Score :{score[uname][0]} /5 {dt[uname][0]}")    

            print("Category :DBMS",end= "")
            if dt[uname][1] ==0:
                print(", Not Attempted yet")
            else:
                print(f", Score :{score[uname][1]} /5 {dt[uname][1]}")   

            print("Category :Python",end= "")
            if dt[uname][2] ==0:
                print(", Not Attempted yet")
            else:
                print(f", Score :{score[uname][2]} /5 {dt[uname][2]}")   
               
            