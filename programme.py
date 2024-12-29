# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:46:37 2024

@author: romar
"""

import pymysql

#1 Récuperer de la base de données
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='rqe_entreprise',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)