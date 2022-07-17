from django.db import models
import hashlib
import time
from uploadfiles.views import uploadFile


class bulletin(models.Model):

    class Meta:
        ordering = ['-number']


    dateTimeOfUpload = models.DateTimeField(auto_now=True)
    number = models.CharField(max_length=200)
    User = models.ForeignKey('users.User', on_delete=models.CASCADE, max_length=10, null=True, blank=True)
    # 0 - Não processado; 1 - Em processamento; 2 - Processado
    done = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.User} {self.number} {self.dateTimeOfUpload} {self.done}'

class files(models.Model):

    def hashFile(instance, filename):
        timesave = str(int(time.time() * 1000))
        return '{0}{1}/{0}{1}'.format(timesave, str((filename)))


    def get_hash(instance, img_path):
        print("@@@@@@@ RREALIZANDO HASH @@@@@@@@")
        
        print(img_path.path())
        
        # This function will return the `md5` checksum for any input image.
        with open(img_path, "rb") as f:
            img_hash = hashlib.md5()
            while chunk := f.read(8192):
                img_hash.update(chunk)
        return img_hash.hexdigest()

    # data e hora do inicial do processamento do arquivo
    dateTimeOfStartProcess = models.DateTimeField(null=True)

    # data de término do processamento do arquivo
    dateTimeOfEndProcess = models.DateTimeField(null=True)
    
    folder = models.CharField(max_length=200, null=True)
    
    hashName = models.CharField(max_length=200, null=True)
    
    file = models.FileField(null=True, blank=True) #(upload_to="", null=True, blank=True)
    
    fileExtension = models.CharField(max_length=200, null=True)
    
    status = models.CharField(max_length=200, null=True)
    
    parent = models.ForeignKey('files', on_delete=models.CASCADE, max_length=10, null=True, blank=True)

    bulletin = models.ForeignKey('bulletin', on_delete=models.CASCADE, max_length=10, null=True, blank=True)


"""
class fileFields (models.Model):

    class Meta:
        ordering = ['-files']
    files = models.ForeignKey('files', on_delete=models.CASCADE, max_length=10, null=True, blank=True)
    fields = models.ForeignKey('Fields', on_delete=models.CASCADE, max_length=10, null=True, blank=True)
    contents = models.TextField(max_length=1000000000, null=True)
    

class Fields (models.Model):
    
    class Meta:
        ordering = ['-field']            
    field = models.TextField(max_length=100, null=True)

"""
class Document(models.Model):
    
    class Meta:
        ordering = ['-uploadedFile']

    def hash_directory_path(instance, filename):
        timesave = str(int(time.time() * 1000))
        return '{0}{1}/{0}{1}'.format(timesave, str(hash(filename)))
          
    number = models.CharField(max_length=200)
    uploadedFile = models.CharField(max_length=200)
    # data e hora da submissão do processo
    dateTimeOfUpload = models.DateTimeField(auto_now=True)
    # data e hora do inicial do processamento do arquivo
    dateTimeOfStartProcess = models.DateTimeField(null=True)
    # data de término do processamento do arquivo
    dateTimeOfEndProcess = models.DateTimeField(null=True)
    folder = models.CharField(max_length=200, null=True)
    # 0 - Não processado; 1 - Em processamento; 2 - Processado
    done = models.IntegerField(default=0)
    log = models.TextField(max_length=20000, null=True, blank=True)
    User = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, max_length=10, null=True, blank=True)
    uploadedFileHash = models.FileField(upload_to=hash_directory_path, null=True, blank=True)

    parent = models.ForeignKey(
        'Document', on_delete=models.CASCADE, max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.uploadedFile
