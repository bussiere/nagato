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
print k
for l in k :
    print root[l[0]].societe

connection.close()