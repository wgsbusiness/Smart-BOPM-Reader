"""
	Autor: Wagner Santos
	Disciplina: Estudo orientado
	Professores: Daniel e Rosseti
	Finalidade: Propor um framework de aplicações para ler caracteres manuescritos utilizando para ferrramneteas de IA
"""
import django, shutil, time, logging, sys, json, os
from users.models import User
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.conf import settings
from classes.documentos import Documentos
from pathlib import Path


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
        return render(request, "sucesso.html", context={"files": document})
    except Exception as e:    
        return render(request, "error.html", context={"Error": logger.error("Erro ao importar o arquivo!" +str(e))})
        
    