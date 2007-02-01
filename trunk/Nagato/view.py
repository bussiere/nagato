from django.http import HttpResponse
from ZODB import FileStorage, DB 
import transaction
from persistent import Persistent



class User(Persistent):
    pass

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
        <tr><td><p>Nom</p> 
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
    societe = request.POST['societe']
    fonction = request.POST['fonction']
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    ad1 = request.POST['ad1']
    ad1 = request.POST['ad2']
    ad1 = request.POST['ad3']
    ad1 = request.POST['ad4']
    cp = request.POST['cp']
    ville = request.POST['ville']
    mail1 = request.POST['mail1']
    mail2 = request.POST['mail2']
    tel1 = request.POST['tel1']
    tel2 = request.POST['tel2']
    portable1 = request.POST['portable1']
    portable2 = request.POST['portable2']
    annijour = request.POST['annijour']
    annimois = request.POST['annimois']
    anniannee = request.POST['anniannee']
    html = "<html><body>%s %s</body></html>" % (societe,anniannee)
    return HttpResponse(html)
    
def rechercher(request):
    html = "<html><body>%s %s</body></html>" % (request.POST['recherche'],request.POST['rechercheb'])
    return HttpResponse(html)

def chercher(request):
        html = """
        <a href="../">Retour</A><br>
       Chercher
        <form action="rechercher/" method="post">
        <table><tr><td>
<INPUT TYPE=radio NAME=rechercheb VALUE=9>Societe<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=8>fonction<br>
</TD><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=1>Nom<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=5>Prenom<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=6>ad1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=4>ad2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=19>ad3<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=2>ad4<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=15>cp<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=10>ville<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=3>mail1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=0>mail2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=11>tel1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=12>tel2<br>
</td><TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=17>portable1<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=16>portable2<br>
</td>
<TD>
<INPUT TYPE=radio NAME=rechercheb VALUE=14>anniversaire<br>
<INPUT TYPE=radio NAME=rechercheb VALUE=7>note<br>
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
        <form action="chermaj" method="post">
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
