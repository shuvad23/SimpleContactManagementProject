#update Values-------------------------------------------------------
def updatevalues(savedata,data):
    while True:
        try:
            lastName=input("=>Enter Your Last Name: ")
            firstName=input("=>Enter Your First Name: ")
            dateOfBirth=input("=>Enter Your Date Of Birth: ")
            address=input("=>Enter Your Address: ")
            data['Last Name']=lastName
            data['First Name']=firstName
            data['Date Of Birth']=dateOfBirth
            data['Address']=address
            break
        except ValueError:
            print("Last Name,First Name,Date of Birth and Email must be String.Plz enter the correct datatype....")
    while True:
        try:#same email(not allowed)---------------------------------------------------------
            while True:
                email=input("=>Enter Your Email-Address: ")
                emailAddress=""
                if savedata==[]:
                    emailAddress=email
                    data['Email Address']=email
                    break
                
                for i in savedata:
                    if email== i['Email Address']:
                        print("The Email-Address  is Already registered."
                              "Plz Enter the Email-Address.....................!!")
                        emailAddress=""
                        break
                    else:
                        emailAddress=email
                if(emailAddress==email):
                    data['Email Address']=email
                    break
            break
        except ValueError:
            print("Email must be String.plz enter the string value..........................")

    #Password--------------------------------
    while True:
        try:
            password=input("=>Enter Your Password: ")
            result=bool
            for i in password:
                if i in ['!','@','#','&','$']:
                    result=True
            if(result==True):
                data['Password']=password
                break
            else:
                print("Password must be Special-Character."
                      "Plz enter minimum one special-character in your password...")
        except ValueError:
            print("Password must be character,integer,special character.plz enter your password again.......")
    
    #National-ID-------------------------------------------------
    while True:
        try :#same ID(not allowed)-----------------------
            while True:
                ID=int(input("=>Enter Your National ID Number: "))
                nationalID=0
                if savedata==[]:
                    nationalID=ID
                    data['National-ID']=ID
                    break
                
                for i in savedata:
                    if ID== i['National-ID']:
                        print("The NID  is Already registered."
                              "Plz Enter the New Number.....................!!")
                        nationalID=0
                        break
                    else:
                        nationalID=ID
                if(nationalID==ID):
                    data['National-ID']=ID
                    break
            break
        except ValueError:
            print("The National-ID must be an integer.Plz enter the correct datatype....")
    
    #ContactNumber------------------------------------------------------
    while True:
        try :#same Number(not allowed)--------------------------
            while True:
                Number=int(input("=>Enter Your Contact-Number: "))
                contactNumber=0
                if savedata==[]:
                    contactNumber=Number
                    data['Contact-Number']=Number
                    break
                
                for i in savedata:
                    if Number== i['Contact-Number']:
                        print("The Number is Already registered."
                              "Plz Enter the New Number.....................!!")
                        contactNumber=0
                        break
                    else:
                        contactNumber=Number
                if(contactNumber==Number):
                    data['Contact-Number']=Number
                    break
            break
        except ValueError:
            print("The Contact-Number must be an integer.Plz enter the correct datatype....")

#Update Contact-------------------------------------------------------------------------- 
def updatecontact(savedata):
    email=input("=> Plz Enter Your Email-Address: ")
    password=input("=> Plz Enter Your Password: ")
    breakPointermain=0
    for datalist in savedata:
        if (email==datalist['Email Address'] and password==datalist['Password']):
            print("You are LogIn Successfully!-----")
            print("\n\tUpdate Contact: ")
            breakPointermain=0
            contact=int(input("=>Plz Enter Your Updating Contact-Number: "))
            breakPointer=0
            for data in savedata:
                if(contact==data['Contact-Number']):
                    breakPointer=0
                    updatevalues(savedata,data)
                    print("Contact Update Successfully!...............................")
                    break
                else:
                    breakPointer=1
            if(breakPointer==1):
                print("The Number Not avilable in the Database.....................")
            break
        else:
            breakPointermain=1
    if(breakPointermain==1):
        print("The Email and Password not match.Plz try again.......................")
    