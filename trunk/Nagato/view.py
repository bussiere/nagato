#! /usr/bin/env python
# *-* coding: iso-8859-1 *-* 
from manage import User
from django.http import HttpResponse
from ZODB import FileStorage, DB 
import transaction,re
from persistent import Persistent
import logging
import string
from ZEO import ClientStorage
logging.getLogger("ZODB.FileStorage").setLevel(10000000)
logging.getLogger("ZODB.lock_file").setLevel(10000000)
logging.getLogger("ZODB.Connection").setLevel(10000000) 






def carnet(request):
    
    html = """<html><body><table width=100% height=100% align="center" valign="top">
        <tr width=100% height=100% align="center" valign="top">
        <td width=100% height=100% align="center" valign="top">
        <a href="rajouter">Rajouter un contact</A>
        <a href="mas">Modifier / Supprimer un contact</a>
        <a href="chercher">Chercher un contact</a>
        <a href="sync">Synchroniser le carnet d'adresse</a>
        </td>
        </tr>
        </table></body></html>"""
    return HttpResponse(html)

def rajouter(request):
        html = """<html><body>
        <a href="../">Retour</A><br>
        rajouter un contact
                <form action="rajoutercontact/" method="post"> 
        <table><tr><td>
        <p>Societe</p> 
              <input type="text" name="societe"    size="35" maxlength="40"/></td> <td>
        <p>Fonction</p> 
              <input type="text" name="fonction"    size="35" maxlength="40"/></td></tr>
        <tr>
         <td><p>Civ</p> 
         <input type="text" name="civ"    size="35" maxlength="40"/> </td>
        <td><p>Nom</p> 
              <input type="text" name="nom"    size="35" maxlength="40"/> </td> 
        <td><p>Prenom</p> 
         <input type="text" name="prenom"    size="35" maxlength="40"/> </td> </tr>
         <tr><td><p>AD1</p> 
              <input type="text" name="ad1"    size="38" maxlength="40"/> </td> 
         <td><p>AD2</p> 
              <input type="text" name="ad2"    size="38" maxlength="40"/></td> 
              <td><p>AD3</p> 
              <input type="text" name="ad3"    size="38" maxlength="40"/></td>
         <td><p>AD4</p> 
              <input type="text" name="ad4"    size="38" maxlength="40"/></td> </tr>
        <tr><td><p>CP</p> 
              <input type="text" name="cp"    size="38" maxlength="40"/> </td> 
        <td><p>VILLE</p> 
              <input type="text" name="ville"    size="38" maxlength="40"/> </td> </tr>
        <tr><td> <p>MAIL1</p> 
              <input type="text" name="mail1"    size="38" maxlength="40"/> </td> 
        <td><p>Mail2</p> 
              <input type="text" name="mail2"    size="38" maxlength="40"/> </td> </tr>
       <tr> <td><p>TEL1</p> 
              <input type="text" name="tel1"    size="15" maxlength="40"/>  </td> 
        <td><p>TEL2</p> 
              <input type="text" name="tel2"    size="15" maxlength="40"/> </td> </tr>
         <tr><td><p>PORTABLE1</p> 
              <input type="text" name="portable1"    size="15" maxlength="40"/></td> 
           <td><p>PORTABLE2</p> 
              <input type="text" name="portable2"    size="15" maxlength="40"/> </td></tr> 
          <tr><td><P>Anniversaire</p>
          <SELECT NAME=annijour>
<OPTION>1
<OPTION>2
<OPTION>3
<OPTION>4
<OPTION>5
<OPTION>6
<OPTION>7
<OPTION>8
<OPTION>9
<OPTION>10
<OPTION>11
<OPTION>12
<OPTION>13
<OPTION>14
<OPTION>15
<OPTION>16
<OPTION>17
<OPTION>18
<OPTION>19
<OPTION>20
<OPTION>21
<OPTION>22
<OPTION>23
<OPTION>24
<OPTION>25
<OPTION>26
<OPTION>27
<OPTION>28
<OPTION>29
<OPTION>30
<OPTION>31
</SELECT> 
<SELECT NAME=annimois>
<OPTION>janvier
<OPTION>fevrier
<OPTION>mars
<OPTION>avril
<OPTION>mai
<OPTION>juin
<OPTION>juillet
<OPTION>aout
<OPTION>septembre
<OPTION>octobre
<OPTION>novembre
<OPTION>decembre
</SELECT> 
              <input type="text" name="anniannee"    size="15" maxlength="40"/> </td> </tr>
         <tr><td colspan="2"> <p>Notes</p> 
              <TEXTAREA NAME="notes" ROWS=8 COLS=50></TEXTAREA>
               </td> </tr>
              </table>
        <p><input type="submit" value="Valider"/></p> 
        <p><input type="reset" value="Effacer"/></p> 
    </form> 
Importer un fichier csv.
        </body></html>"""
        return HttpResponse(html)
    
