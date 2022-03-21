import mysql.connector
conn = mysql.connector.connect(host="localhost",user="Diaby",password="Diaby_2021", database="base_exo")
cursor = conn.cursor()



requet = [
    "Lister les tous les agences:",
    "Lister tous les caissiers par ordre croissant de leur nom:",
    "Lister tous chef d’agence ainsi que l'addresse de l’agence:",
    "Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde:",
    "Lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est moussa dop par ordre croissant du montant:",
    "Lister les utilisateurs de l’agence Plateau:",
    "Lister le nombre de compte par agence:",
    "Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021:",
    "Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021:",
    "Lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 001:",
    "11.Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence ont le numéro est 00",
    "Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussa diop par ordre croissant du montant:",
    "Lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop:",
    "Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.:",
    "Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021:",
    "Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021:",
    "Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021:",
    "Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221:",
    "Lister les agences qui n’ont pas fait de dépôt le 10-08-2021:",
    "Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221:",
    "Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 221:",
    "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221:",
    ]
def affiche(requete):
    for ind , item  in enumerate(requete):
        print(f"{ind + 1}  - {item}") 
        
        
listechoie = [
            "tape 1 pour menu",
            "tape 2pour les commende passer",
            "tape 3 pour quitter"
        ]
for ind , item in enumerate(listechoie):
    print(f"{ind + 1}  - {item}") 
 
