# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:46:37 2024

@author: romar
"""

import pymysql
import pandas  as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import datetime

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
        sql_CA_Par_Produits = "select nom_produit , sum(montant) as 'montant' from produits p inner join ventes v on p.id_produit = v.ref_produit group by nom_produit"
        cursor.execute(sql_CA_Par_Produits)
        
        #Fetch
        CA_Par_Produits = cursor.fetchall()
        df_CA_Par_Produits = pd.DataFrame().from_records(CA_Par_Produits)
        print(df_CA_Par_Produits)
        
    finally :
        print("Récupération des produits effectué")
        

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
      
#---------------------------Ventes par fournisseur-----------------------------
    try: 
        #Ventes de produits par fournisseurs
        sqlVentes_Par_Fournisseurs = "select concat(prenom_fournisseur,'',nom_fournisseur) as 'fournisseur' ,sum(quantite_vendu) from produits p  inner join ventes v on p.id_produit = v.ref_produit inner join fournisseurs f on p.ref_fournisseur = f.id_fournisseur group by fournisseur ;"
        cursor.execute(sqlVentes_Par_Fournisseurs)
        
        #Fetch
        ventes_Par_Fournisseurs = cursor.fetchall()
        df_ventes_Par_Fournisseurs = pd.DataFrame.from_records(ventes_Par_Fournisseurs)
      
    finally : 
     print("Récupération des ventes fournisseurs effectué ")   
#------------------------------Montant moyen des ventes-------------------------
    try: 
        #Ventes de produits par fournisseurs
        sqlMontant_Moyen_Ventes = "SELECT avg(montant) as 'Montant moyen' from ventes"
        cursor.execute(sqlMontant_Moyen_Ventes)
        
        #Fetch
        montant_Moyen_Ventes= cursor.fetchall()
        montant_Moyen_Ventes = pd.DataFrame.from_records(montant_Moyen_Ventes)
        print(montant_Moyen_Ventes)
       
    finally : 
     print("Récupération des ventes fournisseurs effectué ")   
   
#-------------------------Nombre total de clients-----------------------------  
    try: 
        #Ventes de produits par fournisseurs
        sqlNb_Total_Client = "SELECT count(id_clients) as 'Nb clients' from clients"
        cursor.execute(sqlNb_Total_Client)
        
        #Fetch
        nb_Total_Client= cursor.fetchall()
        df_Montant_Moyen_Ventes = pd.DataFrame.from_records(montant_Moyen_Ventes)
    
       
    finally : 
        print("Récupération des ventes fournisseurs effectué ")   
#--------------------------Taux de croissance des ventes------------------------
if (df_ventes_Par_Mois['Mois'] == 12).any() :
  decembre = df_ventes_Par_Mois[df_ventes_Par_Mois['Mois'] == 12]
if (df_ventes_Par_Mois['Mois'] == 12).any() :
  novembre = df_ventes_Par_Mois[df_ventes_Par_Mois['Mois'] == 11]
if (df_ventes_Par_Mois['Mois'] == 12).any() :
  octobre = df_ventes_Par_Mois[df_ventes_Par_Mois['Mois'] == 10]        
  
#----------------------------Graphique CA Par produits-------------------  
laptop = df_CA_Par_Produits['montant'][0]
casque_Sony = df_CA_Par_Produits['montant'][1]
tablette_Samsung = df_CA_Par_Produits['montant'][2]
smartphone_Apple= df_CA_Par_Produits['montant'][3]
ecouteurs_Bose = df_CA_Par_Produits['montant'][4]
montre_Connectee = df_CA_Par_Produits['montant'][5]
clavier_logitech = df_CA_Par_Produits['montant'][6]
chargeur_sans_fil = df_CA_Par_Produits['montant'][7]
labels = ['laptop','Casque Sony','Tablette Samsung','Smartphone Apple']  
couleurs_bars = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
montants = [laptop ,casque_Sony,tablette_Samsung,smartphone_Apple] 



def histogramme(x,y,couleurs_bars,label_x , label_y,titre_graphique) :
 
   fig, ax = plt.subplots(figsize=(10,6))  
   ax.bar(x, y, label=x, color=couleurs_bars)
   for i in range(len(x)):
        plt.text(i, y[i], y[i] , ha="center")
    
   ax.set_ylabel(label_y)
   ax.set_xlabel(label_x)
   ax.set_title(titre_graphique)  
   plt.show()
   
def exporterPdf(nom_fichier ,nb_page, graphique_un = None , graphique_deux = None,
                graphique_trois = None) :
 with PdfPages(nom_fichier) as pdf:
     if nb_page == 1 :
          graphique_un  #Appeler ton graphique
          pdf.savefig()
          plt.close()
          print("Exportation PDF effectué avec succès")
     if nb_page == 2 : 
         graphique_un  #Appeler ton graphique
         pdf.savefig()
         plt.close()
         
         graphique_deux  #Appeler ton graphique
         pdf.savefig()
         plt.close()   
         print("Exportation PDF efectué avec succès")
     if nb_page == 3 : 
          graphique_un  #Appeler ton graphique
          pdf.savefig()
          plt.close()
          
          graphique_deux  #Appeler ton graphique
          pdf.savefig()
          plt.close()   
          
          graphique_trois  #Appeler ton graphique
          pdf.savefig()
          plt.close() 
          print("Exportations PDF effectué avec succès")
             
             
          d = pdf.infodict()
          d['Title'] = 'Projet générateur de rapport PDF'
          d['Author'] = 'Romario Quashie'
          d['Subject'] = 'How to create a multipage pdf file and set its metadata'
          d['CreationDate'] = datetime.datetime(2024, 12, 30)
          d['ModDate'] = datetime.datetime.today()     
         
#--------------------programme principal----------------------------------------         
histogramme_CA_Par_Produits = histogramme(labels,montants, couleurs_bars,"Nom des produits","Chiffre d'affaires (en Euros)",
             "HIstogramme de la répartition du chiffre d'affaires de l'entreprise en fonction des produits")   

exporterPdf("Rapports ventes.pdf", 1 , graphique_un = histogramme_CA_Par_Produits)     