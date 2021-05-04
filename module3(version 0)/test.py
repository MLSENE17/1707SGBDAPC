import mysql.connector as db
try:
    conn= db.connect(host= "localhost",
                    user="admin_CovidModeler",
                    password="dic2tr",
                    database="covidModeler")
            

except db.errors.InterfaceError as e:
    print("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)
def GetDict(obj):
    dictRegion={}
    for val in obj:
        if val["nbrCas"] ==None:
            dictRegion[val["nom_localite"]]=0
        else:
            dictRegion[val["nom_localite"]]=int(val["nbrCas"])
    return dictRegion

curseur=conn.cursor(dictionary=True)
req= """SELECT R.nom_localite, nbrCas FROM (SELECT D.region_id, SUM(nbre_cas) AS nbrCas FROM 
        (SELECT depart_id, nbre_cas FROM cas_localite WHERE date_communique< %s)SR NATURAL JOIN departement D GROUP BY(D.region_id))SSR
         RIGHT OUTER JOIN region R on R.region_id= SSR.region_id ORDER BY nbrCas DESC;"""

date=("2020-04-25", )
curseur.execute(req, date)
result= curseur.fetchall()
print(result)
region=GetDict(result)
print(region)