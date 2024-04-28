from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# pharmacie model
class Pharmacie (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default="")
    email=models.CharField(max_length=50)
    heure_ouv=models.DateTimeField(default=timezone.now)
    heure_ferm=models.DateTimeField(default=timezone.now)
    adresse=models.CharField(max_length=50, default="")
    medicament=models.ManyToManyField('Medicament', through='Pharma_Stock_Medic', related_name='medicament')

# medicament model
class Medicament (models.Model):
    nom=models.CharField(max_length=30)
    medic_image = models.ImageField(upload_to='medic_images/', blank=True, null=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, related_name='medicaments', default="")
    nompharmacie=models.CharField(max_length=30, default="")
    prix=models.FloatField(default=0)
    temps_liv=models.DateTimeField(default=timezone.now)

    quantite = models.IntegerField(default=0)   # stock = stock - qnt

    def __str__(self):
        return self.nom
       
# pharma_stock_medic model
class Pharma_Stock_Medic (models.Model):
    pharmacie=models.ForeignKey(Pharmacie, on_delete=models.CASCADE, related_name='pharmacie')
    medicament=models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='pharmacie')
    quantite=models.IntegerField(default=0)

# patient model
class Patient (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default="")
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=30)
    adresse=models.CharField(max_length=30)
    num=models.IntegerField(blank=True, null=True)
    email=models.CharField(max_length=50)
    
# livreur model
class Livreur  (models.Model): 
    user=models.OneToOneField(User, on_delete=models.CASCADE, default="")
    email=models.CharField(max_length=50)   
    commande=models.ManyToManyField('Commande', through='Livraison', related_name='commande', default="")
    
# categorie model   
class Categorie (models.Model):
   nom=models.CharField(max_length=30, default="")
   def __str__(self):
    return self.nom
    
# commande model
class Commande (models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1)
    cammande_reserved_medic = models.ManyToManyField('Medicament', through='Ligne_Commande', related_name='cammande_reserved_medic')
    cnam=models.ImageField(upload_to='cnam_img/', blank=True, null=True)
    description=models.CharField(max_length=30, default="", null=True)
    confirmadresse=models.CharField(max_length=30, default="", null=True)
    ordonnance=models.ImageField(upload_to='ordonnance_img/', null=True, default="")
    pharmacielocation=models.CharField(max_length=30 , default="",  null=True)

# ligne_commande model
class Ligne_Commande(models.Model):
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='reservations',default="1")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='reservations',default="")
    qnt = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.qnt} units commande for {self.medicament} in {self.commande}"

# livraison model
class Livraison (models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default="")
    orderStatus = models.CharField(max_length=50, default="")
    confirmationcode = models.IntegerField(blank=True, null=True)
    # Add foreign keys to Livreur and Commande
    livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE, related_name='livraisons_livreur', default="")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='livraisons_commande', default="")


    



 