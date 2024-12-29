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
      print(df_ventes)
    
    finally :
     print("Récupération des ventes effectué ")        
    
    #----------------Requete pour recuperer les produits--------------------------
    try:
        sqlProduits = "SELECT * from produits" 
        cursor.execute(sqlProduits)
    
            # Fetch 
        produits = cursor.fetchall()
        df_produits = pd.DataFrame.from_records(produits)
        print(df_produits)
    finally :
        print("Récupération des produits effectué ")
    #---------------------Requête pour récupérer les clients ---------------------
    try:
            
        sqlClients = "SELECT * from clients" 
        cursor.execute(sqlClients)
    
           # Fetch 
        clients = cursor.fetchall()
        df_clients = pd.DataFrame.from_records(clients)
        print(df_clients)
    finally : 
     print("Récupération des clients effectué ")     
#----------------------Requête pour récuperer les fournisseurs-----------
     try:
             
         sqlFournisseurs = "SELECT * from fournisseurs" 
         cursor.execute(sqlFournisseurs)
     
            # Fetch 
         fournisseurs = cursor.fetchall()
         df_fournisseurs = pd.DataFrame.from_records(fournisseurs)
         print(df_fournisseurs)
     finally : 
      print("Récupération des fournisseurs effectué ")    
#-------------------------Récuperer les transactions --------------------------
     try:
             
         sqlTransactions = "SELECT * from transactions" 
         cursor.execute(sqlTransactions)
     
            # Fetch 
         transactions = cursor.fetchall()
         df_transactions = pd.DataFrame.from_records(transactions)
         print(df_transactions)
     finally : 
      print("Récupération des transaction effectué ")          