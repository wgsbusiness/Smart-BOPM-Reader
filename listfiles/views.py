from django.shortcuts import render
from django.views.generic import TemplateView
from uploadfiles import models
from classes import documentos

# Create your views here.
class listFilesPageView(TemplateView):
    template_name = "listfiles.html"
    
from django.views import generic

class BulletinListView(TemplateView):
    bulletin = models.bulletin
    context_object_name = 'bulletin_list'
    queryset = bulletin.objects.all() # Get 5 books containing the title war
    template_name = 'listfiles.html'  # Specify your own template name/location

class BookListView(TemplateView):
    bulletin = models.bulletin

    def get_queryset(self):
        return models.bulletin.objects.all() 


class BulletinListView(TemplateView):
    template_name = 'listfiles.html'  # Specify your own template name/locationn
   # your own name for the list as a template variable
    def get_queryset(self):
        return models.bulletin.objects.all() # Get 5 books containing the title war
    
    def get_context_data(self, **kwargs):
        context = super(BulletinListView, self).get_context_data(**kwargs)
        context['Usuário']: models.bulletin.user
        context['Numero']: models.bulletin.number
        context['data_de_Upload']: models.bulletin.dateTimeOfUpload
        if models.bulletin.done == 0 :
            context['processando'] = "Não Processado"
        elif models.bulletin.done == 1:
            context['processando'] = "Em processamento"
        elif models.bulletin.done == 2:
            context['processando'] = "Já Processado"
        return context
    
    
def teste(request):
    #bulletin = models.bulletin.objects.all()
    doc = documentos()
    bulletin = doc.files()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(bulletin.id)
    
    return render(request,"listfiles.html",{'bulletin':bulletin.id})