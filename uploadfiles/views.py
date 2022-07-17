"""
	Autor: Wagner Santos
	Disciplina: Estudo orientado
	Professores: Daniel e Rosseti
	Finalidade: Propor um framework de aplicações para ler caracteres manuescritos utilizando para ferrramneteas de IA
"""
import hashlib
import django, shutil, time, logging, sys, json, os
from users.models import User
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from . import models
from sbrw import settings
from classes.documentos import Documentos
from pathlib import Path
from classes import util


class uploadfilesPageView(TemplateView):
    template_name = "uploadfiles.html"


class uploadfilesPageResposta(TemplateView):
    template_name = "resposta.html"




      
    
    
def uploadFile(request):
    logger = logging.getLogger()
    try:
        if request.method == "POST":
            # Fetching the form data
            fileNumber = request.POST["fileNumber"]
            
            user = User.objects.get(username__exact=request.POST["usuario"])
            uploadedFile = request.FILES["uploadedFile"]
            # Pegando o momento da gravação do arquivo no servidor
            timesave = str(int(time.time() * 1000))
            #criando nome hash do arquivo
            hashfile = request.FILES["uploadedFile"]
            
            bulletin = models.bulletin(
                User = user,
                number = fileNumber,
                done = 0
            )
            
            bulletin.save()
            
            print(uploadedFile.name)
            extensao = uploadedFile.name.split(".")
            
            print(extensao[1])
            
            
            file = models.files(
                
                bulletin = bulletin,
                
                file = uploadedFile,
                
                folder = "",
    
                hashName = "",
    
                fileExtension = extensao[1], 
                
                status = ""
                
                
            )
            
            file.save()
            print("Criando o hash")
            hashfile =  util.get_hash(str(settings.MEDIA_ROOT) + "/"+ str(file.file.name))
            print("Criando o path")
            newPath = util.createParh(hashfile)
            print("Movendo o arquivo") 
            shutil.move(file.file.path, newPath + "/" + str(hashfile))
            print("Gravando o arquino banco")
            file.file = str(hashfile)
            print("salvando o path no banco")
            file.folder = newPath
            file.hashName = hashfile
            print("pesistindo no banco")
            file.save()
            
            
            """
            # Saving the information in the database
            document = models.Document(
                User = user,
                number= fileNumber,
                uploadedFile=uploadedFile,
                uploadedFileHash=uploadedFile,
                folder=settings.MEDIA_ROOT,
                done=0,
            )
            document.save()
            """
        return render(request, "sucesso.html", context={"files": bulletin.number})
    except Exception as e:    
        return render(request, "error.html", context={"Error": logger.error("Erro ao importar o arquivo!" +str(e))})
        
    