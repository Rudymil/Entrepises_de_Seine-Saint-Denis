# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:17:32 2017

@author: Rudolf MILLET
"""

import psycopg2
import csv
import re # regular expression
import sys

con = None

n_bano_93 = "bano_93.csv"
n_siren_93 = "siren_93.csv"
f_bano_93 = open(n_bano_93,"rb")
f_siren_93 = open(n_siren_93,"rb")

try:

    con = psycopg2.connect(host='localhost',dbname='Entreprises_de_Seine-Saint-Denis',user='postgres',password='postgres',port=5432)
    cur = con.cursor()

    try:

        reader = csv.reader(f_bano_93)
        exp = "([0-9]+)"

        for row in reader:
            
            if row[1].find("B") != -1: # si c est un BIS
            
                numero = re.findall(exp,row[1]) # extraction du numero
                adresse = numero[0]+" B "+row[8]+" "+row[3]+" "+row[9] # "numero B voie_maj code_post ville_maj"
                
            elif row[1].find("T") != -1: # sinon si c est un TER
            
                numero = re.findall(exp,row[1]) # extraction du numero
                adresse = numero[0]+" T "+row[8]+" "+row[3]+" "+row[9] # "numero T voie_maj code_post ville_maj"
                
            elif row[1].find("Q") != -1: # sinon si c est un QUATER
                
                numero = re.findall(exp,row[1]) # extraction du numero
                adresse = numero[0]+" Q "+row[8]+" "+row[3]+" "+row[9] # "numero Q voie_maj code_post ville_maj"
                
            else: # sinon
            
                adresse = row[1]+" "+row[8]+" "+row[3]+" "+row[9] # "numero voie_maj code_post ville_maj"
                
            cur.execute("INSERT INTO bano_93 (adresse,lat,lon) VALUES("+adresse+","+row[6]+","+row[7]+")")

    finally:

        f_bano_93.close()

    try:

        reader = csv.reader(f_siren_93)

        for row in reader:
            
            adresse = row[5]+" "+row[20]+" "+row[28] # "l4_normalisee codpos libcom"
            cur.execute("INSERT INTO siren_93 (siren,l1_normalisee,adresse,libapet,libtefet,libnj) VALUES("+row[0]+","+row[2]+","+adresse+","+row[43]+","+row[46]+","+row[71]+")")

    finally:

        f_siren_93.close()

    con.commit()

except (psycopg2.DatabaseError, e):

    if con:
        
        con.rollback()

    print ('Error %s' % e)    
    sys.exit(1)
    
finally:

    if con:
        
        con.close()