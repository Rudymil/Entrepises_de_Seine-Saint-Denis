# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:17:32 2017

@author: Rudolf MILLET
"""

import psycopg2
import csv
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

        for row in reader:
            voirie = row[3]+" "+row[8]
            cur.execute("INSERT INTO bano_93 (voirie,codpos,libcom,lat,lon) VALUES("+voirie+","+row[3]+","+row[9]+","+row[6]+","+row[7]+")")

    finally:

        f_bano_93.close()

    try:

        reader = csv.reader(f_siren_93)

        for row in reader:
            cur.execute("INSERT INTO siren_93 (siren,l1_normalisee,l4_normalisee,codpos,libcom,libapet,libtefet,libnj) VALUES("+row[0]+","+row[2]+","+row[5]+","+row[20]+","+row[28]+","+row[43]+","+row[46]+","+row[71]+")")

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