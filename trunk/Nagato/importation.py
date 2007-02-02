import csv,fileinput,glob,string,os,unicodedata,sys
fichA= "clients.csv"
cr1 = csv.reader(open(fichA),delimiter=";")


ligne = ""
for row in  cr1:     
        for case in row :
                ligne += " %s " % case
        ligne += "\n"
        print ligne
        ligne = ""

print 'FINIT'
choix = raw_input("FINIT")


