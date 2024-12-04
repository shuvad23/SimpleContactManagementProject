def deleteFileData(savedata):
      email=input("=>Enter Your Email-Address: ")
      password=input("=>Enter Your Password: ")
      breakPointerMain=0
      for datalist in savedata:
         if (email==datalist['Email Address'] and password==datalist['Password']):
            print("You are LogIn Successfully!-----")
            savedata.clear()
            print('\n')
            print("Deleted All File Data Successfully!............................")
         else:
             breakPointerMain=1
      if(breakPointerMain==1):
         print("The Email and Password not match.Plz try again.......................")

