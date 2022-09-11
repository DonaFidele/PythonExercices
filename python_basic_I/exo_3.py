#coding:utf-8
#Write a Python program to display the current date and time.

import datetime,time
#print(datetime.date.today())

jours={'Monday':'lundi', 'Tuesday':'mardi','Wednesday':'mercredi','Thursday':'jeudi','Friday':'vendredi','Saturday':'samedi','Sunday':'dimanche'}
mois={'January':'Janvier', 'February':'Février','March':'Mars','April':'Avril','May':'Mai','June':'Juin','July':'Juillet','August':'Août','September':'Septembre','October':'Octobre','November':'Novembre'}
print("On est le " + jours[time.strftime("%A")] ,time.strftime("%d"),mois[time.strftime("%B")] , time.strftime("%Y ") + "et il est" + time.strftime(" %H:%M:%S"))
