from django.contrib import admin
from django.urls import path
from appk.views import *


urlpatterns = [
    path('categories/', CategorieListCreateAPIView.as_view(), name='categorie-list-create'),
    path('medicaments/', MedicamentListCreateAPIView.as_view(), name='medicament-list-create'),
    path('pharmacies/', PharmacieListCreateAPIView.as_view(), name='pharmacie-list-create'),
    path('pharmastock/', Pharma_Stock_MedicListCreateAPIView.as_view(), name='pharmastock-list-create'),


    
    
]