def rajoutercontact(request):

    newuser2 = User() 
    addr = '192.168.1.201', 8000
    storage = ClientStorage.ClientStorage(addr)
    db2 = DB(storage2)
    connection2 = db2.open()
    root2 = connection2.root()
    k = root2.items()
    newuser2.id = len(k)
    newuser2.societe = string.upper(request.POST['societe'])
    newuser2.fonction = string.upper(request.POST['fonction'])
    newuser2.civ = string.upper(request.POST['civ'])
    newuser2.nom = string.upper(request.POST['nom'])
    newuser2.prenom = string.upper(request.POST['prenom'])
    newuser2.ad1 = string.upper(request.POST['ad1'])
    newuser2.ad2 = string.upper(request.POST['ad2'])
    newuser2.ad3 = string.upper(request.POST['ad3'])
    newuser2.ad4 = string.upper(request.POST['ad4'])
    newuser2.cp = string.upper(request.POST['cp'])
    newuser2.ville = string.upper(request.POST['ville'])
    newuser2.mail1 = string.upper(request.POST['mail1'])
    newuser2.mail2 = string.upper(request.POST['mail2'])
    newuser2.tel1 = string.upper(request.POST['tel1'])
    newuser2.tel2 = string.upper(request.POST['tel2'])
    newuser2.portable1 = string.upper(request.POST['portable1'])
    newuser2.portable2 = string.upper(request.POST['portable2'])
    newuser2.annijour = string.upper(request.POST['annijour'])
    newuser2.annimois = string.upper(request.POST['annimois'])
    newuser2.anniannee = string.upper(request.POST['anniannee'])
    newuser2.notes = string.upper(request.POST['notes'])
    transaction.commit()
    newuser2.id = len(k)
    transaction.commit()
    newuser2._p_changed = 1
    root2[newuser2.id] = newuser2
    print root2[newuser2.id].id
    print root2[newuser2.id]
    transaction.commit()
    connection2.close()
    html = """<html><body>
        <a href="../">Retour</A><br>
Contact rajouté.
        </body></html>"""
    return HttpResponse(html)
    
