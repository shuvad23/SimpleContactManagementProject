def searchcontact(savedata):
      email=input("=>Enter Your Email-Address: ")
      password=input("=>Enter Your Password: ")
      breakPointerMain=0
      for datalist in savedata:
         if (email==datalist['Email Address'] and password==datalist['Password']):
            print("You are LogIn Successfully!-----")
            print("\n\tSearch Contact: ")
            breakPointerMain=0
            contact=int(input("=>Plz Enter Your Searching Contact-Number: "))
            breakPointer=0
            for data in savedata:
               if(contact==data['Contact-Number']):
                  breakPointer=0
                  print("-----------------------------------------------------------------")
                  print("Your Search Contact:.......")
                  print(f"Last Name: {data["Last Name"]}\nFirst Name: {data["First Name"]}\nDate of Birth: {data["Date Of Birth"]}\nAddress: {data["Address"]}\nEmail Address: {data["Email Address"]}\nPassword: {data["Password"]}\nNational-ID: {data["National-ID"]}\nContact-Number: {data["Contact-Number"]}")    
                  print("-----------------------------------------------------------------")
               else:
                     breakPointer=1
            if(breakPointer==1):
                print("The Number Not avilable in the Database")
                print("------------------------------------------------------------")
            break
         else:
             breakPointerMain=1
      if(breakPointerMain==1):
         print("The Email and Password not match.Plz try again.......................")

