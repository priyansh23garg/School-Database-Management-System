
import mysql.connector as co
def ADM_MENU():
    while True:
        #admission.clrScreen()
        print("\t\t..............................................")
        print("\n\t\t*****Admission Menu*****")
        print("1:Add Admission Details")
        print("2:Show Admission Details")
        print("3:Search Admission Details")
        print("4:Deletion of records")
        print("5:Update Admission Details")
        print("6:Return")
        print("\t\t---------------------------------------------")
        choice=int(input("Enter your choice:"))
        if choice==1:
            admin_details()
        elif choice==2:
            show_admin_details()
        elif choice==3:
            search_admin_details()
        elif choice==4:
            delete_admin_details()
        elif choice==5:
            edit_admin_details()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice")
            conti=input("Press any key to continue")
def admin_details():
        mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
        cursor=mycon.cursor()
        adno=input("Enter Admission number:")
        rno=int(input("Enter Roll no:"))
        sname=input("Enter student name:")
        address=input("Enter address:")
        phon=input("Enter phone number:")
        clas=input("Enter class:")

        query="insert into admission(adno,rno,sname,address,phon,clas)values('{}',{},'{}','{}','{}','{}')".format(adno,rno,sname,address,phon,clas)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print('Record has been saved in admission table')
def show_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    cursor.execute("select * from admission")
    data=cursor.fetchall()
    for row in data:
       print(row)
def search_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission Number")
    st="select * from admission where adno='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    if(len(data)==0):
        print("No such records")
    else:
       print(data)
def delete_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input('Enter Admission Number')
    st="delete from admission where adno='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print("Data deleted successfully")
def edit_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()

    print("1:Edit name")
    print("2:Edit Address")
    print("3:Phone Number")
    print("4:Return")
    print("\t\t--------------------------------------")
    choice=int(input("Enter your choice:"))
    if choice==1:
        edit_name()
    elif choice==2:
        edit_address()
    elif choice==3:
        edit_phno()
    elif choice==4:
        return
    else:
        print("Error:Invalid Choice try again....")
        edit_admin_details()
def edit_name():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission Number:")
    nm=input("Enter correct name:")
    st="update admission set sname='%s'where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated sccessfully')
def edit_address():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission No.:")
    nm=input("Enter correct address:")
    st="update admission set address='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")
def edit_phno():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission No.:")
    nm=input("Enter correct phone number:")
    st="update admission set phon='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")
    
    
    
    
    
        
    
        
