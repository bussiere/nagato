from ZODB import FileStorage, DB 
import transaction
from persistent import Persistent
import logging
logging.getLogger("ZODB.FileStorage").setLevel(10000000)
logging.getLogger("ZODB.lock_file").setLevel(10000000)
logging.getLogger("ZODB.Connection").setLevel(10000000) 


class User(Persistent):
    pass
              
storage = FileStorage.FileStorage('bd/contact.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

k =  root.items()
for l in k :
   print l[1].societe
   print l[1].ad1

connection.close()