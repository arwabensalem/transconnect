from django.db import models


class Expedition(models.Model):
    reference = models.CharField(max_length=20, unique=True)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    date_souhaitee = models.DateField()
    poids_kg = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=[('publiee', 'publiee'), ('attribuee', 'attribuee'), ('en_cours', 'en_cours'), ('livree', 'livree'), ('annulee', 'annulee')], default='publiee')
    entreprise = models.ForeignKey('EntreprisesApp.Entreprise', on_delete=models.CASCADE, related_name='expeditions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
