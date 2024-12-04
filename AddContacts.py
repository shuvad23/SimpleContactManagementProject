def addContact(savedata,filename):
    lastName=None
    firstName=None
    dateOfBirth=None
    address=None
    emailAddress=None
    password=None
    nationalID=None
    contactNumber=None
    #LastName,FirstName,DateOfBirth,EmailAddress------------------------------
    while True:
        try:
            lastName=input("=>Enter Your Last Name: ")
            firstName=input("=>Enter Your First Name: ")
            dateOfBirth=input("=>Enter Your Date Of Birth: ")
            address=input("=>Enter Your Address: ")
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
                    break
                
                for data in savedata:
                    if email== data['Email Address']:
                        print("The Email-Address  is Already registered."
                              "Plz Enter the Email-Address.....................!!")
                        emailAddress=""
                        break
                    else:
                        emailAddress=email
                if(emailAddress==email):
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
                IDi=int(input("=>Enter Your National ID Number: "))
                nationalID=0
                if savedata==[]:
                    nationalID=IDi
                    break
                
                for data1 in savedata:
                    if IDi== data1['National-ID']:
                        print("The NID  is Already registered."
                              "Plz Enter the New Number.....................!!")
                        nationalID=0
                        break
                    else:
                        nationalID=IDi
                if(nationalID==IDi):
                    break
            break
        except ValueError:
            print("The National-ID must be an integer.Plz enter the correct datatype....")
    
    #ContactNumber------------------------------------------------------
    while True:
        try :#same Number(not allowed)--------------------------
            while True:
                Number1=int(input("=>Enter Your Contact-Number: "))
                contactNumber=0
                if savedata==[]:
                    contactNumber=Number1
                    break        
                for data2 in savedata:
                    if Number1== data2['Contact-Number']:
                        print("The Number is Already registered."
                              "Plz Enter the New Number.....................!!")
                        contactNumber=0
                        break
                    else:
                        contactNumber=Number1
                if(contactNumber==Number1):
                    break
            break
        except ValueError:
            print("The Contact-Number must be an integer.Plz enter the correct datatype....")
    
    dicData={
        "Last Name":lastName,
        "First Name":firstName,
        "Date Of Birth":dateOfBirth,
        "Address":address,
        "Email Address":emailAddress,
        "Password":password,
        "National-ID":nationalID,
        "Contact-Number":contactNumber
    }

    # for i in [lastName,firstName,dateOfBirth,address,emailAddress,password,nationalID,contactNumber]:
    #     savedate.append(i)

    savedata.append(dicData)
    
    #save in a file-----------------------------------------------------------------------
    with open(filename,'w') as FileName:
        for data in savedata:
            FileName.write(f'{data["Last Name"]},{data["First Name"]},{data["Date Of Birth"]},{data["Address"]},{data["Email Address"]},{data["Password"]},{data["National-ID"]},{data["Contact-Number"]}\n')
    print("\n")
    print("Contact Added Successfully!--------------------------------")