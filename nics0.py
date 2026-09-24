# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:38:18 2016

@author: Aurélien
"""
########################################################################

from tkinter import Tk
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import NW
from tkinter import TOP
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import Button
from tkinter import StringVar
from tkinter import Entry
from tkinter import Spinbox
from tkinter import Checkbutton
from tkinter import IntVar

from PIL import Image

import os
import sys

from tkinter.filedialog import askopenfilename
#######################################################################
#Fonction d'execution du programme

def execution():
	chemin=filename.get()
	print(chemin)
	fonction(chemin)

	canvas_fond.create_text(10,300, anchor="w", text="Execution du programme...", fill="gray70")
	
########################################################################
def fonction(chemin) :

	liste1=chemin.split("/")
	nom_du_fichier="trash.txt"
	#nom_du_fichier="Generated_"+liste1[-1]
	#print(nom_du_fichier)
	fichier_com=open(chemin,"r")
	fichier_trash=open(nom_du_fichier,"w")

	nom_du_fichier_gen="Generated_"+liste1[-1]
	fichier_gen=open(nom_du_fichier_gen,"w")

	liste=[]
	for ligne in fichier_com :
		#print(ligne)
		#lignes=fichier_com.readlines()
		liste.append(ligne)
		#print("LISTE:",liste)
	for element in liste:
		#print("element: ",element)
		fichier_gen.write(str(element))

	listeABCD=[]
	
	listeABCD.append(liste[int(atomeA.get())+5])
	listeABCD.append(liste[int(atomeB.get())+5])
	listeABCD.append(liste[int(atomeC.get())+5])
	listeABCD.append(liste[int(atomeD.get())+5])
	if atomeE.get()=='':
		pass
	else:
		listeABCD.append(liste[int(atomeE.get())+5])
	if atomeF.get()=='':
		pass
	else:
		listeABCD.append(liste[int(atomeF.get())+5])
	print("Liste ABCD: ",listeABCD)
	
	listeABCD2=[]
	for j in range(len(listeABCD)):
		listeABCD2.append(listeABCD[j].split())
	print("listeABCD2:      ",listeABCD2)

	
	A=listeABCD2[0]
	B=listeABCD2[1]
	C=listeABCD2[2]
	D=listeABCD2[3]
	
	#origineBC= milieu de [BC]; coord.: xC-xB, yC-yB, zC-zB
	xorigine1=(float(C[1])+float(B[1]))/2
	yorigine1=(float(C[2])+float(B[2]))/2
	zorigine1=(float(C[3])+float(B[3]))/2
	print("origine 1 :",xorigine1,yorigine1,zorigine1)
	#origineAD
	xorigine2=(float(D[1])+float(A[1]))/2
	yorigine2=(float(D[2])+float(A[2]))/2
	zorigine2=(float(D[3])+float(A[3]))/2
	#origineEF
	if atomeF.get()!='' and atomeE.get()!='':
		F=listeABCD2[5]
		E=listeABCD2[4]
		xorigine3=(float(F[1])+float(E[1]))/2
		yorigine3=(float(F[2])+float(E[2]))/2
		zorigine3=(float(F[3])+float(E[3]))/2
		#origine totale = moyenne des trois
		xorigine=round(((xorigine1+xorigine2+xorigine3)/3),8)
		yorigine=round(((yorigine1+yorigine2+yorigine3)/3),8)
		zorigine=round(((zorigine1+zorigine2+zorigine3)/3),8)

	else:
		xorigine=round(((xorigine1+xorigine2)/2),8)
		yorigine=round(((yorigine1+yorigine2)/2),8)
		zorigine=round(((zorigine1+zorigine2)/2),8)

	print("Ecriture fichier")


	fichier_gen.write(" Bq                 "+("{:.8f}".format(xorigine))+"    "+("{:.8f}".format(yorigine))+"    "+("{:.8f}".format(zorigine))+"\n")

	fichier_com.close()
	fichier_trash.close()
	#os.remove("/trash.txt")


#######################################################################
# Fenetre graphique Tkinter du programme
fenetre=Tk()
fenetre.title("NICS 0")
fenetre.geometry("440x352+400+200")

canvas_fond=Canvas(width=440, height=352, bg="black")
canvas_fond.pack()

canvas_fond.create_text(210, 20, text="Selectionnez un fichier .gjf",font=('courier',12,'bold'), fill="gray70")

canvas_fond.create_text(50, 49, text="Fichier .gjf:", fill="gray70")

filename=StringVar()
entry=Entry(fenetre, textvariable=filename, fg='black',width=26)
canvas_fond.create_window(100, 40, anchor=NW, window=entry)
FILETYPES=[("gjf files", "*.gjf")]

canvas_fond.create_text(50, 112, text="Atome A",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 140, text="Atome B",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 168, text="Atome C",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 196, text="Atome D",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 224, text="Atome E",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 252, text="Atome F",font=('courier',12,'bold'), fill="gray70")

atomeA=StringVar()
entry_atomeA=Entry(fenetre, textvariable=atomeA, fg='black',width=5)
canvas_fond.create_window(100, 100, anchor=NW, window=entry_atomeA)

atomeB=StringVar()
entry_atomeB=Entry(fenetre, textvariable=atomeB, fg='black',width=5)
canvas_fond.create_window(100, 128, anchor=NW, window=entry_atomeB)

atomeC=StringVar()
entry_atomeC=Entry(fenetre, textvariable=atomeC, fg='black',width=5)
canvas_fond.create_window(100, 156, anchor=NW, window=entry_atomeC)

atomeD=StringVar()
entry_atomeD=Entry(fenetre, textvariable=atomeD, fg='black',width=5)
canvas_fond.create_window(100, 184, anchor=NW, window=entry_atomeD)

atomeE=StringVar()
entry_atomeE=Entry(fenetre, textvariable=atomeE, fg='black',width=5)
canvas_fond.create_window(100, 212, anchor=NW, window=entry_atomeE)

atomeF=StringVar()
entry_atomeF=Entry(fenetre, textvariable=atomeF, fg='black',width=5)
canvas_fond.create_window(100, 240, anchor=NW, window=entry_atomeF)

def set_filename():
	filename.set(askopenfilename(filetypes=FILETYPES))
	chaine=filename.get()
	chaine_coupee=chaine.split("/")
	#print(chaine_coupee)
	ouverture="Ouverture du fichier : "+chaine_coupee[-1]
	canvas_fond.create_text(10,285, anchor="w",text=ouverture, fill="gray70")

button=Button(fenetre, text="Parcourir", command=set_filename, bg="gray70", activebackground="gray70")
button.configure(width=10)
button.configure(height=1)
canvas_fond.create_window(324, 37, anchor=NW, window=button)

image_schema=PhotoImage(file="Picture.png")
wi=image_schema.width()

canvas_fond.create_image(300, 190, image=image_schema)

bouton_exe=Button(fenetre, text ="Entrer", command=execution, bg="gray70")
bouton_exe.configure(width=10, activebackground="gray70")
bouton_exe_window=canvas_fond.create_window(400, 200, anchor=NW, window=bouton_exe)
bouton_quitter=Button(fenetre, text="Quitter", command=fenetre.quit, bg="gray70",activebackground="gray70")
bouton_quitter.configure(width=10)
bouton_quitter_window=canvas_fond.create_window(400, 200, anchor=NW, window=bouton_quitter)
canvas_fond.create_window(212, 314, anchor=NW, window=bouton_exe)
canvas_fond.create_window(325, 314, anchor=NW, window=bouton_quitter)

fenetre.mainloop()

