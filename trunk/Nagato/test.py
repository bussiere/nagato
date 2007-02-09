from django.http import HttpResponse
from ZODB import FileStorage, DB 
import transaction,re
from persistent import Persistent
import logging
logging.getLogger("ZODB.FileStorage").setLevel(10000000)
logging.getLogger("ZODB.lock_file").setLevel(10000000)
logging.getLogger("ZODB.Connection").setLevel(10000000) 


class User(Persistent):
    def __init__(self):
            self.id = ""
            self.notes = ""
            self.societe = "" 
            self.fonction = "" 
            self.civ = "" 
            self.prenom = "" 
            self.nom = "" 
            self.ad1 = "" 
            self.ad2 = "" 
            self.cp = "" 
            self.ville = "" 
            self.tel1 = "" 
            self.mail1 = ""
            self.mail2 = ""
            self.portable1 = ""
            self.portable2 = ""
            self.tel2 = "" 
            self.notes = "" 

              
storage = FileStorage.FileStorage('bd/contact.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

k =  root.items()
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
connection.close()