
import admission
import student_data
import fees
s=True
while s:
    #main_menu.clrscreen()
    print("\t\t............................................")
    print("\t\t*****Welcome to School Managment System*****")
    print("\t\t............................................")
    print("\n\t\t*****JAI ACADMEY SCHOOL*****")
    print("1:Admission")
    print("2:Student Data")
    print("3:Fees")
    print("4:Exit")
    print("\t\t--------------------------------------------")
    choice=int(input("Enter your choice:"))
    if choice==1:
        admission.ADM_MENU()
    elif choice==2:
        student_data.STU_MENU()
    elif choice==3:
        fees.FEES_MENU()
    elif choice==4:
         s=False
    else:
        print("Invalid Choice")
        conti=input("Press any key to continue")
        
        
        
