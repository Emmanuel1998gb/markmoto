from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('liste/',views.listeEtudiants,name='liste_etudiants'),
    path('loyer/',views.loyer, name = 'loyer'),
    path('predict',views.predict, name = 'predict')
]
