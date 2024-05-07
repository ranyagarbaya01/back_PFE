from rest_framework import serializers
from appk.models import *
from django.contrib.auth.models import User
from django import forms  

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','is_active')
        extra_kwargs = {'password': {'write_only': True}}
       



        

# User Serializer
class UserSerializerLogin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {'password': {'write_only': True}}



# medicament Serializer
class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = ('__all__')

# Categorie Serializer
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('__all__')

# Pharmacie Serializer   
class PharmacieSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Pharmacie
        fields = ('__all__')



    def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = User.objects.create_user(**user_data)
            pharmacie = Pharmacie.objects.create(user=user, **validated_data)
            return pharmacie


class PharmacieSerializerUpdate(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Pharmacie
        fields = ('__all__')
    
# Pharma_Stock_Medic Serializer
class Pharma_Stock_MedicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharma_Stock_Medic
        fields = ('__all__')

# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Patient
        fields = ('__all__') 

    def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = User.objects.create_user(**user_data)
            patient = Patient.objects.create(user=user, **validated_data)
            return patient
        

# reserver medicament Serializer
class ReserverMadicmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne_Commande
        fields = ('medicament', 'qnt')

# commande with medicament Serializer
class CommandeWithMedicamsSerializer(serializers.ModelSerializer):
    reservations = ReserverMadicmSerializer(many=True)  
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    patient_nom = serializers.SerializerMethodField()
    class Meta:
        model = Commande
        fields = ('__all__')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        patient = instance.patient
        patient_serializer = PatientSerializer(patient)
        representation['patient'] = patient_serializer.data
        return representation    

    
    def get_patient_nom(self, obj):
        return obj.patient.nom  


    def create(self, validated_data):
        reserved_medicmss_data = validated_data.pop('reservations')
        commande = Commande.objects.create(**validated_data)

        for reserved_medicm_data in reserved_medicmss_data:
            Ligne_Commande.objects.create(commande=commande, **reserved_medicm_data)
  
        return commande

# Ligne_Commande Serializer
class Ligne_CommandeSerializer(serializers.ModelSerializer):
    MedicamentName = serializers.CharField(source='medicament.nom', read_only=True)
    class Meta:
        model = Ligne_Commande
        fields = ('medicament','MedicamentName', 'qnt', 'commande')
    
# Livreur Serializer
class LivreurSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Livreur
        fields = ('__all__')
    
 
    def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = User.objects.create_user(**user_data)
            livreur = Livreur.objects.create(user=user, **validated_data)
            return livreur
 
# Commande Serializer
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = ('__all__')

# Livraison Serializer
class LivraisonSerializer(serializers.ModelSerializer):
    patientName = serializers.CharField(source='patient.nom', read_only=True)
    patientFamilyName = serializers.CharField(source='patient.prenom', read_only=True)
    patientPhone = serializers.CharField(source='patient.num', read_only=True)
    patientAddress = serializers.CharField(source='patient.adresse', read_only=True)
    class Meta:
        model = Livraison
        fields = ('id_livraison', 'patient', 'patientName', 'patientFamilyName', 'patientPhone', 'patientAddress', 'orderStatus', 'confirmationcode', 'livreur', 'commande')
    


