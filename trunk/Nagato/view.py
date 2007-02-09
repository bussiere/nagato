#! /usr/bin/env python
# *-* coding: iso-8859-1 *-* 
from django.http import HttpResponse
from ZODB import FileStorage, DB 
import transaction,re
from persistent import Persistent
import logging
import string
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
            self.ad3 = "" 
            self.ad4 = "" 
            self.cp = "" 
            self.ville = "" 
            self.tel1 = "" 
            self.mail1 = ""
            self.mail2 = ""
            self.portable1 = ""
            self.portable2 = ""
            self.tel2 = "" 
            self.notes = "" 
            self.annijour = ""
            self.annimois = ""
            self.anniannee = ""
            self._p_changed = 1



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
    newuser = User() 
    storage = FileStorage.FileStorage('bd/contact.fs')
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    k = root.items()
    newuser.id = len(k)
    newuser.societe = request.POST['societe']
    newuser.fonction = request.POST['fonction']
    newuser.civ = request.POST['civ']
    newuser.nom = request.POST['nom']
    newuser.prenom = request.POST['prenom']
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
    newuser.notes = request.POST['notes']
    root[newuser.id] = newuser
    transaction.commit()
    connection.close()
    html = """<html><body>
        <a href="../">Retour</A><br>
Contact rajouté.
        </body></html>"""
    return HttpResponse(html)
    
def rechercher(request):
    html = """
        <a href="../">Retour</A><br>
        """
    storage = FileStorage.FileStorage('bd/contact.fs')
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    transaction.commit()
    k = root.items()
    transaction.commit()
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
    connection.close()           
    html = html + """<table ><tr><td>Societe</td><td>fonction</td><td>Civ</td><td>Nom</td><td>Prenom</td><td>Ad1</td><td>Ad2</td><td>Ad3</td><td>Ad4</td><td>Cp</td><td>Ville</td><td>Mail1</td><td>Mail2</td><td width=100%>Tel1</td><td>Tel2</td><td>Portable1</td><td>POrtable2</td><td>Societe</td><td>Anniversaire</td><td>Notes</td></tr>"""
    for contact in listec :
        
        html = html + """<tr><td>%s</td><td> %s </td><td>%s</td><td> %s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s </td><td>%s</td><td><a href="mailto:%s">%s</a> </td><td>  %s</td><td> %s </td><td>%s</td><td> %s </td><td>%s</td><td>%s %s %s</td><td> %s</td></tr>\n""" %(contact.societe,contact.fonction,contact.civ,contact.nom,contact.prenom,contact.ad1,contact.ad2,contact.ad3,contact.ad4,contact.cp,contact.ville,contact.mail1,contact.mail1,contact.mail2,contact.tel1,contact.tel2,contact.portable1,contact.portable2,contact.annijour,contact.annimois,contact.anniannee,contact.notes)
        
    html = html + "</table>"
    return HttpResponse(html)

def chercher(request):
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
        Mettre a jour / supprimer
        <form action="chermaj/" method="post">
        <table><tr><td>
<INPUT TYPE=checkbox NAME=Societe VALUE=Societe>Societe<br>
<INPUT TYPE=checkbox NAME=fonction VALUE=fonction>fonction<br>
</TD><TD>
<INPUT TYPE=checkbox NAME=Nom VALUE=Nom>Nom<br>
<INPUT TYPE=checkbox NAME=Prenom VALUE=Prenom>Prenom<br>
</td><TD>
<INPUT TYPE=checkbox NAME=ad1 VALUE=ad1>ad1<br>
<INPUT TYPE=checkbox NAME=ad2 VALUE=ad2>ad2<br>
</td>
<TD>
<INPUT TYPE=checkbox NAME=ad3 VALUE=ad3>ad3<br>
<INPUT TYPE=checkbox NAME=ad4 VALUE=ad4>ad4<br>
</td>
<TD>
<INPUT TYPE=checkbox NAME=cp VALUE=cp>cp<br>
<INPUT TYPE=checkbox NAME=villeVALUE=ville>ville<br>
</td><TD>
<INPUT TYPE=checkbox NAME=mail1 VALUE=mail1>mail1<br>
<INPUT TYPE=checkbox NAME=mail2 VALUE=mail2>mail2<br>
</td>
<TD>
<INPUT TYPE=checkbox NAME=tel1 VALUE=mail1>tel1<br>
<INPUT TYPE=checkbox NAME=tel2 VALUE=mail2>tel2<br>
</td><TD>
<INPUT TYPE=checkbox NAME=portable1 VALUE=mail1>portable1<br>
<INPUT TYPE=checkbox NAME=portable2 VALUE=mail2>portable2<br>
</td>
<TD>
<INPUT TYPE=checkbox NAME=anniversaire VALUE=mail1>anniversaire<br>
<INPUT TYPE=checkbox NAME=note VALUE=mail2>note<br>
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

    
    html = """
        <a href="../">Retour</A><br>
        """
    storage = FileStorage.FileStorage('bd/contact.fs')
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    k = root.items()
    transaction.commit()
    listec = []
    for l in k :
        if request.POST['rechercheb'] == "9":
            if re.search(request.POST['recherche'],l[1].societe) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "8":
            if re.search(request.POST['recherche'],l[1].fonction) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "1":
            if re.search(request.POST['recherche'],l[1].nom) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "5":
            if re.search(request.POST['recherche'],l[1].prenom) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "6":
            if re.search(request.POST['recherche'],l[1].ad1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "4":
            if re.search(request.POST['recherche'],l[1].ad2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "19":
            if re.search(request.POST['recherche'],l[1].ad3) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "2":
            if re.search(request.POST['recherche'],l[1].ad4) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "15":
            if re.search(request.POST['recherche'],l[1].cp) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "10":
            if re.search(request.POST['recherche'],l[1].ville)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "3":
            if re.search(request.POST['recherche'],l[1].mail1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "0":
            if re.search(request.POST['recherche'],l[1].mail2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "11":
            if re.search(request.POST['recherche'],l[1].tel1) :
                listec.append(l[1])
        if request.POST['rechercheb'] == "12":
            if re.search(request.POST['recherche'],l[1].tel2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "17":
            if re.search(request.POST['recherche'],l[1].portable1)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "16":
            if re.search(request.POST['recherche'],l[1].portable2)  :
                listec.append(l[1])
        if request.POST['rechercheb'] == "14":
            anniversaire = "%s/%s/%s"%(l[1].annijour,l[1].annimois,l[1].anniannee)
            if anniversaire == request.POST['recherche'] :
                listec.append(l[1])
        if request.POST['rechercheb'] == "7":
            if re.search(request.POST['recherche'],l[1].notes)  :
                listec.append(l[1])
    connection.close()      
    for contact in listec :
        html = html + "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s <br>" %(contact.societe,contact.fonction,contact.nom,contact.prenom,contact.ad1,contact.ad2,contact.ad3,contact.ad4,contact.cp,contact.ville,contact.mail1,contact.mail2,contact.tel1,contact.tel2,contact.portable1,contact.portable2,contact.annijour,contact.annimois,contact.anniannee)
    return HttpResponse(html)


