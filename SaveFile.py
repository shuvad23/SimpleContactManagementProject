def saveFile(ContactFileName,savedata):
    with open(ContactFileName,'w') as FileName:
        for data in savedata:
            FileName.write(f'{data["Last Name"]},{data["First Name"]},{data["Date Of Birth"]},{data["Address"]},{data["Email Address"]},{data["Password"]},{data["National-ID"]},{data["Contact-Number"]}\n')
  