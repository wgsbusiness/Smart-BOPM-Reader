"""
	Autor      : Wagner Santos
	Disciplina : Estudo orientado
	Professores: Daniel e Rosseti
	Finalidade : Propor um framework de aplicações para ler caracteres manuescritos utilizando para ferrramneteas de IA
"""

#import sqlite3
"""
#***************************
# impotando modulos de multprocessos
from multiprocessing import Pool
from multiprocessing import Process, current_process
import time
from time import sleep
import random
#
#**************************
"""
from documentos import Documentos
#from filevalidation.filevalidation import convert
from datetime import datetime
from craft.test import main_craft
import time
#import os, sys, shutil


continuar = True
print("Waiting for files to start processing...")

while continuar:
    try:
        time.sleep(1)
        uploadfiles = Documentos()
        linhas = uploadfiles.select(done=0)
        if len(linhas)>0:
            for linha in linhas:
                print("Starting", linha[2], "file processing..." )
                if uploadfiles.convert(_id = linha[0]):
                    #retangulo, file, coord = uploadfiles.shape (shape = linha[0])
                    if main_craft(linha[3] + "/paginas/final", linha[3] + "/paginas/final"):
                        print("End of processing", linha[2], "file.")
                        uploadfiles.update(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6],linha[7], 2)
                        print("Waiting for files to start processing...")
    except FileNotFoundError as e:
        print(e)
        continuar = False