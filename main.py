from AddContacts import addContact
from SaveFile import saveFile
from ViewContacts import viewContacts
from RemoveContact import removeContact
from SearchContact import searchcontact
from UpdateContact import updatecontact
from RestoredData import restoredData
from DeleteFileData import deleteFileData
saveContact=[]
FileName="ContactHistory.csv"
def contactManagement(option):
    match option:
      case 1:
            addContact(saveContact,FileName)
            saveFile(FileName,saveContact)
      case 2:
            viewContacts(FileName)
      case 3:
            removeContact(saveContact,FileName)
      case 4:
            searchcontact(saveContact)
      case 5:
            updatecontact(saveContact)
            saveFile(FileName,saveContact)
      case 6:
              deleteFileData(saveContact)
              saveFile(FileName,saveContact)
      case _:
              print("Number Not Between 1 and 6! plz enter the right number")             

restoredData(saveContact,FileName)

while True:

      

    print("\t\tContact Book Management System"
          "\n"
          "\n\t1. Add Contacts \t2. View Contacts"
          "\n\t3. Remove Contact \t4. Search Contacts"
          "\n\t5. Update Contact \t6. Delete All Data From File"
          "\n\t0. Exit")
    option=int(input("=>> Enter Your Choice: "))
    if(option==0):
        print("Thanks For Using Contact Management System. Have A Nice Day.....")
        break
    contactManagement(option)