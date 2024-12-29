# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:46:37 2024

@author: romar
"""

import pymysql
import pandas  as pd

#1 Se connecter à la base de données
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='rqe_entreprise',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

 
with conn.cursor() as cursor:
#------------------------Requete pour recuperer les ventes-----------------------
    try:       
      sqlVentes = "SELECT * from ventes" 
      cursor.execute(sqlVentes)
      
      # Fetch 
      ventes = cursor.fetchall()
      df_ventes = pd.DataFrame.from_records(ventes)
    
    finally :
     print("Récupération des ventes effectué ")        
    
    #----------------Requete pour recuperer les produits--------------------------
    try:
        sqlProduits = "SELECT * from produits" 
        cursor.execute(sqlProduits)
    
            # Fetch 
        produits = cursor.fetchall()
        df_produits = pd.DataFrame.from_records(produits)
        
    finally :
        print("Récupération des produits effectué")
    #---------------------Requête pour récupérer les clients ---------------------
    try:     
        sqlClients = "SELECT * from clients" 
        cursor.execute(sqlClients)
    
           # Fetch 
        clients = cursor.fetchall()
        df_clients = pd.DataFrame.from_records(clients)
        
    finally : 
     print("Récupération des clients effectué ")     
#----------------------Requête pour récuperer les fournisseurs-----------
     try:
         #Liste des fournisseurs    
         sqlFournisseurs = "SELECT * from fournisseurs" 
         cursor.execute(sqlFournisseurs)
     
            # Fetch 
         fournisseurs = cursor.fetchall()
         df_fournisseurs = pd.DataFrame.from_records(fournisseurs)
         
     finally : 
      print("Récupération des fournisseurs effectué ")    
#-------------------------Récuperer les transactions --------------------------
     try:
            
         sqlTransactions = "SELECT * from transactions" 
         cursor.execute(sqlTransactions)
     
            # Fetch 
         transactions = cursor.fetchall()
         df_transactions = pd.DataFrame.from_records(transactions)
         
     finally : 
      print("Récupération des transaction effectué ")    

#1 Performance des ventes

#-----------------------Chiffres d'affaires par produit------------------------
    try:
        
        #Requête
        sql_CA_Par_Produits = "select nom_produit , sum(montant) from produits p inner join ventes v on p.id_produit = v.ref_produit group by nom_produit"
        cursor.execute(sql_CA_Par_Produits)
        
        #Fetch
        CA_Par_Produits = cursor.fetchall()
        df_CA_Par_Produits = pd.DataFrame().from_records(CA_Par_Produits)
        
    finally :
        print("Récupération des produits effectué")
        df_CA_Par_Produits

#-------------------------Ventes par periode---------------------------------
    try:       
     #Requête
       sqlVentesParMois = "SELECT Month(date_vente) as 'Mois' , sum(quantite_vendu) as 'quantité totale' from ventes group by Month(date_vente)"
       cursor.execute(sqlVentesParMois)
    
    #Fetch
       ventes_Par_Mois = cursor.fetchall()
       df_ventes_Par_Mois = pd.DataFrame.from_records(ventes_Par_Mois)
     
    finally : 
      print("Récupération des ventes par periode effectué ")   
      
#-----------------------Ventes par categorie-------------------------------
#---------------------------Ventes par fournisseur-----------------------------
    try: 
        #Ventes de produits par fournisseurs
        sqlVentes_Par_Fournisseurs = "select concat(prenom_fournisseur,'',nom_fournisseur) as 'fournisseur' ,sum(quantite_vendu) from produits p  inner join ventes v on p.id_produit = v.ref_produit inner join fournisseurs f on p.ref_fournisseur = f.id_fournisseur group by fournisseur ;"
        cursor.execute(sqlVentes_Par_Fournisseurs)
        
        #Fetch
        ventes_Par_Fournisseurs = cursor.fetchall()
        df_ventes_Par_Fournisseurs = pd.DataFrame.from_records(ventes_Par_Fournisseurs)
        print(df_ventes_Par_Fournisseurs)
    finally : 
     print("Récupération des ventes fournisseurs effectué ")   
#------------------------------Montant moyen des ventes-------------------------
    try: 
        #Ventes de produits par fournisseurs
        sqlMontant_Moyen_Ventes = "SELECT avg(montant) as 'Montant moyen' from ventes"
        cursor.execute(sqlMontant_Moyen_Ventes)
        
        #Fetch
        montant_Moyen_Ventes= cursor.fetchall()
        df_Montant_Moyen_Ventes = pd.DataFrame.from_records(montant_Moyen_Ventes)
        print(df_Montant_Moyen_Ventes)
    finally : 
     print("Récupération des ventes fournisseurs effectué ")   
#--------------------------Taux de croissance des ventes------------------------
