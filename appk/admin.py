from django.contrib import admin

# Register your models here.
# import models 

# admin.site.register(medecin)
from .models import *

admin.site.register(Patient)
admin.site.register(Pharmacie)
admin.site.register(Livreur)
admin.site.register(Medicament)
admin.site.register(Categorie)
admin.site.register(Pharma_Stock_Medic)
admin.site.register(Commande)
admin.site.register(Livraison)
admin.site.register(Ligne_Commande)
