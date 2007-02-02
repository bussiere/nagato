from ZODB import FileStorage, DB 
import transaction

storage = FileStorage.FileStorage('bd/contact.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
k =  root.items()
for l in k :
    newuser = l[1]
    print newuser.notes
connection.close()