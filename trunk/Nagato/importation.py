import csv,fileinput,glob,string,os,unicodedata,sys
from ZODB import FileStorage, DB 
import transaction,re
from persistent import Persistent
from manage import User

fichA= "clients.csv"
cr1 = csv.reader(open(fichA),delimiter=";")


 


storage = FileStorage.FileStorage('bd/contact.fs')
db = DB(storage)
connection = db.open()
root = connection.root()





ligne = ""
for row in  cr1:
        newuser = User() 
        compteur = 0
        for case in row :
            transaction.commit()
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
        k = root.items()
        transaction.commit()
        newuser.id = len(k)
        transaction.commit()
        newuser._p_changed = 1
        root[newuser.id] = newuser
        transaction.commit()
        del newuser
        

connection.close()

print 'FINIT'
choix = raw_input("FINIT")


