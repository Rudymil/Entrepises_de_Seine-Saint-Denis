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
f_bano_93 = open(n_bano_93)
f_siren_93 = open(n_siren_93)

try:

    con = psycopg2.connect(host='localhost',dbname='Entreprises_de_Seine-Saint-Denis',user='postgres',password='postgres',port=5432)
    cur = con.cursor()

    try:

        reader = csv.reader(f_bano_93)
        exp = "([0-9]+)"

        for row in reader:
            
            #print(row)
            ligne = ";".join(row)
            #print(ligne)
            tableau = ligne.split(";")
            #print(tableau)

            if tableau[1].find("B") != -1: # si c est un BIS

                numero = re.findall(exp,tableau[1]) # extraction du numero
                adresse = numero[0]+" B "+tableau[8]+" "+tableau[3]+" "+tableau[9] # "numero B voie_maj code_post ville_maj"

            elif tableau[1].find("Q") != -1 and tableau[1].find("T") != -1: # sinon si c est un QUATER

                numero = re.findall(exp,tableau[1]) # extraction du numero
                adresse = numero[0]+" Q "+tableau[8]+" "+tableau[3]+" "+tableau[9] # "numero Q voie_maj code_post ville_maj"
                
            elif tableau[1].find("T") != -1: # sinon si c est un TER

                numero = re.findall(exp,tableau[1]) # extraction du numero
                adresse = numero[0]+" T "+tableau[8]+" "+tableau[3]+" "+tableau[9] # "numero T voie_maj code_post ville_maj"

            else: # sinon

                adresse = tableau[1]+" "+tableau[8]+" "+tableau[3]+" "+tableau[9] # "numero voie_maj code_post ville_maj"

            cur.execute("INSERT INTO bano_93 (adresse,the_geom) VALUES('"+adresse+"', ST_GeomFromText('POINT("+tableau[6]+" "+tableau[7]+")', 4326))")

    finally:

        f_bano_93.close()

    try:

        reader = csv.reader(f_siren_93)

        for row in reader:

            #print(row)
            ligne = ";".join(row)
            #print(ligne)
            tableau = ligne.split(";")
            #print(tableau)

            adresse = tableau[5]+" "+tableau[20]+" "+tableau[28] # "l4_normalisee codpos libcom"
            cur.execute("INSERT INTO siren_93 (siren,l1_normalisee,adresse,libapet,libtefet,libnj) VALUES('"+tableau[0]+"','"+tableau[2]+"','"+adresse+"','"+tableau[43]+"','"+tableau[46]+"','"+tableau[71]+"')")

    finally:

        f_siren_93.close()
    
    con.commit()

#except (psycopg2.DatabaseError, e):

    #if con:

        #con.rollback()

    #print ('Error %s' % e)    
    #sys.exit(1)

finally:

    if con:

        con.close()