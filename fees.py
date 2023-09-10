import mysql.connector as co
def FEES_MENU():
    while True:
        #fees.clrScreen()
        print("\t\t..............................................")
        print("\n\t\t*****Fees Menu*****")
        print("1:Add Fees Details")
        print("2:Show Fees Details")
        print("3:Search Fees Details")
        print("4:Deletion of records")
        print("5:Update Fees Details")
        print("6:Return")
        print("\t\t---------------------------------------------")
        choice=int(input("Enter your choice:"))
        if choice==1:
            add_fees_details()
        elif choice==2:
            show_fees_details()
        elif choice==3:
            search_fees_details()
        elif choice==4:
            delete_fees_details()
        elif choice==5:
            edit_fees_details()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice")
            conti=input("Press any key to continue")
def add_fees_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    session=input("Enter Session:")
    stclass=input("Enter Class:")
    stsec=input("Enter Section:")
    adno=input("Enter Admission number:")
    paymenttype=input("Enter Payment Mode:")
    amount=input("Enter Amount:")
    dat=input("Enter Date:")

    query="insert into fees(session,stclass,stsec,adno,paymenttype,amount,dat)values('{}','{}','{}','{}','{}','{}','{}')".format(session,stclass,stsec,adno,paymenttype,amount,dat)
    cursor.execute(query)
    mycon.commit()
    mycon.close()
    cursor.close()
    print("Record has been saved in fees table")
def show_fees_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    cursor.execute("select * from fees")
    data=cursor.fetchall()
    for row in data:
        print(row)
def search_fees_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission No.:")
    st="select * from fees where adno='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetcall()
    print(data)
def delete_fees_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission No.:")
    st="delete from fees where adno='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print("Data deleted successfully")
def edit_fees_details():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()

    print("1:Edit Session")
    print("2:Edit Class")
    print("3:Edit Section")
    print("4:Return")
    print("\t\t---------------------------------------")
    choice=int(input("Enter choice:"))
    if choice==1:
        edit_session()
    elif choice==2:
        edit_class()
    elif choice==3:
        edit_sec()
    elif choice==4:
        return
    else:
        print("Error:Invalid Coice try again....")
        edit_fees_details()
def edit_session():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission No.:")
    nm=input("Enter correct session:")
    st="update fees set session='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")
def edit_class():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission No.")
    nm=input("Enter correct class:")
    st="update fees set stclass='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")
def edit_sec():
    mycon=co.connect(host="localhost",user="root",passwd="giveaccess",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission No.:")
    nm=input("Enter correct section:")
    st="update fees set stsec='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")
    
    
