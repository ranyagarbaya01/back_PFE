from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from appk.models import *
from appk.serializers import *
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token as AuthToken
from django.http import JsonResponse
from django.views import View
from django.views.generic import UpdateView
from .serializers import PatientSerializer
from rest_framework.generics import UpdateAPIView

# Creating and getting all categories
class CategorieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

# getting a single category by its ID, updating and deleting a category
class CategorieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

# deleting all categories
def delete_all_categories(request):
    Categorie.objects.all().delete()
    return JsonResponse({'message': 'All categories deleted successfully'})

# Creating and getting all medicaments
class MedicamentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# getting a single medicament by its ID, updating and deleting a medicament
class MedicamentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

# deleting all medicaments
def delete_all_medicaments(request):
    Medicament.objects.all().delete()
    return JsonResponse({'message': 'All medicaments deleted successfully'})

# Creating and getting all pharmacies
class PharmacieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer

# getting a single pharmacy by its ID, updating and deleting a pharmacy
class PharmacieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer

# deleting all pharmacies
def delete_all_pharmacies(request):
    Pharmacie.objects.all().delete()
    return JsonResponse({'message': 'All pharmacies deleted successfully'})

# Creating and getting all pharmacies
class Pharma_Stock_MedicListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pharma_Stock_Medic.objects.all()
    serializer_class = Pharma_Stock_MedicSerializer

# getting a single pharmacy by its ID, updating and deleting a pharmacy
class Pharma_Stock_MedicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharma_Stock_Medic.objects.all()
    serializer_class = Pharma_Stock_MedicSerializer

# deleting all pharmastock
def delete_all_pharmastock(request):
    Pharma_Stock_Medic.objects.all().delete()
    return JsonResponse({'message': 'All pharmastock deleted successfully'})

# Creating and getting all patients
class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
# getting a single patient by its ID, updating and deleting a shoe
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# deleting all patients
def delete_all_patients(request):
    Patient.objects.all().delete()
    return JsonResponse({'message': 'All patients deleted successfully'})

# Creating and getting all lignes de commande
class Ligne_CommandeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ligne_Commande.objects.all()
    serializer_class = Ligne_CommandeSerializer

# getting a single ligne de commande by its ID, updating and deleting a ligne de commande
class Ligne_CommandeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligne_Commande.objects.all()
    serializer_class = Ligne_CommandeSerializer

# deleting all lignes de commande
def delete_all_lignecommande(request):
    Ligne_Commande.objects.all().delete()
    return JsonResponse({'message': 'All lignes de commande deleted successfully'})

# Creating and getting all livreurs
class LivreurListCreateAPIView(generics.ListCreateAPIView):
    queryset = Livreur.objects.all()
    serializer_class = LivreurSerializer

# getting a single livreur by its ID, updating and deleting a livreur
class LivreurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livreur.objects.all()
    serializer_class = LivreurSerializer

# deleting all livreurs
def delete_all_livreurs(request):
    Livreur.objects.all().delete()
    return JsonResponse({'message': 'All livreurs deleted successfully'})

# Creating and getting all commandes
class CommandeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

# getting a single ordonnance by its ID, updating and deleting a commande
class CommandeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

# deleting all commandes
def delete_all_commandes(request):
    Commande.objects.all().delete()
    return JsonResponse({'message': 'All commandes deleted successfully'})

# Creating and getting all livraisons
class LivraisonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer

# getting a single livraison by its ID, updating and deleting a livraison
class LivraisonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livraison.objects.all()
    serializer_class = LivraisonSerializer

# deleting all livraisons
def delete_all_livraisons(request):
    Livraison.objects.all().delete()
    return JsonResponse({'message': 'All livraisons deleted successfully'})


# patient login
class PatientLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        
        email = request.data.get('email')
        pwd = request.data.get('pwd')

        if not email or not pwd:
            return Response({'detail': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = Patient.objects.get(email=email, pwd=pwd)
        except Patient.DoesNotExist:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Assuming you have a token authentication system for patients
        token = AuthToken.objects.create(patient.user)

        return Response({
            'token': token[1],
            'patient': self.aserializer_class(patient).data,
        }, status=status.HTTP_200_OK)

        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# patient register
class PatientRegistreListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# pass command with medicament
class CommandeWithMedicmCreateView(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeWithMedicamsSerializer

    def perform_create(self, serializer):
        commande = serializer.save()
        # Récupérer les données de réservation de medicm
        medicmss_data = self.request.data.get('reservations', [])
        # Utiliser un ensemble pour stocker les meddic déjà réservés
        reserved_medicm_set = set()
        # Créer les réservations de medicm associées à commande
        created_reservations = []
        for medicm_data in medicmss_data:
            medicament_id = medicm_data.get('medicament')
            quantity = medicm_data.get('qnt')
            medicament = Medicament.objects.get(id=medicament_id)
            if medicament.quantite >= quantity:
                medicament.quantite -= quantity
                medicament.save()
            else:
                # En cas d'échec de la réservation, annuler la création de commande et rétablir les stocks
                event.delete()
                return Response({'error': f'Not enough stock available for Medicm {medicament_id}'}, status=status.HTTP_400_BAD_REQUEST)
 
        return Response({'commande': serializer.data, 'reservations': created_reservations}, status=status.HTTP_201_CREATED)





#class OrdonnanceListCreateAPIView(generics.ListCreateAPIView):
#queryset = Ordonnance.objects.all()#serializer_class = OrdonnanceSerializer