def rechercher(request):
    logging.getLogger("ZODB.FileStorage").setLevel(10000000)
    logging.getLogger("ZODB.lock_file").setLevel(10000000)
    logging.getLogger("ZODB.Connection").setLevel(10000000) 
    html = """<html><body>
        <a href="../">Retour</A><br>
        """
    addr = '192.168.1.201', 8000
    storage = ClientStorage.ClientStorage(addr)
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    transaction.commit()
    k = root.items()
    listec = []
    recherche = string.upper(request.POST['recherche'])
    for l in k :
        if request.POST['rechercheb'] == "9":
            if re.search(recherche,l[1].societe) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "8":
            if re.search(recherche,l[1].fonction) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "1":
            if re.search(recherche,l[1].nom) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "5":
            if re.search(recherche,l[1].prenom) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "6":
            if re.search(recherche,l[1].ad1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "4":
            if re.search(recherche,l[1].ad2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "19":
            if re.search(recherche,l[1].ad3) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "2":
            if re.search(recherche,l[1].ad4) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "15":
            if re.search(recherche,l[1].cp) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "10":
            if re.search(recherche,l[1].ville)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "3":
            if re.search(recherche,l[1].mail1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "0":
            if re.search(recherche,l[1].mail2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "11":
            if re.search(recherche,l[1].tel1) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "12":
            if re.search(recherche,l[1].tel2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "17":
            if re.search(recherche,l[1].portable1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "16":
            if re.search(recherche,l[1].portable2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "14":
            anniversaire = "%s/%s/%s"%(l[1].annijour,l[1].annimois,l[1].anniannee)
            if anniversaire == recherche :
                listec.append(l[1])
        if request.POST['rechercheb'] == "7":
            if re.search(recherche,l[1].notes)  :
                listec.append(l[1])
    transaction.commit()
    connection.close()          
    html = html + """<table ><tr><td>Societe</td><td>fonction</td><td>Civ</td><td>Nom</td><td>Prenom</td><td>Ad1</td><td>Ad2</td><td>Ad3</td><td>Ad4</td><td>Cp</td><td>Ville</td><td>Mail1</td><td>Mail2</td><td width=100%>Tel1</td><td>Tel2</td><td>Portable1</td><td>POrtable2</td><td>Societe</td><td>Anniversaire</td><td>Notes</td></tr>"""
    for contact in listec :
        
        html = html + """<tr><td>%s</td><td> %s </td><td>%s</td><td> %s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s</td><td><a href="mailto:%s">%s</a> </td><td>  %s</td><td> %s </td><td>%s</td><td> %s </td><td>%s</td><td>%s %s %s</td><td> %s</td></tr>\n""" %(contact.societe,contact.fonction,contact.civ,contact.nom,contact.prenom,contact.ad1,contact.ad2,contact.ad3,contact.ad4,contact.cp,contact.ville,contact.mail1,contact.mail1,contact.mail2,contact.tel1,contact.tel2,contact.portable1,contact.portable2,contact.annijour,contact.annimois,contact.anniannee,contact.notes)
        
    html = html + "</table></body></html>"
    return HttpResponse(html)

def chercher(request):
        logging.getLogger("ZODB.FileStorage").setLevel(10000000)
        logging.getLogger("ZODB.lock_file").setLevel(10000000)
        logging.getLogger("ZODB.Connection").setLevel(10000000) 
        html = """
        <a href="../">Retour</A><br>
       Chercher
        <form action="rechercher/" method="post">
        <table><tr><td>
<INPUT TYPE=radio NAME=rechercheb VALUE="9" CHECKED>Societe<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="8">fonction<br>
</TD><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="1">Nom<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="5">Prenom<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="6">ad1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="4">ad2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="19">ad3<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="2">ad4<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="15">cp<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="10">ville<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="3">mail1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="0">mail2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="11">tel1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="12">tel2<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="17">portable1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="16">portable2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="14">anniversaire<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="7">note<br>
</td>
</tr>
</table><br>
<p>Chercher</p> 
              <input type="text" name="recherche"    size="35" maxlength="40"/></td> 
  <p><input type="submit" value="Valider"/></p> 
        <p><input type="reset" value="Effacer"/></p>
</form>
        """
        return HttpResponse(html)
    
    
def mas(request):
    html = """
        <a href="../">Retour</A><br>
       Mettre a jour
        <form action="chermaj/" method="post">
        <table><tr><td>
<INPUT TYPE=radio NAME=rechercheb VALUE="9" CHECKED>Societe<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="8">fonction<br>
</TD><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="1">Nom<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="5">Prenom<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="6">ad1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="4">ad2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="19">ad3<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="2">ad4<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="15">cp<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="10">ville<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="3">mail1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="0">mail2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="11">tel1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="12">tel2<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="17">portable1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="16">portable2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE="14">anniversaire<br>
<INPUT TYPE=radio NAME=rechercheb VALUE="7">note<br>
</td>
</tr>
</table><br>
<p>Chercher</p> 
              <input type="text" name="recherche"    size="35" maxlength="40"/></td> 
  <p><input type="submit" value="Valider"/></p> 
        <p><input type="reset" value="Effacer"/></p>
</form>
        """
    return HttpResponse(html)

def chermaj(request):

    
    logging.getLogger("ZODB.FileStorage").setLevel(10000000)
    logging.getLogger("ZODB.lock_file").setLevel(10000000)
    logging.getLogger("ZODB.Connection").setLevel(10000000) 
    html = """<html><body>
        <a href="../">Retour</A><br>
        """
    addr = '192.168.1.201', 8000
    storage = ClientStorage.ClientStorage(addr)
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    transaction.commit()
    k = root.items()
    listec = []
    recherche = string.upper(request.POST['recherche'])
    for l in k :
        if request.POST['rechercheb'] == "9":
            if re.search(recherche,l[1].societe) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "8":
            if re.search(recherche,l[1].fonction) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "1":
            if re.search(recherche,l[1].nom) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "5":
            if re.search(recherche,l[1].prenom) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "6":
            if re.search(recherche,l[1].ad1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "4":
            if re.search(recherche,l[1].ad2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "19":
            if re.search(recherche,l[1].ad3) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "2":
            if re.search(recherche,l[1].ad4) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "15":
            if re.search(recherche,l[1].cp) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "10":
            if re.search(recherche,l[1].ville)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "3":
            if re.search(recherche,l[1].mail1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "0":
            if re.search(recherche,l[1].mail2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "11":
            if re.search(recherche,l[1].tel1) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "12":
            if re.search(recherche,l[1].tel2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "17":
            if re.search(recherche,l[1].portable1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "16":
            if re.search(recherche,l[1].portable2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "14":
            anniversaire = "%s/%s/%s"%(l[1].annijour,l[1].annimois,l[1].anniannee)
            if anniversaire == recherche :
                listec.append(l[1])
        if request.POST['rechercheb'] == "7":
            if re.search(recherche,l[1].notes)  :
                listec.append(l[1])
    transaction.commit()
    connection.close()          
    html = html + """<form action="modif/" method="post"><table ><tr><td></td><td>Societe</td><td>fonction</td><td>Civ</td><td>Nom</td><td>Prenom</td><td>Ad1</td><td>Ad2</td><td>Ad3</td><td>Ad4</td><td>Cp</td><td>Ville</td><td>Mail1</td><td>Mail2</td><td width=100%>Tel1</td><td>Tel2</td><td>Portable1</td><td>POrtable2</td><td>Societe</td><td>Anniversaire</td><td>Notes</td></tr>"""
    for contact in listec :
        
        html = html + """<tr><td>
<INPUT TYPE=radio NAME=id VALUE="%s" ></td><td>%s</td><td> %s </td><td>%s</td><td> %s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s</td><td><a href="mailto:%s">%s</a> </td><td>  %s</td><td> %s </td><td>%s</td><td> %s </td><td>%s</td><td>%s %s %s</td><td> %s</td></tr>\n""" %(contact.id,contact.societe,contact.fonction,contact.civ,contact.nom,contact.prenom,contact.ad1,contact.ad2,contact.ad3,contact.ad4,contact.cp,contact.ville,contact.mail1,contact.mail1,contact.mail2,contact.tel1,contact.tel2,contact.portable1,contact.portable2,contact.annijour,contact.annimois,contact.anniannee,contact.notes)
        
    html = html + """</table><input type="submit" value="Modifier"/></form></body></html>"""
    return HttpResponse(html)


def modif(request):
    logging.getLogger("ZODB.FileStorage").setLevel(10000000)
    logging.getLogger("ZODB.lock_file").setLevel(10000000)
    logging.getLogger("ZODB.Connection").setLevel(10000000) 
    html = """<html><body>
        <a href="../">Retour</A><br>
        """
    addr = '192.168.1.201', 8000
    storage = ClientStorage.ClientStorage(addr)
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    transaction.commit()
    k = root.items()
    listec = []
    recherche = string.upper(request.POST['id'])
    for l in k :
        if re.search(recherche,l[1].id) :
                listec.append(l[1])