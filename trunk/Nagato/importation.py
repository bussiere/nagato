import csv,fileinput,glob,string,os,unicodedata,sys
fichA= "clients.csv"
cr1 = csv.reader(open(fichA),delimiter=";")
class User(Persistent):
    pass

newuser = User() 
storage2 = FileStorage.FileStorage('bd/id.fs')
db2 = DB(storage)
connection2 = db2.open()
root2 = connection.root()


storage = FileStorage.FileStorage('bd/contact.fs')
db = DB(storage)
connection = db.open()
root = connection.root()




ligne = ""
for row in  cr1:
        compteur = 0
        for case in row :
            if compteur == 0 :
                newuser.notes += " %s " % case
            if compteur == 1 :
                newuser.societe = "%s" % case
            if compteur == 2 :
                newuser.fonction = "%s" % case
            if compteur == 3 :
                newuser.civ = "%s" % case
            if compteur == 4 :
                newuser.prenom = "%s" % case
                newuser.nom = request.POST['nom']
                newuser.ad1 = request.POST['ad1']
                newuser.ad2 = request.POST['ad2']
                newuser.ad3 = request.POST['ad3']
                newuser.ad4 = request.POST['ad4']
                newuser.cp = request.POST['cp']
                newuser.ville = request.POST['ville']
                newuser.mail1 = request.POST['mail1']
                newuser.mail2 = request.POST['mail2']
                newuser.tel1 = request.POST['tel1']
                newuser.tel2 = request.POST['tel2']
                newuser.portable1 = request.POST['portable1']
                newuser.portable2 = request.POST['portable2']
                newuser.annijour = request.POST['annijour']
                newuser.annimois = request.POST['annimois']
                newuser.anniannee = request.POST['anniannee']
            compteur += 1
        k = root2.items()
        newuser.id = len(k)
        root2[newuser.id] = newuser.id
        transaction.commit()
        root[newuser.id] = newuser
        transaction.commit()
connection.close()
connection2.close()
print 'FINIT'
choix = raw_input("FINIT")


