#!/usr/bin/env python
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)
from persistent import Persistent
class User(Persistent):
    def __init__(self):
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


if __name__ == "__main__":
    
    execute_manager(settings)
