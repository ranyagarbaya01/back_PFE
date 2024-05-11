from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#notification model
class Notification(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, default="")
    pharmacie = models.ForeignKey('Pharmacie', on_delete=models.CASCADE, default="")
    commande = models.ForeignKey('Commande', on_delete=models.CASCADE, default="")
    message = models.CharField(max_length=100)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message



# pharmacie model
class Pharmacie (models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, default="")
    email=models.CharField(max_length=50)
    heure_ouv=models.DateTimeField(default=timezone.now)
    heure_ferm=models.DateTimeField(default=timezone.now)
    codesecurite = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    medicament=models.ManyToManyField('Medicament', through='Pharma_Stock_Medic', related_name='medicament')
    role=models.CharField(max_length=30, default="pharmacie", blank=True, null=True) 


# medicament model
class Medicament (models.Model):
    nom=models.CharField(max_length=30)
    medic_image = models.ImageField(upload_to='medic_images/', blank=True, null=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, related_name='medicaments', default="")
    pharmaciemedic= models.ForeignKey(Pharmacie, on_delete=models.CASCADE, related_name="pharmaciemedicament" , default="")
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
    role=models.CharField(max_length=30, default="patient")
    
# livreur model
class Livreur  (models.Model): 
    user=models.OneToOneField(User, on_delete=models.CASCADE, default="")
    nom=models.CharField(max_length=30, default="")
    prenom=models.CharField(max_length=30, default="")
    num=models.IntegerField(blank=True, null=True)
    email=models.CharField(max_length=50, default="")   
    commande=models.ManyToManyField('Commande', through='Livraison', related_name='commande', default="")
    role=models.CharField(max_length=30, default="livreur")
# categorie model   
class Categorie (models.Model):
   nom=models.CharField(max_length=30, default="")
   def __str__(self):
    return self.nom
    
# commande model
class Commande (models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient" )#hhhhhhhh makch kaada t7ot fel patient howa el user li 3amel login, el logic hedheka aslan mch mawjoud, lazem fel fonction mta3 el creation tzidha dkika
    cammande_reserved_medic = models.ManyToManyField('Medicament', through='Ligne_Commande', related_name='cammande_reserved_medic')
    cnam=models.ImageField(upload_to='cnam_img/', blank=True, null=True)
    description=models.CharField(max_length=30, default="", null=True)
    confirmadresse=models.CharField(max_length=30, default="", null=True)
    ordonnance=models.ImageField(upload_to='ordonnance_img/', null=True, default="")
    pharmacies= models.ForeignKey(Pharmacie, on_delete=models.CASCADE, related_name="pharmaciecommande" , default="")

# ligne_commande model
class Ligne_Commande(models.Model):
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE, related_name='reservations',default="1")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='reservations',default="")
    qnt = models.IntegerField(default=0)
    pharmacielocation=models.CharField(max_length=30 , default="",  null=True)
    confirmadresse=models.CharField(max_length=30, default="", null=True)

    def __str__(self):
        return f"{self.qnt} units commande for {self.medicament} in {self.commande}"

# livraison model
class Livraison (models.Model):
    id_livraison = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default="")
    orderStatus = models.CharField(max_length=50, default="en livraison")
    confirmationcode = models.IntegerField(blank=True, null=True)
    # Add foreign keys to Livreur and Commande
    livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE, related_name='livraisons_livreur', default="")
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='livraisons_commande', default="")


