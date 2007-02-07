from ZODB import FileStorage, DB 
import transaction
from persistent import Persistent
class User(Persistent):
    pass
              
storage = FileStorage.FileStorage('bd/contact.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

k =  root.items()
for l in k :
    newuser = l[1]
    print newuser.id
    print newuser.societe

connection.close()