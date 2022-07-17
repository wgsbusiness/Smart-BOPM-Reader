############################
#
#	Classe Documents
#
#	Autor      : Wagner Santos
#	Disciplina : Estudo orientado
#	rofessores: Daniel e Rosseti
#	Finalidade : Propor um framework de aplicações para ler caracteres manuescritos utilizando para ferrramneteas de IA
#
############################

import sqlite3
import os
import sys
import time
import cv2  # as cv
import numpy as np
from pathlib import Path
from django.forms import FileField
from   pdf2image import convert_from_path

#import argparse
#import time
#from matplotlib import pyplot as plt
#import imutils





class Documentos:
    
    
	def __init__(self, idUser = None, number= None, uploadedFile=None,dateTimeOfUpload = None,dateTimeOfStartProcess =None ,dateTimeOfEndProcess = None,log = "", folder = None, done = False):
		self.__idUser                = idUser
		self.__number                = number
		self.__uploadedFile		     = uploadedFile
		self.__dateTimeOfUpload	     = dateTimeOfUpload
		self.__UploadedFileHash      = ""
		self.__dateTimeOfStartProcess= dateTimeOfStartProcess
		self.__dateTimeOfEndProcess  = dateTimeOfEndProcess
		self.__log				     = log
		self.__done  				 = done
		self.__folder                = folder
		self.__id                    = 0
		self.__parent_id             = None

	def setIdParent(self, id:int):
		self.__parent_id = id
	
	def getIdParent (self):
		return self.__parent_id	
 
	def setIdUser(self, id:int):
		self.__idUser = id
	
	def getIdUser (self):
		return self.__idUser
 
	def getFolder(self):
		return self.__folder

	def setFolder(self, f):
		self.__folder = f

	def getId(self):
		return self.__id 

	def getUploadedFileHash(self):
		return self.__UploadedFileHash

	def setUploadedFileHash(self, fh):
		self.__UploadedFileHash= fh

	def setNumber(self, number):
		self.__number = number

	def getNumber(self):
		return self.__number 

	def setUploadedFile(self, uploadedFile):
		self.__uploadedFile = uploadedFile

	def getUploadedFile(self):
		return self.__uploadedFile

	def setDateTimeOfUpload(self, dateTimeOfUpload):
		self.__dateTimeOfUpload = dateTimeOfUpload

	def getDateTimeOfUpload(self):
		return self.__dateTimeOfUpload

	def setDateTimeOfStartProcess(self, dateTimeOfStartProcess):
		self.__dateTimeOfStartProcess = dateTimeOfStartProcess

	def getDateTimeOfStartProcess(self):
		return self.__dateTimeOfStartProcess

	def setLog(self, log):
		self.__log = log

	def getLog(self):
		return self.__log

	def setDone(self, done):
		self.__log = done

	def getDone(self):
		return self.__done
	"""
	precisa colocar os paramestros dentro da ordem gravada no lista
	para atualizar no banco de dados o campo DONE e dar sequencia ao processamento dos arquivos

	a seguencia deve ser vista na base de dados

	"""
	def files(self):
		consulta = 'select id, * from uploadfiles_bulletin as b inner join uploadfiles_files f on b.id = f.bulletin_id'
		# Realizando a conexão com o banco de dados 
		conn = sqlite3.connect('db.sqlite3')
		# setting the cursor
		cursor = conn.cursor()
		#Executando a consulta
		files = cursor.execute(consulta)
		# Persistindo na base de dados
		conn.commit()
		# Fechando a base de dados
		conn.close
		print("@@@@@@@@@@@@    SHOW @@@@@@@@@@@@@@@@@@@@@@@@")
		return files
	def savefiles(self):
		try:
			print("@@@@@@ INSERÇAO@@@@@@@")
			# Criando a consulta de inserção dos dados 
			consulta = "insert into uploadfiles_document (User_id, number, uploadedFile, dateTimeOfUpload, UploadedFileHash, dateTimeOfStartProcess, dateTimeOfEndProcess, log, done, folder, parent_id) "
			consulta += " VALUES ( " + str(self.__idUser) + ", "
			print("@@@@@@@@@@@@    SHOW 01 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__number)  + "', "
			print("@@@@@@@@@@@@    SHOW 02 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__uploadedFile) + "', "
			print("@@@@@@@@@@@@    SHOW 03 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__dateTimeOfUpload) + "', "
			print("@@@@@@@@@@@@    SHOW 04 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__UploadedFileHash) + "', "
			print("@@@@@@@@@@@@    SHOW 05 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__dateTimeOfStartProcess) + "', "
			print("@@@@@@@@@@@@    SHOW 06 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__dateTimeOfEndProcess) + "', "
			print("@@@@@@@@@@@@    SHOW 07 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__log) + "', "
			print("@@@@@@@@@@@@    SHOW 08 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__done) + "', "
			print("@@@@@@@@@@@@    SHOW 09 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + (self.__folder) + "', "
			print("@@@@@@@@@@@@    SHOW 01 @@@@@@@@@@@@@@@@@@@@@@@@")
			consulta += "'" + str(self.__parent_id) + "');"
			print(consulta)
			print("prepatando a conexão")
			# Realizando a conexão com o banco de dados 
			conn = sqlite3.connect('db.sqlite3')
			# setting the cursor
			cursor = conn.cursor()
			#Executando a consulta
			cursor.execute(consulta)
			# Persistindo na base de dados
			conn.commit()
			# Fechando a base de dados
			conn.close
			print("@@@@@@@@@@@@    SHOW @@@@@@@@@@@@@@@@@@@@@@@@")
			return True
		except TypeError as e:
      
			print(e)
			return False
		

 

	def update(self, id,  number= None, uploadedFile=None,dateTimeOfUpload = None,dateTimeOfStartProcess =None ,dateTimeOfEndProcess = None,log = "", folder = None, done = False):
		# connecting...
		conn = sqlite3.connect('db.sqlite3')
		# setting the cursor
		cursor = conn.cursor()
		if id != None:
			consuta =  "UPDATE uploadfiles_document SET number = '" + number + "', "
			# colocar o numero que a pessoa informou
			# colocar o hast com o nome do arquivo
			consuta += "uploadedFile = '" + uploadedFile + "', "
			consuta += "dateTimeOfUpload = '" + dateTimeOfUpload + "', "
			consuta += "dateTimeOfStartProcess = '" + str(dateTimeOfStartProcess) + "', "
			consuta += "log = '" + str(log) + "', "
			consuta += "folder = '" + str(folder) + "', "
			consuta += "done = '" + str(done) + "'"
			consuta += " where id ='" + str(id) + "';"
			# connecting...
			conn = sqlite3.connect('db.sqlite3')
			# setting the cursor
			cursor = conn.cursor()
			cursor.execute(consuta)
			conn.commit()
			conn.close
			return True
		else:
			return False

	def select(self, id=None, done = None):
		# connecting...
		conn = sqlite3.connect('db.sqlite3')
		# setting the cursor
		cursor = conn.cursor()
		if id == None and done == None:
			consuta = "select id, number, uploadedFile, folder, dateTimeOfUpload,  dateTimeOfStartProcess, dateTimeOfEndProcess, log, done from uploadfiles_document;"
		elif done != None and id == None:
			consuta = "select id, number, uploadedFile, folder, dateTimeOfUpload,  dateTimeOfStartProcess, dateTimeOfEndProcess, log, done from uploadfiles_document where done =" + str(done) + ";"
		elif done == None and id != None:
			consuta = "select id, number, uploadedFile, folder, dateTimeOfUpload,  dateTimeOfStartProcess, dateTimeOfEndProcess, log, done from uploadfiles_document where id =" + str(id) + ";"
		else: 
			consuta = "select id, number, uploadedFile, folder, dateTimeOfUpload,  dateTimeOfStartProcess, dateTimeOfEndProcess, log, done from uploadfiles_document where id =" + str(id) + " and done =" + str(done) + ";"
		cursor.execute(consuta)
		lista = cursor.fetchall()
		return lista

	def select_usename(self, username):
		# connecting...
		conn = sqlite3.connect('db.sqlite3')
		# setting the cursor
		cursor = conn.cursor()
		consuta = "select id, number, uploadedFile, folder, dateTimeOfUpload,  dateTimeOfStartProcess, dateTimeOfEndProcess, log, done from uploadfiles_document where username =" + username +";"
		cursor.execute(consuta)
		lista = cursor.fetchall()
		return lista

	def convert( self, _id):
		#try:
		dataFiles = self.select(id = _id)
		DirSaida = dataFiles[0][3] + "/paginas"
		DirEntrada = dataFiles[0][3] +"/"+ dataFiles[0][2]
		if not os.path.exists(DirSaida):
			os.makedirs(DirSaida)

		print("convertendo as paginas")
		dpi = 500
		print(DirEntrada)
		paginas = convert_from_path(DirEntrada, dpi)
		# inicia a contagen das páginas
		Conta_Pagina = 0
		arqsSaida=[]
		with open("../../result/coordenadas.txt", "a+") as y:
			# Enquanto houver um objeto pagina em paginas
			for pagina in paginas:
				# Monta o nome de saida do arquivo
				arqsSaida.insert (Conta_Pagina, DirSaida  + "/"+ dataFiles[0][2][:-4] + '_pagina_' + str(Conta_Pagina +1) +'.jpg')
				# grava a o objeto pagina como imagem
				pagina.save(arqsSaida[Conta_Pagina], "JPEG")
				retangulo, file,coord = self.shape(shape = DirSaida  + "/"+ dataFiles[0][2][:-4] + '_pagina_' + str(Conta_Pagina +1) +'.jpg', DirSaida = DirSaida)
				coord = ''.join(map(str,coord))
				linha = os.path.basename(file) + ";" + str(Conta_Pagina +1) + ";" + str(dpi) + ";" + str(retangulo) + "\n"
				y.write(linha)
				# soma uma à variável conta_pagina
				Conta_Pagina += 1
		y.close()
		print("Termino da impressao das coordenadas")
		#if self.shape(shape = DirSaida  + "/"+ dataFiles[0][2][:-4] + '_pagina_1.jpg'):	
		#	return True
		#else:
		return True
		#except Exception as e:
		#	return False

	def shape (self, shape, DirSaida):
		img2   = cv2.imread(shape, 0) #carregando a imagem em tons de cinza

		img  = cv2.imread(shape) # carregando a imagem colorida

		ret, threshold = cv2.threshold(img2,20,255,cv2.THRESH_BINARY_INV)

		kernel = np.ones((21,21),np.uint8)

		dilated_value = cv2.dilate(threshold,kernel,iterations = 1)
		
		contours, hierarchy = cv2.findContours(dilated_value,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		
		cordinates = []
		coord      = []
		area_maior = 0
		retangulo  = 0
		tamanho = 0
		for cnt in contours:
			area = cv2.contourArea(cnt)

			x,y,w,h = cv2.boundingRect(cnt)

			if area > 0.0:
				coord.append([[x,y,w,h], area])
			if area > 20000:
				if area > area_maior:
					area_maior = area
					xmaior = x
					ymaior = y
					wmaior = w
					hmaior = h
				#bounding the images
				#if y < 30000: 

				cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
				#approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
				#cv2.drawContours(img, [approx], 0, (255, 0, 0), 5)

			retangulo +=1
		if not os.path.exists(DirSaida + "/final"):
			os.makedirs(DirSaida + "/final")
		cv2.imwrite(DirSaida + "/final/" + os.path.basename(shape)[:-4] + "_final.jpg", img)
		
		return retangulo, shape, coord