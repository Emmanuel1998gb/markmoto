from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import joblib

def index(request):

    donnees = {
          'nom' : 'lemabo ',
            'postNom' : 'tandishabo',
            'sexe':'masculin'
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(donnees,request))

def listeEtudiants(request):

    donnees = {
        'etudiant1':{
            'nom' : 'lemabo ',
            'postNom' : 'tandishabo',
            'sexe':'masculin'
        },
        'etudiant2':{
            'nom' : 'Jacob',
            'postNom' : 'Motana',
            'sexe':'masculin'
        }
    }

    template = loader.get_template('liste.html')
    return HttpResponse(template.render(donnees,request))

def loyer(request):
    template = loader.get_template('ml.html')
    return HttpResponse(template.render({},request))

def predict(request):
    if request.method == 'POST':
        baterieAuto = int(request.POST['baterieAuto'])
        capaciteMemoire = int(request.POST['capaciteMemoire'])
        tableauPixel = int(request.POST['tableauPixel'])
        ancieneteModele = int(request.POST['ancieneteModele'])

        
        tableau = [[baterieAuto,capaciteMemoire,tableauPixel,ancieneteModele]]

        regresseur = joblib.load('modele_ml/tandisMod.pkl')

        return HttpResponse(regresseur.predict(tableau))
    print('ok')



