from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response
from appk.models import *
from appk.serializers import *
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from knox.models import AuthToken
from django.http import JsonResponse
from django.views import View
from django.views.generic import UpdateView
from .serializers import PatientSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view


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
    serializer_class = PharmacieSerializerUpdate

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
    queryset =   Patient.objects.all()
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

    def partial_update(self, request, *args, **kwargs):
        livraison = self.get_object()
        livraison.orderStatus = 'livré'
        livraison.save()
        return Response(self.get_serializer(livraison).data)

# deleting all livraisons
def delete_all_livraisons(request):
    Livraison.objects.all().delete()
    return JsonResponse({'message': 'All livraisons deleted successfully'})




from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Login_gn(APIView):
    serializer_class = UserSerializer
    aserializer_class = PatientSerializer
    mserializer_class = LivreurSerializer
    phserializer_class=PharmacieSerializer


    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'detail': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            if not user.is_active:
                return Response({'detail': 'Your account is not activated yet. Please contact the admin.'}, status=status.HTTP_401_UNAUTHORIZED)

            # token = AuthToken.objects.create(user)
            token, created = Token.objects.get_or_create(user=user)

            # Choix du serializer en fonction du type de l'utilisateur
            if hasattr(user, 'patient'):
                serializer = self.aserializer_class(user.patient)
            elif hasattr(user, 'livreur'):
                serializer = self.mserializer_class(user.livreur)
            elif hasattr(user, 'pharmacie'):
                serializer = self.phserializer_class(user.pharmacie)
            else:
                return Response({'detail': 'Invalid user type.'}, status=status.HTTP_400_BAD_REQUEST)
            print(token.key)
            return Response({
                'token': token.key,
                'user': serializer.data,
                
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)



# pass command with medicament
class CommandeWithMedicmCreateView(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeWithMedicamsSerializer

    def perform_create(self, serializer):
        print("test------------------")
        print("Sent data:", self.request.data)
        print("Current authenticated user:", self.request.user)
        headers = self.request.META
        print(headers)
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
            # confirmadresse = medicm_data.get('confirmadresse')
            # pharmacielocation = medicm_data.get('pharmacielocation')
            medicament = Medicament.objects.get(id=medicament_id)
            if medicament.quantite >= quantity:
                medicament.quantite -= quantity
                medicament.save()
            else:
                # En cas d'échec de la réservation, annuler la création de commande et rétablir les stocks
                commande.delete()
                return Response({'error': f'Not enough stock available for Medicm {medicament_id}'}, status=status.HTTP_400_BAD_REQUEST)
 
        return Response({'commande': serializer.data, 'reservations': created_reservations}, status=status.HTTP_201_CREATED)


# patient register
class PatientRegistreListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]


# Livreur register
class LivreurRegistreListView(generics.ListCreateAPIView):
    queryset = Livreur.objects.all()
    serializer_class = LivreurSerializer
    # permission_classes = [IsAuthenticated]


# pharmacie register
class PharmacieRegistreListView(generics.ListCreateAPIView):
    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer
    # permission_classes = [IsAuthenticated]

@api_view(['GET'])
def Command_by_user(request, user_id):
    try:
        commande = Commande.objects.filter(patient=user_id)
        serializer = CommandeWithMedicamsSerializer(commande, many=True)
        return Response(serializer.data, status=200)
    except Commande.DoesNotExist:
        return Response({'message': 'No Commande requests found for the specified user ID.'}, status=404)
    except Exception as e:
        return Response({'message': str(e)}, status=500)


@api_view(['GET'])
def Livreur_by_command(request, command_id):
    try:
        livreur = Livreur.objects.filter(commande=command_id)
        serializer = LivreurSerializer(livreur, many=True)
        return Response(serializer.data, status=200)
    except Livreur.DoesNotExist:
        return Response({'message': 'No livreur requests found for the specified command ID.'}, status=404)
    except Exception as e:
        return Response({'message': str(e)}, status=500)















# from rest_framework_simplejwt.tokens import AccessToken # type: ignore

# def decode_jwt_token(jwt_token):
#     try:
#         # Décodez le jeton en utilisant la méthode de la bibliothèque JWT
#         decoded_token = AccessToken(jwt_token)
        
#         # Récupérez les informations utiles du jeton décodé
#         user_id = decoded_token.payload['user_id']
#         user_username = decoded_token.payload['username']
#         user_role = decoded_token.payload['role']  # Si vous avez stocké le rôle dans le jeton
        
#         # Vous pouvez ajouter d'autres informations nécessaires
        
#         return {
#             'user_id': user_id,
#             'username': user_username,
#             'role': user_role,
#             # Ajoutez d'autres clés si nécessaire
#         }
#     except Exception as e:
#         # Gérer les erreurs de décodage ou d'autres exceptions
#         print("Erreur lors du décodage du jeton:", e)
#         return None

# patient login

# class PatientLoginViewj(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if not username or not password:
#             return Response({'detail': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(request, username=username, password=password)

#         if user is None:
#             return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             patient = Patient.objects.get(user=user)
#         except Patient.DoesNotExist:
#             return Response({'detail': 'No patient associated with this user.'}, status=status.HTTP_404_NOT_FOUND)

#         #Assuming you have a token authentication system for patients
#         token = AuthToken.objects.create(user)

#         return Response({
#             'token': token[1],
#             'patient': self.get_serializer(patient).data,}, status=status.HTTP_200_OK)
      




# pass command with medicament
# class CommandeWithMedicmCreateView(generics.ListCreateAPIView):
#     queryset = Commande.objects.all()
#     serializer_class = CommandeWithMedicamsSerializer

#     def perform_create(self, serializer):
#         commande = serializer.save()
#         # Récupérer les données de réservation de medicm
#         medicmss_data = self.request.data.get('reservations', [])
#         # Utiliser un ensemble pour stocker les meddic déjà réservés
#         reserved_medicm_set = set()
#         # Créer les réservations de medicm associées à commande
#         created_reservations = []
#         for medicm_data in medicmss_data:
#             medicament_id = medicm_data.get('medicament')
#             quantity = medicm_data.get('qnt')
#             #medicamentname = medicm_data.get('MedicamentName')
#             medicament = Medicament.objects.get(id=medicament_id)
#             if medicament.quantite >= quantity:
#                 medicament.quantite -= quantity
#                 medicament.save()
#             else:
#                 # En cas d'échec de la réservation, annuler la création de commande et rétablir les stocks
#                 commande.delete()
#                 return Response({'error': f'Not enough stock available for Medicm {medicament_id}'}, status=status.HTTP_400_BAD_REQUEST)
 
#         return Response({'commande': serializer.data, 'reservations': created_reservations}, status=status.HTTP_201_CREATED)


# livreur login
# @method_decorator(csrf_exempt, name='dispatch')
# class LivreurLoginView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def get(self, request, *args, **kwargs):
#         # Generate a CSRF token and set it in a cookie
#         get_token(request)
        
#         # Return a successful response
#         return Response({'detail': 'CSRF cookie set.'}, status=status.HTTP_204_NO_CONTENT)
    
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         print(username)
#         print(password)
#         if not username or not password:
#             return Response({'detail': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(request, username=username, password=password)

#         if user is None:
#             return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             livreur = Livreur.objects.get(user=user)
#         except Livreur.DoesNotExist:
#             return Response({'detail': 'No patient associated with this user.'}, status=status.HTTP_404_NOT_FOUND)

#         #Assuming you have a token authentication system for patients
#         token = AuthToken.objects.create(user)

#         return Response({
#             'token': token[1],
#             'livreur': self.get_serializer(livreur).data,}, status=status.HTTP_200_OK)




#class OrdonnanceListCreateAPIView(generics.ListCreateAPIView):
#queryset = Ordonnance.objects.all()#serializer_class = OrdonnanceSerializer


# interface DecodeToken extends JwtPayload {
#     isBoarded: boolean;}

# export const TOKEN_KEY: string = process.env.TOKEN_KEY || '';

# export async function verifyToken(request : Request): Promise<DecodeToken | null> {
#     const token ; string | null = await request.headers.get('Authorization');
#     if (!token) return null;
#     try {
#         return verify(token, TOKEN_KEY) as DecodeToken;
#     } catch (error) {
#         console.log("token verification errors", error);
#         return null;
#     }}

# export async function handleUnauthorized(){
#     return NextResponse.json({success: false, message: 'unauthorized: token is missing'}, {status: 401});}


# import jwt
# from django.conf import settings
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# @api_view(['POST'])
# def verifyToken(request):
#     token = request.headers.get('Authorization', '').split(' ')[-1] # Récupérer le token de l'en-tête
#     if not token:
#         return Response({'message': 'Token missing'}, status=status.HTTP_401_UNAUTHORIZED)
    
#     try:
#         decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#         # Faire quelque chose avec le token décrypté, par exemple vérifier les autorisations, etc.
#         return Response({'message': 'Token valid'}, status=status.HTTP_200_OK)
#     except jwt.ExpiredSignatureError:
#         return Response({'message': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)
#     except jwt.InvalidTokenError:
#         return Response({'message': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

# patient login

# class PatientLoginView(generics.CreateAPIView):
#     serializer_class = UserSerializerLogin
#     aserializer_class = PatientSerializer
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if not username or not password:
#             return Response({'detail': 'Please provide both username and password.'}, status=status.HTTP_400_BAD_REQUEST)
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:  
#             token = AuthToken.objects.create(user)
#             return Response({
#                 'token': token[1],
#                 'user': self.aserializer_class(user.patient).data,
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)



