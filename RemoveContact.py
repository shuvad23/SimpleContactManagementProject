def removeContact(savedata,filename):
        email=input("Enter Your Email-Address: ")
        password=input("Enter Your Password: ")
        breakPointerMain=0
        for data in savedata:
            if (email==data['Email Address'] and password==data['Password']):
                print("You are LogIn Successfully!-----")
                print("\n\tRemove Contact: ")
                breakPointerMain=0
                contact=int(input("Plz Enter Your Removing Contact-Number: "))
                breakPointer=0
                for datalist in savedata:
                    if(contact==datalist['Contact-Number']):
                        breakPointer=0
                        savedata.remove(datalist)
                        with open(filename,'w') as f:
                            for data in savedata:
                                f.write(f'{data["Last Name"]},{data["First Name"]},{data["Date Of Birth"]},{data["Address"]},{data["Email Address"]},{data["Password"]},{data["National-ID"]},{data["Contact-Number"]}\n')
                            print("\nContact Removed Successfully!........................................")
                    else:
                         breakPointer=1

                if(breakPointer==1):
                     print("The Number Not avilable in the Database.....................")
                break
            else:
                 breakPointerMain=1
        if(breakPointerMain==1):
             print("The Email and Password not match.Plz try again.......................")
        
        