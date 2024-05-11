"""
URL configuration for test_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appk.views import *
from django.conf.urls.static import static
from django.conf import settings

# from appk import *



urlpatterns = [
    # models
    path('admin/', admin.site.urls),
    path('categories/', CategorieListCreateAPIView.as_view(), name='categorie-list-create'),
    path('medicaments/', MedicamentListCreateAPIView.as_view(), name='medicament-list-create'),
    path('pharmacies/', PharmacieListCreateAPIView.as_view(), name='pharmacie-list-create'),
    path('pharmastock/', Pharma_Stock_MedicListCreateAPIView.as_view(), name='pharmastock-list-create'),
    path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    path('lignecommande/', Ligne_CommandeListCreateAPIView.as_view(), name='lignecommande-list-create'),
    path('livreurs/', LivreurListCreateAPIView.as_view(), name='livreur-list-create'),
     path('commandes/', CommandeListCreateAPIView.as_view(), name='commande-list-create'),
    path('livraisons/', LivraisonListCreateAPIView.as_view(), name='livraison-list-create'),
    # views of register and login patient
    path('patients/register/', PatientRegistreListView.as_view(), name='patient-register'),
    # path('patients/test/login', PatientLoginView.as_view(), name='patient-login'),
    # views of register and login livreur
    path('livreurs/register/', LivreurRegistreListView.as_view(), name='livreur-register'),
    

    path('pharmacie/register/', PharmacieRegistreListView.as_view(), name='PharmacieRegistreListView'),


    
    # views of commandemedic
    path('commandemedic/', CommandeWithMedicmCreateView.as_view(), name='CommandeWithMedicmCreateView'),
    # views of categories
    path('categorylist/<int:pk>/', CategorieDetailView.as_view()),
    path('categorylist/', CategorieDetailView.as_view()),
    path('delete_all_categories/', delete_all_categories, name='delete_all_categories'),
    # views of medicaments
    path('medicamentlist/<int:pk>/', MedicamentDetailView.as_view()),
    path('medicamentlist/', MedicamentDetailView.as_view()),
    path('delete_all_medicaments/', delete_all_medicaments, name='delete_all_medicaments'),
    # views of pharmacies
    path('pharmacielist/<int:pk>/', PharmacieDetailView.as_view()),
    path('pharmacielist/', PharmacieDetailView.as_view()),
    path('delete_all_pharmacies/', delete_all_pharmacies, name='delete_all_pharmacies'),
    # views of pharmastock
    path('pharmastocklist/<int:pk>/', Pharma_Stock_MedicDetailView.as_view()),
    path('pharmastocklist/', Pharma_Stock_MedicDetailView.as_view()),
    path('delete_all_pharmastock/', delete_all_pharmastock, name='delete_all_pharmastock'),
    # views of patients
    path('patientlist/<int:pk>/', PatientDetailView.as_view()),
    path('patientlist/', PatientDetailView.as_view()),
    path('delete_all_patients/', delete_all_patients, name='delete_all_patients'),
    # views of lignecommande
    path('lignecommandelist/<int:pk>/', Ligne_CommandeDetailView.as_view()),
    path('lignecommandelist/', Ligne_CommandeDetailView.as_view()),
    path('delete_all_lignecommande/', delete_all_lignecommande, name='delete_all_lignecommande'),
    # views of livreurs
    path('livreurlist/<int:pk>/', LivreurDetailView.as_view()),
    path('livreurlist/', LivreurDetailView.as_view()),
    path('delete_all_livreurs/', delete_all_livreurs, name='delete_all_livreurs'),
    # views of commandes
    path('commandelist/<int:pk>/', CommandeDetailView.as_view()),
    path('commandelist/', CommandeDetailView.as_view()),
    path('delete_all_commandes/', delete_all_commandes, name='delete_all_commandes'),
    # views of livraisons
    path('livraisonlist/<int:pk>/', LivraisonDetailView.as_view()),
    path('livraisonlist/', LivraisonDetailView.as_view()),
    path('delete_all_livraisons/', delete_all_livraisons, name='delete_all_livraisons'),

    path('Login_gn/', Login_gn.as_view(), name='Login_gn'),
    path('utilisateurs/<int:user_id>/commandes/', Command_by_user, name='commandes-utilisateur'),
    path('commandes/<int:command_id>/livreurs/', Livreur_by_command, name='livreurs-commandes'),

   

    


    # path('', urls),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
 
    