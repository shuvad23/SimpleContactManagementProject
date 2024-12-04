def viewContacts(fileName):
    print("------------------------------------------------------------------------------------------------")
    print("Last Name , First Name,Date Of Birth,Address,Email Address,Password ,National-ID,Contact-Number")
    with open(fileName,'r') as f:
        readData=f.read()
        print(readData)
    print("------------------------------------------------------------------------------------------------")