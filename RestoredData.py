def restoredData(savecontact,fileData):
    with open('ContactHistory.csv','r') as fp:
        for line in fp.readlines():
            coloumData = line.strip().split(",")
            dicValue={
                    "Last Name":coloumData[0],
                    "First Name":coloumData[1],
                    "Date Of Birth":coloumData[2],
                    "Address":coloumData[3],
                    "Email Address":coloumData[4],
                    "Password":coloumData[5],
                    "National-ID":int(coloumData[6]),
                    "Contact-Number":int(coloumData[7]),
                }
            
            savecontact.append(dicValue) 

