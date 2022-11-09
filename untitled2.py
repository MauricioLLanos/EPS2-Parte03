# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:49:24 2022

@author: Alumno
"""

import sqlite3

miConexion=sqlite3.connect("PruebaDB")

miCursor.execute("""
                 
                 CREATE TABLE VEHICULOS(
                     MATRICULA VARCHAR(10) PRIMARY KEY,
                     MODELO VARCHAR(15)
                     PRECIO INTEGER,
                     COLOR VARCHAR(15)
                     )
                 
                """ )
                
                
         AñadirDatos = [
             ("5514-DSK", "Mercedes","5000","gris"),
             ("5514-DSK", "Mercedes","5000","gris"),
             ("5514-DSK", "Mercedes","5000","gris"),
             ("5514-DSK", "Mercedes","5000","gris"),
             ("5514-DSK", "Mercedes","5000","gris")
                 )] 
             
             miCursor.executemany("INSERT INTO VEHICULOS VALUES(?,?,?,?)", AñadirDatos)
             
             miConexion.commit()
             miConexion.close()