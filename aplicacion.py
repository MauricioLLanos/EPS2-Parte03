# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3

miConexion = sqlite3.connect("Zarate_almacen")

miCursor= miConexion.cursor()

miCursor=execute("""
                 CREATE TABLE Producto
                 idproducto PRIMARY KEY,
                 codigo numeric(10),
                 nombre varchar(30),
                 precio numeric(10)
                 """)
                 
           AñadirDatos = [
              ( "1", "a","Arroz","13.0")
              ( "2"	,"b"	,"Camote","1.0")
              ( "3"	,"c	","Pan","2.0")
              ( "4"	,"d","Gaseosa","4.0")
              ( "5"	,"e	","Torta","5.0")
              ( "6"	,"f","Camaron",	"6.0")
              ( "7"	,"g	","Pezcado","6.5")
              ( "8",	"h"	,"Carne","7.0")
              (" 9",	"i"	,"Lechuga",	"8.0")
              ( "10",	"j"	,"Azucar","10.0")
               ]      

miCursor.executemany("INSERT INTO VEHICULOS VALUES(?,?,?,?")


menu = int(input("Menu Opciones:\n 1- Registrar\n 2. Eliminar\n 3. Editar\n 4. Listar\n 5. Salir\n"))
while menu !=0:
    if menu == 1:
        print ("Registrar")
    elif menu == 2:
        print ("Eliminar")
    elif menu == 3:
        print ("Editar")
    elif menu == 4:
        print ("Listar")
    elif menu == 5:
        print ("Salir")
    else:
        print ("elegir una opcioón correcta")
    
    menu = int(input("\nMenu Opciones:\n 1- Registrar\n 2. Eliminar\n 3. Editar\n 4. Listar\n 5. Salir\n"))
        
    