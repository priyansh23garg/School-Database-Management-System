
import mysql.connector as co
def STU_MENU():
    while True:
        #student_data.clrScreen()
        print("\t\t.............................................")
        print("\n\t\t*****Student Data Menu*****")
        print("1:Add Student Record")
        print("2:Show Student Details")
        print("3:Search Student Record")
        print("4:Delete Student Records")
        print("5:Edit Student Records")
        print("6:Exit")
        print("\t\t--------------------------------------------")
        choice=int(input("Enter your choice:"))
        if choice==1:
            Add_Records()
        elif choice==2:
           Show_Stu_Details()
        elif choice==3:
          Search_Stu_Details()
        elif choice==4:
           Delete_Stu_Details()
        elif choice==5:
           Edit_Stu_Details()
        elif choice==6:
            return
        else:
            print("Error:Invalid Choice try again...")
            conti="Press any key to return to Main Menu"
def Add_Records():
        mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
        cursor=mycon.cursor()
        session=input("Enter academic session(eg,2020-21):")
        stname=input("Enter Student Name:")
        stclass=input("Enter class:")
        stsec=input("Enter Sec:")
        adno=input("Enter Admission no.:")
        sub1=input("Enter subject1:")
        sub2=input("Enter subject2:")
        sub3=input("Enter subject3:")

        query="INSERT INTO student(session,stname,stclass,stsec,adno,sub1,sub2,sub3) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(session,stname,stclass,stsec,adno,sub1,sub2,sub3)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in student table")
def Show_Stu_Details():
       mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
       cursor=mycon.cursor()
       cursor.execute("select * from student")
       data = cursor.fetchall()
       for row in data:
          print(row)
def Search_Stu_Details():
       mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
       cursor=mycon.cursor()
       ac=input("Enter Admission no.")
       st="select * from student where adno='%s'"%(ac)
       cursor.execute(st)
       data = cursor.fetchall()
       print(data)
def Delete_Stu_Details():
       mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
       cursor=mycon.cursor()
       ac=input("Enter Admission no.")
       st="delete from student where adno='%s'"%(ac)
       cursor.execute(st)
       mycon.commit()
       print('Data deleted successfully')
def Edit_Stu_Details():
     mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
     cursor=mycon.cursor()
     print("1:Edit session")
     print("2:Edit name")
     print("3:Edit class")
     print("4:Edit section")
     print("5:Edit Admission no.")
     print("6:Edit sub1")
     print("7:Edit sub2")
     print("8:Edit sub3") 
     print("9:Return")
     print("\t\t----------------------------------------------------------")
     choice=int(input("Enter your choice"))
     if choice==1:
         edit_session()
     elif choice==2:
        edit_name()
     elif choice==3:
        edit_class()
     elif choice==4:
        edit_sec()
     elif choice==5:
        edit_adno()
     elif choice==6:
        edit_sub1()
     elif choice==7:
        edit_sub2()
     elif choice==8:
        edit_sub3()
     elif choice==9:
        return
     else:
        print("Error:Invalid choice try again...")
        Edit_Stu_Details()
def edit_name():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no.:")
    nm=input("Enter correct name:")
    st="update student set stname='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_session():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no.:")
    nm=input("Enter correct session:")
    st="update student set session='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_class():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no.:")
    nm=input("Enter correct class:")
    st="update student set stclass='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_sec():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no.:")
    nm=input("Enter correct section:")
    st="update student set stsec='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_adno():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no.:")
    nm=input("Enetr correct roll no.:")
    st="update student set stroll='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_sub1():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enetr Admission no.:")
    nm=input("Enter correct sub1:")
    st="update student set sub1='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_sub2():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no.:")
    nm=input("Enter correct sub1:")
    st="update student set sub2='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_sub3():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no.:")
    nm=input("Enter correct sub3:")
    st="update student set sub3='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
    
    
         
        
