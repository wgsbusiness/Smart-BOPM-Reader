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

import hashlib
import os
from sbrw import settings
import random

def get_hash(img_path):
    print(img_path)    
    # This function will return the `md5` checksum for any input image.
    with open(img_path, "rb") as f:
        img_hash = hashlib.md5()
        while chunk := f.read(8192):
            img_hash.update(chunk)
    return img_hash.hexdigest()

def  createParh(hash):
    x= random.randint(1,len(hash))
    continua = True
    while continua:
        x= random.randint(1,len(hash))
        way = str(settings.MEDIA_ROOT) + "/" + hash[0:x]
        if not os.path.exists(way):
            os.makedirs(way)
            way+= "/" + str(hash[x:len(hash)])
            os.makedirs(way)
            continua = False
        else:
            x= random.randint(1,len(hash))
            way+= "/" + str(hash[x:len(hash)])
            if not os.path.exists(way):
                os.makedirs(way)
                continua = False
    return way
