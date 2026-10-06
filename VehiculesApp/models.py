from django.db import models


class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=20, unique=True)
    type_vehicule = models.CharField(max_length=50, choices=[('camionnette', 'camionnette'), ('fourgon', 'fourgon'), ('camion_porteur', 'camion_porteur'), ('semi-remorque', 'semi-remorque')])
    capacite_kg = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    entreprise = models.ForeignKey('EntreprisesApp.Entreprise', on_delete=models.CASCADE, related_name='vehicules')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
