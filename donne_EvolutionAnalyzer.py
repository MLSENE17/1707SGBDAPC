import mysql.connector as db
import sys


def dbConnect():
    try:
        conn= db.connect(host= "localhost",
                        user="admin_CovidModeler",
                        password="dic2tr",
                        database="covidModeler")
                

    except db.errors.InterfaceError as e:
        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)
    return conn

def dicoRegion_Departement():
    conn=dbConnect()
    curseur= conn.cursor()
    request= """ SELECT R.nom_localite AS region, D.nom_localite AS departement, R.region_id
                FROM region R JOIN departement D ON R.region_id= D.region_id"""
    curseur.execute(request)
    result=curseur.fetchall()
    regions={}
    departements={}
    for val in result:
        regions.update({val[0] : val[2]})
        departements.update({val[1] : val[2]})
    
    return(regions, departements)

def nbrCasParMois(departement):
    conn=dbConnect()
    curseur= conn.cursor()
    request= """SELECT Date_format(date_communique, '%Y-%m') AS mois, (SUM(nbre_cas)*1000/population) AS cumul 
                FROM departement NATURAL JOIN cas_localite WHERE nom_localite LIKE %s GROUP BY mois;"""
    depart=(departement,)
    curseur.execute(request, depart)
    result=curseur.fetchall()
    nbrCas={}
    for val in result:
        if val[1] == None:
            nbrCas[val[0]] = 0
        else:
            nbrCas[val[0]] = float(val[1])

    return nbrCas