while True:
    menuchoi = int(input(f"faire votre choix")) 
    if menuchoi == 3:
        break
    else:
        if menuchoi == 1:
            affiche(requet)
            
    exchoice= int(input(f"choisir votre requete:"))
    requet_choisi = []
    t=requet.pop(exchoice -1)
    affiche(requet)
    if exchoice == 1:
        cursor.execute("select * from AGENCE")
        agence=cursor.fetchall()
        print(agence)
    elif exchoice == 2:
        cursor.execute("select nom_USER from USERS where id_PROFIL_PROFIL = 3 ORDER BY nom_USER")
        caissier=cursor.fetchall()
        print(caissier)    
    elif exchoice == 3:
        cursor.execute("select nom_USER,adresse_AGENCE from USERS,AGENCE  where id_PROFIL_PROFIL = 1 ")
        nonagence=cursor.fetchall()
        print(nonagence) 
    elif exchoice == 4:
        cursor.execute("select numero_COMPTE_TRANSACTION from COMPTE_TRANSACTION inner  join TRANSACTIONS  on COMPTE_TRANSACTION.numero = TRANSACTIONS.numero_COMPTE_TRANSACTION inner  join AGENCE on  AGENCE.numero_AGENCE = TRANSACTIONS.numero_AGENCE_AGENCE  and  adresse_AGENCE = '41 Randy Park' ORDER BY COMPTE_TRANSACTION.solde_COMPTE_TRANSACTION ASC;")
        transaction=cursor.fetchall()
        print(transaction)
    elif exchoice == 5:
        cursor.execute("select sum(montant_TRANSACTION) from TRANSACTIONS join USERS on USERS.id_USER = TRANSACTIONS.id_USER_USER where USERS.id_PROFIL_PROFIL = 3 and USERS.nom_USER = 'Goby'")
        montant=cursor.fetchall()
        print(montant) 
    elif exchoice == 6:
        cursor.execute("select nom_USER from USERS join AGENCE on USERS.id_USER = AGENCE.id_USER_USER  where AGENCE.adresse_AGENCE = '13 Chive Plaza'")
        nom_user=cursor.fetchall()
        print(nom_user) 
    elif exchoice == 7:
        cursor.execute("select numero from COMPTE_TRANSACTION  inner join TRANSACTIONS on COMPTE_TRANSACTION.numero = TRANSACTIONS.numero_COMPTE_TRANSACTION inner join AGENCE on AGENCE.numero_AGENCE =TRANSACTIONS.numero_AGENCE_AGENCE")
        numerocomp=cursor.fetchall()
        print(numerocomp) 
    elif exchoice == 8:
        cursor.execute("select numero_COMPTE_TRANSACTION  from TRANSACTIONS left  join AGENCE on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE left join USERS on USERS.id_USER = TRANSACTIONS.id_USER_USER and USERS.nom_USER ='Desantis' and TRANSACTIONS.date_TRANSACTION = '2011-08-05'")
        compttransa=cursor.fetchall()
        print(compttransa) 
    elif exchoice == 9:
        cursor.execute("select nom_USER from USERS LEFT  JOIN TRANSACTIONS on USERS.id_USER = TRANSACTIONS.id_USER_USER  and TRANSACTIONS.date_TRANSACTION ='2011-08-11' and TRANSACTIONS.numero_COMPTE_TRANSACTION = 1 and USERS.id_USER = 4")
        leftnom = cursor.fetchall()
        print(leftnom) 
    elif exchoice == 10:
        cursor.execute("select montant_TRANSACTION, date_TRANSACTION from TRANSACTIONS left  join USERS on USERS.id_USER = TRANSACTIONS.id_USER_USER left join AGENCE on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE  and AGENCE.numero_AGENCE = 1")
        monttra= cursor.fetchall()
        print(monttra) 
    elif exchoice == 11:
        cursor.execute("select nom_USER, numero_COMPTE_TRANSACTION from ASSOCIER left join USERS on USERS.id_USER = ASSOCIER.id_USER_USER left join AGENCE on USERS.id_USER = AGENCE.id_USER_USER and AGENCE.numero_AGENCE = 1 and ASSOCIER.date_debut between '2019-01-01' and '2019-04-30' ORDER BY ASSOCIER.numero_COMPTE_TRANSACTION")
        associer=cursor.fetchall()
        print(associer)
    elif exchoice == 12:
        cursor.execute("select num_DEPOTouRETRAIT from TRANSACTIONS left  join AGENCE on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE left join USERS on USERS.id_USER = TRANSACTIONS.id_USER_USER where USERS.nom_USER = 'Goby' ORDER BY TRANSACTIONS.montant_TRANSACTION")
        depot=cursor.fetchall()
        print(depot) 
    elif exchoice == 13:
        cursor.execute("select montant_TRANSACTION, frais_TRANSACTION from TRANSACTIONS left join USERS on TRANSACTIONS.id_USER_USER= USERS.id_USER left join AGENCE on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE where USERS.nom_USER = 'Slott' and AGENCE.numero_AGENCE = 1 ORDER BY TRANSACTIONS.montant_TRANSACTION")
        frais=cursor.frtchall()
        print(frais) 
    elif exchoice == 14:
        cursor.execute("select sum(montant_TRANSACTION*valeur) , libelle_PART from TRANSACTIONS left join POSSEDR on TRANSACTIONS.num_TRANSACTION = POSSEDR.num_TRANSACTION_TRANSACTIONS left join PART on PART.id_PART = POSSEDR.id_PART_PART left join AGENCE on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE where AGENCE.numero_AGENCE = 1 GROUP BY libelle")
        sommemont=cursor.fetchall()
        print(sommemont) 
    elif exchoice == 15:
        cursor.execute("select sum(montant_TRANSACTION*valeur) , libelle_PART from TRANSACTIONS left join POSSEDR on TRANSACTIONS.num_TRANSACTION = POSSEDR.num_TRANSACTION_TRANSACTIONS left join PART on PART.id_PART = POSSEDR.id_PART_PART left join AGENCE on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE where date_TRANSACTION = '1961-04-18'  GROUP BY libelle_PART")
        sommetra=cursor.fetchall()
        print(sommetra) 
    elif exchoice == 16:
        cursor.execute("select adresse_AGENCE,max(TRANSACTIONS.montant_TRANSACTION) from AGENCE left join TRANSACTIONS on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE where  TRANSACTIONS.date_TRANSACTION = '1961-04-18'GROUP BY adresse_AGENCE")
        addre=cursor.fetchall()
        print(addre) 
    elif exchoice == 17:
        cursor.execute("select adresse_AGENCE,min(TRANSACTIONS.montant_TRANSACTION) from AGENCE left join TRANSACTIONS on TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE where  TRANSACTIONS.date_TRANSACTION = '1989-01-14'and id_TYPE_TYPE = 1  GROUP BY adresse_AGENCE")
        addagence=cursor.fetchall()
    #     print(addagence) 
    # elif exchoice == 18:
    
        
        # print() 
    # elif exchoice == 19:
    #     print("19") 
    # elif exchoice == 20:
    #     print("20") 
    # elif exchoice == 21:
    #     print("21") 
    # elif exchoice == 22:
    #     print("22")                                                                                              
    #affiche(requet)
        
    
    requet_choisi.append(t)
   
    
    
    # print(requet_choisi)         
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              

   
