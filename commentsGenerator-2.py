# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:11:29 2022

@author: gio

maybe vedi prima la licenza prima di pubblicare
code copied from: https://blog.aspose.com/2022/01/14/add-comments-to-ppt-slides-in-python/
useful to manipulate pptx:  https://www.geeksforgeeks.org/creating-and-updating-powerpoint-presentations-in-python-using-python-pptx/?id=discuss
new line symbol: https://www.educba.com/python-raw-string/
str cut: https://www.geeksforgeeks.org/string-slicing-in-python/
os path: https://www.geeksforgeeks.org/os-module-python-examples/


useful file: lectureNames-v2.py

"""


import aspose.slides as slides
import os #dir_list = os.listdir(path) 


def generateTXT():
    
    #
    #
    #
    root = ""
    #
    #
    #
    
    path = root + "\\lectures\\" 
    
    #per ogni pptx che trovi nel path
    for lecture in os.listdir(path):
        
        #[:-5] toglie il .pptx dalla string
        filename = root + "\\cards\\" + lecture[:-5] + ".txt" 
        
        #blocco if-else per generare solo i file nuovi, senza dover sovrascrivere i vecchi
        if(os.path.isfile(filename) and os.path.getsize(filename) > 0):
            #se il file esiste e non è vuoto: non fare niente
            pass
        else:
            #se il file non esiste oppure esiste ma vuoto
            # open file in write mode
            file = open(filename, "w")
            
            #entra nel singolo pptx
            with slides.Presentation(path + lecture) as presentation:
                # Loop through authors
                for author in presentation.comment_authors:
                    # Loop through comments
                    for comment in author.comments:
                        #print(comment.text)
                        file.write( "S" + str(comment.slide.slide_number) + ": " + comment.text + '\n')
                        
            #chiude il file in cui ha scritto la lecture
            file.close()


    #print("salvati " + materia)

'''
materia = ["ST", "E1"]
for m in materia:
    generateTXT(m)
'''
generateTXT()

