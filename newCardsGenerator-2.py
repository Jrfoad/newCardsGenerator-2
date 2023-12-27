"""
Created on Tue Oct 25 12:49:22 2022

@author: gio
generate an exe from py: https://www.geeksforgeeks.org/convert-python-script-to-exe-file/
input text: https://www.geeksforgeeks.org/how-to-get-the-input-from-tkinter-text-box/
placing elements: https://www.tutorialspoint.com/setting-the-position-on-a-button-in-tkinter-python
radiobutton: https://www.tutorialspoint.com/python/tk_radiobutton.htm
scale: https://www.geeksforgeeks.org/python-tkinter-scale-widget/


TODO:
    alla corrispettiva lezione mostra la mappa, stesso nella finestra
        aggiungi bottone per "map hider" che mostrerà una zona della mappa random stesso nella finestra
        aggiungi bottone "mostra mappa" per mostrare la soluzione di quella nascosta
            
NOTE:
    non puoi creare un exe di un py che usi la libreria Apose.slides
"""


import tkinter as tk
from tkinter import *
import os #dir_list = os.listdir(path) 
import random
import subprocess


# Top level window
frame = tk.Tk()
frame.title("cards generator 1.0")
frame.geometry('1200x350')
#
#
#
root = ""
#
#
#

###############################################################################
#useful functions

def printCard(materia, lecture):
    
    cardFileName = root + materia + "\\cards\\" + lecture 
    #print(cardFileName)
    
    file = open(cardFileName, "r")
    
    # read the content of the file opened
    content = file.readlines()
    
    if not content:
        lblCard.config(text = "file di domande vuoto, aggiorna le cards")
    else:
        #print(random.choice(content))
        #print(len(content))
        lblCard.config(text = random.choice(content))
    
    file.close()


def getLectureName():
    
    #getting input
    numeroLez = v1.get()    #inputLez.get(1.0, "end-1c")
    global materia              #materia = inputMateria.get(1.0, "end-1c")
    
    #setting the path: materia = "SO"
    path = root + materia + "\\cards\\"
    filename = os.listdir(path) #ottieni l'array dei nomi dei file
    
    #check existance of lecture
    if int(numeroLez) > len(filename):
        print("non c'è questa lezione")
    
    #searching lecture
    #la regola testata è: 8:10 per doppia cifra, se cifra singola esce >>> 3_
    if int(numeroLez) <= 9:   
        numeroLez = str(numeroLez) + "_"
        
    #questo for è geniale: confronterà le stringhe contenente il numero della lezione, 
    #ma se il numero è a singola cifra confronterà sempre due caratteri stringa perchè aggiungiamo alla singola cifra il "_"
    for f in filename:
        #print(f[1:3])
        if str(numeroLez) == f[1:3]: 
            
            lblFile.config(text = f)
            printCard(materia, f)
            

def generaCommenti():
    filepath = "commentsGenerator-2.py"
    subprocess.call("python "+filepath)
    


###############################################################################
inputMateria = IntVar(frame, 1)

materia = ''
'''
def selE1():
    global materia
    materia = "E1"
    #print(materia)

def selST():
    global materia
    materia = "ST"
    #print(materia)


Radiobutton(frame, 
                text = "E1", 
                variable = inputMateria,
                value = 1,
                command=selE1
                ).pack(anchor=W, ipadx=5, ipady=5)


Radiobutton(frame, 
                text = "ST", 
                variable = inputMateria,
                value = 0,
                command=selST
                ).pack(anchor=W, ipadx=5, ipady=5, side=LEFT)
'''
###############################################################################
###############################################################################
# numero Lezione
v1 = IntVar()
w = tk.Scale(frame, from_=1, to=35, variable=v1, orient=HORIZONTAL, width=20, 
             label ="lezione" ).pack(ipadx = 200, side = TOP)



###############################################################################
###############################################################################

# Label Creation filename
lblFile = tk.Label(frame, text = "[file]")
lblFile.pack()
lblFile.place(y=170)   

#######################################
# Label Creation card
lblCard = tk.Label(frame, text = "[Risposta in Slide num]: [Quest]")
lblCard.pack()
lblCard.place(y=200)   

###############################################################################
###############################################################################
# Button Creation
printButton = tk.Button(frame,
						text = "cerca",
						command = getLectureName)
printButton.pack()
#printButton.place()

#######################################
# Button Creation per generare nuovi file txt per le cards
commentButton = tk.Button(frame,
						text = "aggiorna cards",
						command = generaCommenti)

commentButton.pack(side = RIGHT, padx = 150)


###############################################################################
###############################################################################
frame.mainloop()
