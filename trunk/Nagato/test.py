from django.http import HttpResponse
from ZODB import FileStorage, DB 
import transaction,re
from persistent import Persistent
import logging
from ZEO import ClientStorage
logging.getLogger("ZODB.FileStorage").setLevel(10000000)
logging.getLogger("ZODB.lock_file").setLevel(10000000)
logging.getLogger("ZODB.Connection").setLevel(10000000) 


class User(Persistent):
     pass

addr = '192.168.1.201', 8000
storage = ClientStorage.ClientStorage(addr)
db = DB(storage)
connection = db.open()
root = connection.root()
k = root.items()
print root[220]
test = """
for l in k :
   print l[1].id
   print l[1].societe
   print l[1].ad1
   print l[1].ad2
   print l[1].prenom
   print l[1].nom
   print l[1].cp
   print l[1].ville
   print "***************************" 
   """
connection.close()