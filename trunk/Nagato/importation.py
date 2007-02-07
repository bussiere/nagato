import csv,fileinput,glob,string,os,unicodedata,sys
from ZODB import FileStorage, DB 
import transaction,re
from persistent import Persistent



fichA= "clients.csv"
cr1 = csv.reader(open(fichA),delimiter=";")
class User(Persistent):
    def __init__(self):
        self.id = ""

 
storage2 = FileStorage.FileStorage('bd/id.fs')
db2 = DB(storage2)
connection2 = db2.open()
root2 = connection2.root()
if not root2.has_key('userdb2'):
    from BTrees.OOBTree import OOBTree
    root2['userdb2'] = OOBTree()

userdb2 = root2['userdb2']

storage = FileStorage.FileStorage('bd/contact.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
if not root.has_key('userdb'):
    from BTrees.OOBTree import OOBTree
    root['userdb'] = OOBTree()

userdb = root['userdb']


newuser = User() 


ligne = ""
for row in  cr1:
        compteur = 0
        for case in row :
            
            newuser.notes = ""
            if compteur == 0 :
                newuser.notes += " %s " % case
            if compteur == 1 :
                newuser.societe = "%s" % case
                print newuser.societe
            if compteur == 2 :
                newuser.fonction = "%s" % case
            if compteur == 3 :
                newuser.civ = "%s" % case
            if compteur == 4 :
                newuser.prenom = "%s" % case
            if compteur == 5 :
                newuser.nom = "%s" % case
            if compteur == 6 :
                newuser.ad1 = "%s" % case
            if compteur == 7 :
                newuser.ad2 = "%s" % case
            if compteur == 8 :
                newuser.cp = "%s" % case
            if compteur == 9 :
                newuser.ville = "%s" % case
            if compteur == 10 :
                newuser.tel1 = "%s" % case
            if compteur == 11 :
                newuser.mail1 = "%s" % case
            if compteur == 12 :
                newuser.tel2 = "%s" % case
            if compteur == 13 :
                newuser.notes += " %s " % case
            if compteur == 14 :
                newuser.notes += " %s " % case
            compteur += 1
        k = root2.items()
        transaction.commit()
        newuser.id = len(k)
        print len(k)
        userdb2[newuser.id] = newuser.id
        transaction.commit()
        userdb[newuser.id] = newuser
        transaction.commit()
        print userdb2[newuser.id]
        print userdb[newuser.id].societe
        transaction.commit()
connection.close()
connection2.close()
print 'FINIT'
choix = raw_input("FINIT")


